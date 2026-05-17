import json
from models import User, Movie


def load_data():
    with open("users.json", "r") as f:
        u_data = json.load(f)

    users = {}

    for u in u_data:
        users[u["user_id"]] = User(
            u["user_id"],
            u["username"],
            u["watched"]
        )

    with open("items.json", "r") as f:
        i_data = json.load(f)

    movies = [
        Movie(i["id"], i["title"], i["genre"], i["duration"])
        for i in i_data
    ]

    return users, movies


def save_new_history(user_id, new_movie_title):

    with open("users.json", "r") as f:
        data = json.load(f)

    for u in data:
        if u["user_id"] == user_id:
            if new_movie_title not in u["watched"]:
                u["watched"].append(new_movie_title)

    with open("users.json", "w") as f:
        json.dump(data, f, indent=2)