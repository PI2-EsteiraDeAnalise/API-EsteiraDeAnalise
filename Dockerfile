FROM debian:stable

WORKDIR /app

ARG DEBIAN_FRONTEND=noninteractive
ARG DEBCONF_NOWARNINGS="yes"

COPY ./requirements.txt /app

RUN apt-get update && \
  apt-get install --no-install-recommends -y \
  python3-pip

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 5000

ENTRYPOINT ["./docker_entrypoint.sh"]
