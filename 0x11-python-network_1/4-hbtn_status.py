#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status."""
import requests

if __name__ == "__main__":
    # Send a GET request to the specified URL
    r = requests.get("https://alx-intranet.hbtn.io/status")

    # Print information about the response body
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))

# Ensure there is a newline at the end of the file
