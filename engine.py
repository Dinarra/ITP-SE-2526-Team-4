def get_similar_users(target_user, all_users_dict):
    similar = []
    for u_id, user in all_users_dict.items():
        if u_id != target_user.user_id:
            if target_user.watched_history.intersection(user.watched_history):
                similar.append(user)
    return similar

def generate_recommendations(target_user, similar_users):
    recommended_set = set()
    for other in similar_users:
        unwatched = other.watched_history - target_user.watched_history
        for movie_title in unwatched:
            if movie_title not in recommended_set:
                recommended_set.add(movie_title)
                yield movie_title

def get_movies_by_genre(movies_list, genre):
    return list(filter(lambda m: m.genre.lower() == genre.lower(), movies_list))