FROM python:3.9-alpine
LABEL Karm Designs

# To keep the app from Unbuffering
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app/

# Create a seperate user for running the process so anyone with access would not have permission to the root user
RUN adduser -D user
USER user