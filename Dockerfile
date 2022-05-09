FROM ubuntu:18.04

ARG USER=myuser
RUN useradd -m -s /bin/bash -G sudo $USER

RUN apt-get update
RUN apt-get install -y --no-install-recommends \
    sudo \
    curl \
    lsb-release \
    python3-pip \
    python3-setuptools \
    git

USER $USER
WORKDIR /home/${USER}/
ADD workspace /home/${USER}/workspace/

RUN pip3 install --upgrade pip
RUN pip3 install opencv-python

