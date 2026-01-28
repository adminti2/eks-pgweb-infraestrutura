from flask import Flask, jsonify
import socket
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
        <head>
            <title>PGWEB - Test App</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    max-width: 800px;
                    margin: 50px auto;
                    padding: 20px;
                    background: #f0f0f0;
                }
                .container {
                    background: white;
                    padding: 30px;
                    border-radius: 10px;
                    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                }
                h1 { color: #2c3e50; }
                .info { 
                    background: #ecf0f1;
                    padding: 15px;
                    border-radius: 5px;
                    margin: 10px 0;
                }
                .status { color: #27ae60; font-weight: bold; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🚀 PGWEB Application - Running!</h1>
                <div class="info">
                    <p><strong>Status:</strong> <span class="status">✓ Online</span></p>
                    <p><strong>Container:</strong> ''' + socket.gethostname() + '''</p>
                    <p><strong>Environment:</strong> ''' + os.getenv('ENV', 'development') + '''</p>
                    <p><strong>Version:</strong> 1.0.0</p>
                    <p><strong>Timestamp:</strong> ''' + str(datetime.now()) + '''</p>
                </div>
                <p>✅ Infrastructure successfully deployed!</p>
            </div>
        </body>
    </html>
    '''

@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'hostname': socket.gethostname(),
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/info')
def info():
    return jsonify({
        'app': 'pgweb-hom-muxx',
        'version': '1.0.0',
        'environment': os.getenv('ENV', 'development'),
        'container': socket.gethostname()
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)
