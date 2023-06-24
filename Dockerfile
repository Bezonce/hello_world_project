# app/Dockerfile
FROM python:3.8-slim-buster

# set the working directory
WORKDIR /app

# install dependencies
COPY ./requirements.txt /app
RUN pip install --no-cache-dir --upgrade -r requirements.txt



# Copy the source code into the container
COPY . /app
ENV FLASK_APP=hello.py
ENV FLASK_DEBUG=1

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000"]