class Item:
    def init(self, item_id, genre):
        self.id = item_id
        self.genre = genre

class User:
    def init(self, user_id, liked_items):
        self.user_id = user_id
        self.liked_items = set(liked_items)

    def str(self):
        return f"User {self.user_id} | Items: {len(self.liked_items)}"

    class RecommendationEngine:
        def init(self, users):
            self.users = users