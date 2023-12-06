#!/usr/bin/python3
"""Uses the GitHub API to display a GitHub ID based on given credentials.

Usage: ./10-my_github.py <GitHub username> <GitHub password>
  - Uses Basic Authentication to access the ID.
"""
import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    # Set up Basic Authentication using the provided GitHub username and password
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])

    # Send a GET request to the GitHub API to retrieve user information
    r = requests.get("https://api.github.com/user", auth=auth)

    # Print the GitHub user ID
    print(r.json().get("id"))

# Ensure there is a newline at the end of the file
