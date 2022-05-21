#!/bin/bash

docker run --rm -it `
-v $pwd/videos:/mnt/videos `
-v $pwd/images:/mnt/images `
-u "ubuntu" `
exit_velocity:test /bin/bash