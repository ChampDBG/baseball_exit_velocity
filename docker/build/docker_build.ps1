#!/bin/bash

docker build -t exit_velocity:test -f ./docker/build/Dockerfile --build-arg USER=ubuntu .