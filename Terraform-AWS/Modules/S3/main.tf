# this create an S3 bucket
resource "aws_s3_bucket" "terraform_state" {
  bucket = var.bucket_name
  tags = {
    Name        = var.bucket_name
    description = var.description
  }
}