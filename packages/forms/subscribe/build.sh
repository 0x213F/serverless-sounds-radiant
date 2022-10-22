#!/bin/bash

echo "hello 1"
set -e

echo "hello 2"
virtualenv --without-pip virtualenv
echo "hello 3"
pip install -r requirements.txt --target virtualenv/lib/python3.9/site-packages
