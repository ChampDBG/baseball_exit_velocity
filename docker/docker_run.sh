#!/bin/bash

docker run --rm -it \
-u ${USER} \
exit_velocity:test ./docker/entrypoint.sh