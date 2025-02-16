terraform {
  backend "s3" {
    bucket         = "Terraform_state_lock_remote-backend"
    key            = "terraform.tfstate"
    region         = "eu-west-2"
    dynamodb_table = "Terraform_state_remote-backend"
    encrypt        = true
  }
}
