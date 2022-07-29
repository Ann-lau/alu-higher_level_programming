#!/bin/bash
# takes in a URL as an argument
curl -sG "$1" -H "X-School-User-Id: 98"
