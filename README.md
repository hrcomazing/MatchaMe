# MatchaMe

A modular Python project built to run and orchestrate different components — from Python scripts to shell commands, Node.js, and more. MatchaMe is environment-managed with Conda for reproducibility and portability.

---

## Overview

MatchaMe started as a simple environment template and now contains a minimal prototype of a dating app.  The logic lives in `matcha_app.py` and demonstrates how daily matching and weekly roster checks can work.

Core ideas implemented:
- The AI agent pairs available users once per day.
- Each match lasts for a week of chatting.
- During that week you can add your partner to a three-person "roster" of favorites.
- If both people still have each other on their roster at week's end, the chat persists; otherwise it is removed.

While not a production web service, this code offers a starting point for experimenting with the matchmaking rules.

---

## Setup

### 1. Clone the Repository

git clone https://github.com/yourusername/MatchaMe.git
cd MatchaMe

---

### 2. Set Up the Conda Environment

conda env create -f environment.yml
conda activate matchame-env

## Usage
Run the demo either with a direct path or as a module:

```bash
python code/main.py
# or
python -m code.main
```

The `code` directory is now a package, so module-style execution works as well.

## Environment

All dependencies are managed via Conda. To export or update the environment:
conda env export --no-builds > environment.yml
