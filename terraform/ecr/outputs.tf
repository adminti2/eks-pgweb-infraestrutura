output "repository_url" {
  description = "ECR repository URL"
  value       = aws_ecr_repository.pgweb.repository_url
}

output "repository_arn" {
  description = "ECR repository ARN"
  value       = aws_ecr_repository.pgweb.arn
}

output "repository_name" {
  description = "ECR repository name"
  value       = aws_ecr_repository.pgweb.name
}

output "docker_login" {
  description = "Docker login command"
  value       = "aws ecr get-login-password --region ${var.aws_region} | docker login --username AWS --password-stdin ${aws_ecr_repository.pgweb.repository_url}"
}

output "docker_push" {
  description = "Docker push command"
  value       = "docker tag pgweb-hom-muxx:latest ${aws_ecr_repository.pgweb.repository_url}:latest && docker push ${aws_ecr_repository.pgweb.repository_url}:latest"
}
