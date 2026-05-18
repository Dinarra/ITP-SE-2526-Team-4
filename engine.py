def get_similar_users(target_user, all_users_dict):
    similar = []
    for u_id, user in all_users_dict.items():
        if u_id != target_user.user_id:
            if target_user.watched_history.intersection(user.watched_history):
                similar.append(user)
    return similar