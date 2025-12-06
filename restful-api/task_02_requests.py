def fetch_and_save_posts():
    """Fetch posts and save them into posts.csv"""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        filtered = [
            {"id": post["id"], "title": post["title"], "body": post["body"]}
            for post in data
        ]

        with open("posts.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(filtered)
