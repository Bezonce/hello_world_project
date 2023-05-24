# app/Dockerfile
FROM python:latest

# set the working directory
WORKDIR /app

# install dependencies
COPY ./requirements.txt /app
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy the source code into the container
COPY . /app

EXPOSE 8501

CMD ["streamlit", "run", "src/streamlit_app.py"]