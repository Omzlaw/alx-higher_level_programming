#!/usr/bin/python3
"""Sends a POST request to http://0.0.0.0:5000/search_user with a given letter.

Usage: ./8-json_api.py <letter>
  - The letter is sent as the value of the variable `q`.
  - If no letter is provided, sends `q=""`.
"""
import sys
import requests

if __name__ == "__main__":
    # Determine the letter to search for (default to empty string if not provided)
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": letter}

    # Send a POST request to the specified URL with the payload
    r = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        # Attempt to parse the response as JSON
        response = r.json()

        # Check if the response is empty
        if response == {}:
            print("No result")
        else:
            # Print the response information
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")

# Ensure there is a newline at the end of the file
