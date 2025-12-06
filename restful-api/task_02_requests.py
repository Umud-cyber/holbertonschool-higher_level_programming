import requests
import csv
import sys
from typing import List, Dict, Any

# Define the base URL for the JSONPlaceholder API
API_URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts() -> None:
    """
    Fetches all posts from JSONPlaceholder, prints the status code,
    and then prints the title of each post.
    """
    print("--- Fetch and Print Posts ---")
    try:
        # Send a GET request to the API_URL
        response = requests.get(API_URL)

        # Print the status code
        print(f"Status Code: {response.status_code}")

        # Check if the request was successful (2xx status codes)
        response.raise_for_status()

        # Parse the JSON data into a Python list of dictionaries
        posts: List[Dict[str, Any]] = response.json()

        # Iterate through the parsed data and print the title of each post
        for post in posts:
            print(post.get("title"))

    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error occurred: {e}", file=sys.stderr)
    except requests.exceptions.ConnectionError as e:
        print(f"Connection Error occurred: {e}", file=sys.stderr)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred during request: {e}", file=sys.stderr)


# ---
def fetch_and_save_posts() -> None:
    """
    Fetches all posts, structures the data (id, title, body),
    and writes it to a CSV file named posts.csv.
    """
    print("\n--- Fetch and Save Posts to CSV ---")
    try:
        # Send a GET request
        response = requests.get(API_URL)
        response.raise_for_status()

        # Parse the JSON data
        posts_data: List[Dict[str, Any]] = response.json()

        # Structure the data into a list of dictionaries with specific keys (id, title, body)
        # We use a list comprehension for concise data structuring.
        structured_data: List[Dict[str, Any]] = [
            {
                'id': post.get('id'),
                'title': post.get('title'),
                'body': post.get('body')
            }
            for post in posts_data
        ]

        # Define the file name and the field names for the CSV header
        csv_file = 'posts.csv'
        fieldnames = ['id', 'title', 'body']

        # Write the data to a CSV file
        with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
            # Initialize DictWriter, mapping dictionary keys to CSV columns
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Write the header row
            writer.writeheader()

            # Write the post data rows
            writer.writerows(structured_data)

        print(f"Successfully wrote {len(structured_data)} posts to {csv_file}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred during request: {e}", file=sys.stderr)
    except IOError as e:
        print(f"An error occurred while writing to CSV: {e}", file=sys.stderr)


if __name__ == '__main__':
    # This block is used for testing the functions directly if run outside of main_02_requests.py
    fetch_and_print_posts()
    fetch_and_save_posts()import requests
import csv
import sys
from typing import List, Dict, Any

# Define the base URL for the JSONPlaceholder API
API_URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts() -> None:
    """
    Fetches all posts from JSONPlaceholder, prints the status code,
    and then prints the title of each post.
    """
    print("--- Fetch and Print Posts ---")
    try:
        # Send a GET request to the API_URL
        response = requests.get(API_URL)

        # Print the status code
        print(f"Status Code: {response.status_code}")

        # Check if the request was successful (2xx status codes)
        response.raise_for_status()

        # Parse the JSON data into a Python list of dictionaries
        posts: List[Dict[str, Any]] = response.json()

        # Iterate through the parsed data and print the title of each post
        for post in posts:
            print(post.get("title"))

    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error occurred: {e}", file=sys.stderr)
    except requests.exceptions.ConnectionError as e:
        print(f"Connection Error occurred: {e}", file=sys.stderr)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred during request: {e}", file=sys.stderr)


# ---
def fetch_and_save_posts() -> None:
    """
    Fetches all posts, structures the data (id, title, body),
    and writes it to a CSV file named posts.csv.
    """
    print("\n--- Fetch and Save Posts to CSV ---")
    try:
        # Send a GET request
        response = requests.get(API_URL)
        response.raise_for_status()

        # Parse the JSON data
        posts_data: List[Dict[str, Any]] = response.json()

        # Structure the data into a list of dictionaries with specific keys (id, title, body)
        # We use a list comprehension for concise data structuring.
        structured_data: List[Dict[str, Any]] = [
            {
                'id': post.get('id'),
                'title': post.get('title'),
                'body': post.get('body')
            }
            for post in posts_data
        ]

        # Define the file name and the field names for the CSV header
        csv_file = 'posts.csv'
        fieldnames = ['id', 'title', 'body']

        # Write the data to a CSV file
        with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
            # Initialize DictWriter, mapping dictionary keys to CSV columns
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Write the header row
            writer.writeheader()

            # Write the post data rows
            writer.writerows(structured_data)

        print(f"Successfully wrote {len(structured_data)} posts to {csv_file}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred during request: {e}", file=sys.stderr)
    except IOError as e:
        print(f"An error occurred while writing to CSV: {e}", file=sys.stderr)


if __name__ == '__main__':
    # This block is used for testing the functions directly if run outside of main_02_requests.py
    fetch_and_print_posts()
    fetch_and_save_posts()
