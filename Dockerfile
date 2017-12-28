FROM ubuntu

MAINTAINER Ryuichi Ogawa

RUN apt-get update

RUN apt-get install -y python-pip 

COPY . /opt/app

WORKDIR /opt/app

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "run.py"]