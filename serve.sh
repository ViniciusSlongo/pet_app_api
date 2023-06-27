#!/bin/sh

gunicorn src.app:app -b 0.0.0.0:5002 -w 1 --timeout 900 
