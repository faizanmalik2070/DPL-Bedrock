

variable "aws_region" {
  default = "us-east-1"
}

variable "project_name" {
  default = "my-project"
}

variable "environment" {
  default = "dev"
}

variable "lambda_name" {
  default = "my-terraform-lambda"
}

variable "lambda_runtime" {
  default = "python3.12"
}

variable "lambda_handler" {
  default = "handler.lambda_handler"
}

variable "lambda_memory" {
  default = 256
}

variable "lambda_timeout" {
  default = 10
}

variable "lambda_env" {
  type = map(string)
  default = {
    STAGE = "dev"
  }
}
