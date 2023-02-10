#!/bin/bash

# Remove the old container
docker rm -f weather-bot

# Build the new image
docker build --network=host -t weather-bot .

# Run the new container
docker run --network=host -d --name weather-bot weather-bot
