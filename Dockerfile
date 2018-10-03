FROM python:3.6-alpine as base 

FROM base as builder

RUN mkdir /install
WORKDIR /install

COPY requirements.txt /requirements.txt

RUN pip3 install --install-option="--prefix=/install" -r /requirements.txt

FROM base

COPY --from=builder /install /usr/local

COPY . /app
WORKDIR /app
EXPOSE 5000
ENTRYPOINT ["python3"]
CMD ["app.py"]

