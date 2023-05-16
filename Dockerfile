FROM python:3.9.2-buster

WORKDIR /app/Kodla
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN export FLASK_APP=app
EXPOSE 5000

CMD flask run --host 0.0.0.0