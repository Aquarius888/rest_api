# rest_api
Test project for MRC(Epam)

## Usage

1. git clone https://github.com/Aquarius888/rest_api.git
2. cd rest_api
3. cp settings.py.sample settings.py
4. docker build -t flask-rest-alpine:latest .
5. docker run -v "/opt/volume":/opt -d -p 5000:5000 flask-rest-alpine:latest

### Check
6. curl -i -X POST -F file=@<path_and_name_of_uploaded_file> http://localhost:5000/api/v1
7. curl -i http://localhost:5000/api/v1/new_poem.txt
8. cat /opt/volume/occurrancies.txt
