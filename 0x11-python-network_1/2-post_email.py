#!/usr/bin/python3
"""Sends a POST request to a given URL with a given email.

Usage: ./2-post_email.py <URL> <email>
  - Displays the body of the response.
"""
import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
    # Get the URL and email from the command-line arguments
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    # Encode the data and create a POST request
    data = urllib.parse.urlencode(value).encode("ascii")
    request = urllib.request.Request(url, data)

    # Open the URL and print the response body
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))

# Ensure there is a newline at the end of the file
