#!/bin/bash
# Takes in a URL as first arg, sends POST request, and displays the response body.
curl -s -X POST -d 'email=test@gmail.com&subject=I will always be here for PLD' "$1"
