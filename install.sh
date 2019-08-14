#!/usr/bin/env sh

mkdir -p src/python
yum install -y python3 zip
pip3 install psycopg2-binary -t src/python

