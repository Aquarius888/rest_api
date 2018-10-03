# rest_api
Test project for MRK(Epam)

## Usage

1. git clone https://github.com/Aquarius888/rest_api.git
2. cd rest_api
3. docker build -t flask-rest:latest .
4. docker run -v "/opt/volume":$STORAGE -d -p 5000:5000 flask-rest:latest
