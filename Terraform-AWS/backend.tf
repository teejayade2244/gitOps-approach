terraform {
  backend "s3" {
    bucket         = var.state_locking_s3_bucket_name
    key            = "terraform.tfstate"
    region         = var.region
    dynamodb_table = var.dynamo_db_name_remote-backend 
    encrypt        = true
  }
}
