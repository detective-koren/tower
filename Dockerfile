FROM python

# 한글설정
RUN apt-get update && apt-get install -y locales
RUN locale-gen ko_KR.UTF-8
ENV LC_ALL ko_KR.UTF-8

ENV PYTHONUNBUFFERED 1 
RUN mkdir /src 
WORKDIR /src 

ADD . /src/
ADD requirements.txt /src/
RUN pip3 install -r requirements.txt

EXPOSE 8000