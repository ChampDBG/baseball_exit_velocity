#!/bin/bash

docker build -t exit_velocity:test -f ./docker/Dockerfile --build-arg USER=ubuntu .