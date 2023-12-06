#!/usr/bin/python3
"""Displays the X-Request-Id header variable of a request to a given URL.

Usage: ./5-hbtn_header.py <URL>
"""
import sys
import requests

if __name__ == "__main__":
    # Get the URL from the command-line arguments
    url = sys.argv[1]

    # Send a GET request to the specified URL
    r = requests.get(url)

    # Print the value of the X-Request-Id header
    print(r.headers.get("X-Request-Id"))

# Ensure there is a newline at the end of the file
