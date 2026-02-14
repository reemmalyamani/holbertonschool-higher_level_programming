#!/usr/bin/python3
"""
Task 02: Consuming and processing data from an API using Python
"""

import csv
import requests

URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """
    Fetch all posts from JSONPlaceholder and print:
    - Status Code: <code>
    - titles of all posts (one per line) if successful
    """
    try:
        response = requests.get(URL, timeout=10)
    except requests.RequestException:
        # If there's a network error, we still shouldn't crash the program.
        # The task only requires printing the status code on success,
        # so we simply return here.
        return

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get("title", ""))


def fetch_and_save_posts():
    """
    Fetch all posts from JSONPlaceholder and save them into posts.csv
    with columns: id, title, body (if successful)
    """
    try:
        response = requests.get(URL, timeout=10)
    except requests.RequestException:
        return

    if response.status_code != 200:
        return

    posts = response.json()

    structured_posts = [
        {
            "id": post.get("id"),
            "title": post.get("title"),
            "body": post.get("body"),
        }
        for post in posts
    ]

    fieldnames = ["id", "title", "body"]

    with open("posts.csv", mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(structured_posts)

