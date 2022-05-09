#!/bin/bash

docker run --rm -it `
-v ./videos:/mnt/videos `
-v ./images:/mnt/images `
-u "wu" `
exit_velocity:test /bin/bash