#!/bin/bash
# JSON post req
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
