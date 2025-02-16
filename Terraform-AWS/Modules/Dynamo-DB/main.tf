resource "aws_dynamodb_table" "terraform_locks" {
  name         = var.dynamo_db_name_remote-backend
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = var.hash_key

  attribute {
    name = var.hash_key
    type = "S"
  }
}