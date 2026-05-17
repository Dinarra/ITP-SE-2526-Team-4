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
class Movie(Content):
    def __init__(self, content_id, title, genre, duration):
        super().__init__(content_id, title, genre)
        self.duration = duration

    # Polymorphism: переопределение метода
    def get_details(self):
        return f"🎬 Movie: {self.title} ({self.duration} min) | Genre: {self.genre}"

# Inheritance: ActiveUser наследует Viewer
class User(Viewer):
    def __init__(self, user_id, username, watched_history):
        super().__init__(username)
        # Encapsulation: приватные атрибуты
        self.__user_id = user_id
        self.__watched_history = set(watched_history)

    @property
    def user_id(self):
        return self.__user_id

    @property
    def watched_history(self):
        return self.__watched_history

    # Polymorphism: переопределение метода
    def get_role_profile(self):
        return f"👤 Active User: {self.username}"