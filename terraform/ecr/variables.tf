variable "aws_region" {
  description = "AWS Region"
  type        = string
  default     = "us-east-1"
}

variable "repository_name" {
  description = "ECR repository name"
  type        = string
  default     = "pgweb-hom-muxx"
}

variable "environment" {
  description = "Environment"
  type        = string
  default     = "hom"
}
