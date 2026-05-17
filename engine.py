def get_similar_users(target_user, all_users):
    similar = []
    for user in all_users:
        if user.user_id != target_user.user_id:
            if target_user.liked_items.intersection(user.liked_items):
                similar.append(user)
    return similar