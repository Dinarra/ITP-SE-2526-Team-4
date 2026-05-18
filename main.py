from data_manager import load_data, save_new_history
from engine import get_similar_users, generate_recommendations


def main():
    try:
        print("=== WELCOME TO TEAM 4 ENTERTAINMENT HUB ===")
        users_dict, movies_list = load_data()

        print("\n[Database Status] Loaded profiles:")
        for u_id, user in users_dict.items():
            print(f" ID {u_id}: {user.get_role_profile()} | History size: {len(user.watched_history)}")

        print("\nAvailable movies catalog details:")
        for m in movies_list:
            print(f" -> {m.get_details()}")

        user_input = input("\nEnter User ID to run analytics (1-4): ")
        target_id = int(user_input)

        if target_id not in users_dict:
            print("Target error: User ID does not exist.")
            return

        target_user = users_dict[target_id]
        print(f"\nActive profile: {target_user.username}")
        print(f"Watched list: {list(target_user.watched_history)}")

        similar_peers = get_similar_users(target_user, users_dict)
        print(f"Found {len(similar_peers)} peer profiles with overlapping interests.")

        print("\n--- Running AI Recommendation Generator ---")
        recs = list(generate_recommendations(target_user, similar_peers))

        if recs:
            for item in recs:
                print(f"🔥 Recommended Discovery: {item}")

            save_choice = input(
                "\nWould you like to auto-save the first recommendation to database history? (yes/no): ")
            if save_choice.lower() == 'yes':
                save_new_history(target_id, recs[0])
                print("Database successfully updated on disk!")
        else:
            print("No new unique content left to recommend from similar peers.")

    except ValueError:
        print("Input Exception: Numerical argument execution aborted.")
    except Exception as e:
        print(f"Runtime execution failure: {e}")


if name == "main":
    main()
