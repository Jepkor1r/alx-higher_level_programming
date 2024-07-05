#!/bin/bash
# send a POST request with file contents, first arg=url, second args=filename
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
