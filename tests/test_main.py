import unittest
from code.matcha_app import MatchaApp

class TestMatchaApp(unittest.TestCase):
    def setUp(self):
        """Set up a fresh instance of MatchaApp for each test."""
        self.app = MatchaApp()
        self.app.register("alice", {"bio": "Loves hiking"})
        self.app.register("bob", {"bio": "Enjoys cooking"})
        self.app.register("carol", {"bio": "Reads a lot"})

    def test_daily_match(self):
        """Test daily matching functionality."""
        self.app.daily_match()
        users = self.app.users
        for user in users.values():
            self.assertIsNotNone(user.current_match, f"{user.username} should have a match.")
            self.assertIn(user.current_match, users, f"{user.username}'s match should be a registered user.")

    def test_like_user(self):
        """Test liking a user."""
        self.app.daily_match()
        alice_match = self.app.users["alice"].current_match
        self.assertIsNotNone(alice_match, "Alice should have a match before liking.")
        self.app.like_user("alice", alice_match)
        self.assertIn(alice_match, self.app.users["alice"].liked_users, "Alice should have liked her match.")

    def test_send_message(self):
        """Test sending a message."""
        self.app.daily_match()
        alice_match = self.app.users["alice"].current_match
        self.assertIsNotNone(alice_match, "Alice should have a match before sending a message.")
        self.app.send_message("alice", f"Hi {alice_match}!")
        chat_key = tuple(sorted(["alice", alice_match]))
        self.assertIn(chat_key, self.app.chats, "Chat should exist between Alice and her match.")
        self.assertIn(f"Hi {alice_match}!", self.app.chats[chat_key], "Message should be in the chat.")

    def test_end_of_week(self):
        """Test end-of-week functionality."""
        self.app.daily_match()
        for user in self.app.users.values():
            if user.current_match:
                self.app.like_user(user.username, user.current_match)
                self.app.send_message(user.username, f"Hi {user.current_match}!")
        self.app.end_of_week()
        for pair, msgs in self.app.chats.items():
            self.assertTrue(len(msgs) > 0, f"Chat {pair} should persist if both users liked each other.")

if __name__ == '__main__':
    unittest.main()