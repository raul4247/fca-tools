FROM ubuntu:18.04
RUN apt-get update && apt-get install -y --no-install-recommends python3 python3-virtualenv

WORKDIR /src
COPY src/ .
