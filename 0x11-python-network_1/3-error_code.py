#!/usr/bin/python3
"""Sends a request to a given URL and displays the response body.

Usage: ./3-error_code.py <URL>
  - Handles HTTP errors.
"""
import sys
import urllib.error
import urllib.request

if __name__ == "__main__":
    # Get the URL from the command-line arguments
    url = sys.argv[1]

    # Create a request and handle HTTP errors
    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as response:
            # Print the response body
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as e:
        # Print the HTTP error code
        print("Error code: {}".format(e.code))

# Ensure there is a newline at the end of the file
