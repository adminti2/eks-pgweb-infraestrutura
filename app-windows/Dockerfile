FROM mcr.microsoft.com/dotnet/framework/aspnet:4.8-windowsservercore-ltsc2022

SHELL ["powershell", "-Command", "$ErrorActionPreference = 'Stop';"]

# Remover site padrão
RUN Remove-Website -Name 'Default Web Site'; \
    Remove-Item -Path 'C:\inetpub\wwwroot\*' -Recurse -Force

# Criar diretórios
RUN New-Item -Path 'C:\inetpub\Block' -ItemType Directory -Force; \
    New-Item -Path 'C:\Setis\Muxx' -ItemType Directory -Force

# Copiar inetpub\Block (site IIS)
COPY app-content/inetpub-block/ C:/inetpub/Block/

# Copiar C:\Setis\Muxx (aplicação backend)
COPY app-content/setis-muxx/ C:/Setis/Muxx/

# Limpar configuração defaultDocument
RUN Clear-WebConfiguration -PSPath 'MACHINE/WEBROOT/APPHOST' -Filter 'system.webServer/defaultDocument/files' -ErrorAction SilentlyContinue

# Criar site IIS "Muxx" apontando para C:\inetpub\Block
RUN New-Website -Name 'Muxx' \
                -Port 80 \
                -PhysicalPath 'C:\inetpub\Block' \
                -ApplicationPool '.NET v4.5'

# Configurar permissões
RUN icacls 'C:\inetpub\Block' /grant 'IIS_IUSRS:(OI)(CI)F' /T; \
    icacls 'C:\inetpub\Block' /grant 'IUSR:(OI)(CI)F' /T; \
    icacls 'C:\Setis\Muxx' /grant 'IIS_IUSRS:(OI)(CI)F' /T; \
    icacls 'C:\Setis\Muxx' /grant 'IUSR:(OI)(CI)F' /T

# Habilitar anonymous authentication
RUN Set-WebConfigurationProperty -Filter '/system.webServer/security/authentication/anonymousAuthentication' -Name Enabled -Value True -PSPath 'IIS:\Sites\Muxx' -ErrorAction SilentlyContinue

# Resetar IIS
RUN iisreset

EXPOSE 80

HEALTHCHECK --interval=30s --timeout=5s --start-period=90s --retries=3 \
    CMD powershell -command \
    try { \
        $response = Invoke-WebRequest http://localhost:80 -UseBasicParsing -TimeoutSec 3; \
        if ($response.StatusCode -eq 200) { exit 0 } else { exit 1 }; \
    } catch { exit 1 }
