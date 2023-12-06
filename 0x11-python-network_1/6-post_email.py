#!/usr/bin/python3
"""Sends a POST request to a given URL with a given email.

Usage: ./6-post_email.py <URL> <email>
  - Displays the body of the response.
"""
import sys
import requests

if __name__ == "__main__":
    # Get the URL and email from the command-line arguments
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    # Send a POST request to the specified URL with the given email
    r = requests.post(url, data=value)

    # Print the body of the response
    print(r.text)

# Ensure there is a newline at the end of the file
