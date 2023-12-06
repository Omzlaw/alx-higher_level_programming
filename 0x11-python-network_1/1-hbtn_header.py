#!/usr/bin/python3
"""Displays the X-Request-Id header variable of a request to a given URL.

Usage: ./1-hbtn_header.py <URL>
"""
import sys
import urllib.request

if __name__ == "__main__":
    # Get the URL from the command-line arguments
    url = sys.argv[1]

    # Create a request and open the URL
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        # Print the X-Request-Id header value
        print(dict(response.headers).get("X-Request-Id"))

# Ensure there is a newline at the end of the file
