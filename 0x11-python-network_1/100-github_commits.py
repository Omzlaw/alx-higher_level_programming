#!/usr/bin/python3
"""Lists the 10 most recent commits on a given GitHub repository.

Usage: ./100-github_commits.py <repository name> <repository owner>
"""
import sys
import requests

if __name__ == "__main__":
    # Construct the URL for the GitHub API based on provided repository name and owner
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    # Send a GET request to the GitHub API to retrieve commit information
    r = requests.get(url)
    commits = r.json()

    try:
        # Print information for the 10 most recent commits
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass

# Ensure there is a newline at the end of the file
