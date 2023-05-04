#!/bin/bash

docker build -t joga-bonito-tech .
docker run -p 8501:8501 joga-bonito-tech