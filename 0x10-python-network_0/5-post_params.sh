#!/bin/bash
# Script that ends a POST request to the passed URL
cur -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
