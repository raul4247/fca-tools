FROM ubuntu:21.10
RUN apt-get update
RUN apt-get autoclean
RUN apt-get install -y --no-install-recommends python3 python3-pip vim

ENV PATH "$PATH:/src"
ENV PYTHONPATH "$PYTHONPATH:/src"

COPY setup.py .
COPY requirements.txt .
COPY src/ .
ADD src/ src/
RUN python3 setup.py install
RUN pip3 install -r requirements.txt

# Installing Data Peeler
RUN apt-get install -y --no-install-recommends build-essential
RUN apt-get install -y --no-install-recommends libboost-all-dev
WORKDIR /src/fcatools/d-peeler
RUN make install

WORKDIR /src
