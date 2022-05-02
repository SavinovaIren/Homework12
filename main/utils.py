import json


def load_json(path):
    with open(path, 'r', encoding='utf-8') as file:
        return json.load(file)

def search_post_by_string(posts, string):
    post_list = []
    for post in posts:
        if string.lower() in post["content"].lower():
            post_list.append(post)
    return post_list





