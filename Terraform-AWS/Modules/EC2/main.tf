resource "aws_instance" "ec2_instance" {
  ami                    = var.ami
  instance_type          = var.instance_type
  subnet_id = var.public_subnets_id[0]
  vpc_security_group_ids = [var.security_group_id]
  tags = {
    Name = var.server_name
  }
}