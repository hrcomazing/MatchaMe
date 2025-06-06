# main.py
import sys

try:
    import numpy as np
except ModuleNotFoundError:
    np = None
    print("Numpy is not installed. Continuing without it.")

from matcha_app import MatchaApp


def main():
    """Entry point for the MatchaMe demo script."""
    print("Conda environment is working!")
    print(f"Python executable: {sys.executable}")
    if np is not None:
        print(f"Numpy version: {np.__version__}")
    else:
        print("Numpy not available")

    # Demonstrate basic dating logic
    app = MatchaApp()
    app.register("alice", {"bio": "Loves hiking"})
    app.register("bob", {"bio": "Enjoys cooking"})
    app.register("carol", {"bio": "Reads a lot"})

    app.daily_match()
    print("Daily matches:")
    for u in app.users.values():
        print(f" {u.username} -> {u.current_match}")

    # simulate liking and chatting
    for u in app.users.values():
        if u.current_match:
            app.like_user(u.username, u.current_match)
            app.send_message(u.username, f"Hi {u.current_match}!")

    app.end_of_week()
    print("Chats after end of week:")
    for pair, msgs in app.chats.items():
        print(pair, msgs)


if __name__ == "__main__":
    main()
    print("executed")
