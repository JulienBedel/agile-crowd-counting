#!/bin/sh
docker build --tag agile-counting .
docker run -p 5000:5000 --rm -it agile-counting