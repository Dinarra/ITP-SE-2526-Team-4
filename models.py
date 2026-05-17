class Item:
    def init(self, item_id, genre):
        self.id = item_id
        self.genre = genre

class User:
    def init(self, user_id, liked_items):
        self.user_id = user_id
        self.liked_items = set(liked_items)