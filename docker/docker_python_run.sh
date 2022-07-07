#!/bin/bash

docker run --rm -it \
-v /home/ubuntu/git/baseball_exit_velocity/:/home/ubuntu/exit_velocity \
-u ${USER} \
exit_velocity:test ./docker/entrypoint.sh