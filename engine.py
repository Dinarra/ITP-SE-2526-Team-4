def get_similar_users(target_user, all_users):
    similar = []
    for user in all_users:
        if user.user_id != target_user.user_id:
            if target_user.liked_items.intersection(user.liked_items):
                similar.append(user)
    return similar

def generate_recommendations(target_user, similar_users):
    recommended = set()
    for other in similar_users:
        new_items = other.liked_items - target_user.liked_items
        for item in new_items:
            if item not in recommended:
                recommended.add(item)
                yield item