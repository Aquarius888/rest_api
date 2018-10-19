# rest_api
Test project for MRC(Epam)

## Automation Usage

1. Requirements:
1.1 installed and configured terraform
1.2 exported AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY
2. git clone https://github.com/Aquarius888/rest_api.git
3. cd rest_api
4. terraform plan
5. terraform apply (yes)

## Manual Usage

1. git clone https://github.com/Aquarius888/rest_api.git
2. cd rest_api
3. cp settings.py.sample settings.py
4. docker build -t flask-rest-alpine:latest .
5. docker run -v "/opt/volume":/opt -d -p 5000:5000 flask-rest-alpine:latest

### Check
6. curl -i -X POST -F file=@<path_and_name_of_upload_file> http://<server_IP>:5000/api/v1
7. curl -i http://<server_IP>:5000/api/v1/new_poem.txt
8. cat /opt/volume/occurrancies.txt
