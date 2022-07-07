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

RUN apt-get install -y --no-install-recommends \
    libgl1-mesa-dev \
    libglib2.0-0 \
    libsm6 \
    libxrender1 \
    libxext6

RUN pip3 install --upgrade pip
RUN python3 -m pip install opencv-contrib-python

USER $USER
RUN mkdir /home/${USER}/exit_velocity
WORKDIR /home/${USER}/exit_velocity
COPY ./ /home/${USER}/exit_velocity
