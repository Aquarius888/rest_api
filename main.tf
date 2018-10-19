provider "aws" {
  region = "eu-central-1"
}

resource "aws_instance" "flask_rest_api" {
  ami = "ami-0233214e13e500f77"
  instance_type = "t2.micro"
  user_data = <<-EOF
              #!/bin/bash
              sudo yum install -y git
              sudo yum install -y docker
              sudo /etc/init.d/docker start
              git clone https://github.com/Aquarius888/rest_api.git
              cd rest_api
              cp settings.py.sample settings.py
              sudo docker build -t flask-rest-alpine:latest .
              sudo docker run -v "/opt/volume":/opt -d -p 5000:5000 flask-rest-alpine:latest
              EOF
  tags {
    Name = "flask_rest_api"
  }
}
