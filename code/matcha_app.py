"""Simple dating app logic for MatchaMe."""

import random
import datetime
from collections import defaultdict

class User:
    def __init__(self, username, profile):
        self.username = username
        self.profile = profile
        self.roster = set()  # usernames this user likes
        self.inbox = defaultdict(list)  # chat history keyed by partner username
        self.current_match = None
        self.last_matched = None

    def like(self, username):
        """Add a username to the roster if space is available."""
        if len(self.roster) >= 3:
            raise ValueError("Roster full (max 3)")
        self.roster.add(username)

    def unlike(self, username):
        self.roster.discard(username)

class MatchaApp:
    def __init__(self):
        self.users = {}
        self.chats = defaultdict(list)  # (user1,user2) -> messages
        self.day = 0

    def register(self, username, profile):
        if username in self.users:
            raise ValueError("Username taken")
        self.users[username] = User(username, profile)

    def like_user(self, liker, liked):
        """Current user expresses interest in another user."""
        if liker not in self.users or liked not in self.users:
            raise ValueError("Unknown user")
        self.users[liker].like(liked)

    def daily_match(self):
        """Pair users randomly each day if they don't have a current match."""
        available = [u for u in self.users.values() if u.current_match is None]
        random.shuffle(available)
        for i in range(0, len(available), 2):
            if i+1 < len(available):
                u1 = available[i]
                u2 = available[i+1]
                u1.current_match = u2.username
                u2.current_match = u1.username
                u1.last_matched = self.day
                u2.last_matched = self.day

    def send_message(self, sender, text):
        user = self.users[sender]
        partner_name = user.current_match
        if partner_name is None:
            raise ValueError("No active match")
        partner = self.users[partner_name]
        self.chats[tuple(sorted([sender, partner_name]))].append((sender, text))
        user.inbox[partner_name].append((sender, text))
        partner.inbox[sender].append((sender, text))

    def end_of_week(self):
        """Evaluate rosters and expire unmatched chats."""
        for u in self.users.values():
            partner_name = u.current_match
            if partner_name is None:
                continue
            partner = self.users[partner_name]
            if (partner.username in u.roster and u.username in partner.roster):
                # keep chatting
                u.current_match = partner.username
                partner.current_match = u.username
            else:
                # end chat
                u.current_match = None
                partner.current_match = None
                self.chats.pop(tuple(sorted([u.username, partner.username])), None)
        self.day += 7

