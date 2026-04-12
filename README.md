# MatchaMe

A modular Python project built to run and orchestrate different components — from Python scripts to shell commands, Node.js, and more. MatchaMe is environment-managed with Conda for reproducibility and portability.

---

## Overview

MatchaMe contains a prototype of a dating app demonstrating automated matchmaking and engagement logic. The core logic resides in `code/matcha_app.py`.

Core ideas implemented:
- **Daily Matching**: The AI agent pairs available users once per day.
- **Weekly Engagement**: Each match lasts for one week of chatting.
- **The Roster**: During the match week, users can add their partner to a "roster" of up to three favorites.
- **Persistence**: If both users have each other on their roster at the end of the week, the chat persists; otherwise, the match expires.

While not a production web service, this code offers a starting point for experimenting with automated matchmaking rules and engagement mechanics.

---

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/MatchaMe.git
cd MatchaMe
```

---

### 2. Set Up the Conda Environment

```bash
conda env create -f environment.yml
conda activate matchame-env
```

## Usage

Run the demo from the `code` directory:

```bash
python code/main.py
```

You can also run the test suite:

```bash
python -m unittest discover tests
```

## Environment

All dependencies are managed via Conda. To export or update the environment:

```bash
conda env export --no-builds > environment.yml
```
