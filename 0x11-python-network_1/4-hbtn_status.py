#!/usr/bin/python3
"""
Script that fetches https://alx-intranet.hbtn.io/status
Uses the requests package
"""

import requests

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)
    content = response.text
    content_type = type(content).__name__

    print("Body response:")
    print("\t- type:", content_type)
    print("\t- content:", content)

