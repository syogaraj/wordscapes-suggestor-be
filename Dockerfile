FROM python:3.8-slim-buster
WORKDIR /app
COPY . /app
#COPY requirements.txt .

RUN apt-get -y update && apt-get -y upgrade && apt-get install -y enchant
RUN python -m pip install -r requirements.txt
#EXPOSE ${PORT:-5000}

CMD uvicorn main:app --host=0.0.0.0 --port=${PORT:-5000}