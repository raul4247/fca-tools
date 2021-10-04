FROM ubuntu:18.04
RUN apt-get update && apt-get install -y --no-install-recommends python3 python3-pip

WORKDIR /src
COPY src/ .
COPY requirements.txt .

RUN pip3 install -r requirements.txt

# Installing Data Peeler
RUN apt-get install -y --no-install-recommends build-essential
RUN apt-get install -y --no-install-recommends libboost-all-dev
WORKDIR /src/fcatools/d-peeler
RUN make install

WORKDIR /src
