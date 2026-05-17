class Content:
    def __init__(self, content_id, title, genre):
        self.id = content_id
        self.title = title
        self.genre = genre

    def get_details(self):
        return f"{self.title} [{self.genre}]"

# Base Class for Inheritance
class Viewer:
    def __init__(self, username):
        self.username = username

    def get_role_profile(self):
        return f"Guest Viewer: {self.username}"