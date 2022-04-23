FROM debian:unstable-slim

WORKDIR /app

ARG DEBIAN_FRONTEND=noninteractive
ARG DEBCONF_NOWARNINGS="yes"

COPY ./requirements.txt /app

RUN apt-get update && \
  apt-get install --no-install-recommends -y \
  python3-pip

RUN pip install -r requirements.txt

COPY ./src /app

RUN flask db init && \
  flask db migrate && \
  flask db upgrade

WORKDIR /app/src

EXPOSE 5000

ENTRYPOINT ["python3", "app.py"]
