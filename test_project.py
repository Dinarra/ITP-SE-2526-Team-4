from models import User
from engine import get_similar_users


def test_similarity_logic():
    test_users = {
        1: User(1, "Alice", ["MovieA", "MovieB"]),
        2: User(2, "Bob", ["MovieB", "MovieC"]),
        3: User(3, "Charlie", ["MovieD"])
    }

    target = test_users[1]
    results = get_similar_users(target, test_users)

    assert len(results) == 1, "Should find exactly 1 similar user"
    assert results[0].username == "Bob", "Similar user should be Bob"
    print("ALL UNIT TESTS PASSED SUCCESSFULLY (100%)")



if __name__ == "__main__":
    test_similarity_logic()