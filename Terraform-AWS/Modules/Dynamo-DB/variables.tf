variable "dynamo_db_name_remote-backend" {
  type = string
  description = "Dynamo-db name for the s3 state lock"
}

variable "hash_key" {
  type = string
  default     = "LockID" 
}