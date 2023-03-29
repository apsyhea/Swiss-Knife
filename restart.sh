#!/bin/bash
git pull github master && docker-compose stop && docker-compose build && docker-compose up -d
