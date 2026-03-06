# TG-Workflow-controller

A Telegram bot for controlling GitHub Actions workflows across multiple accounts.

## Architecture
```
Telegram Bot
     │
     ▼
Bot Backend (Python)
     │
     ├── MongoDB (accounts + workflows)
     │
     └── GitHub API
            │
            ▼
GitHub Actions
```

# MongoDB collections
**accounts**
```json
{
  "name": "main_account",
  "token": "github_pat_xxx"
}
```
**repos**
```json
{
  "account": "main_account",
  "repo": "user/repository"
}
```
**workflows**
```json
{
  "repo": "user/repository",
  "workflow": "build.yml"
}
```
# Project structure
```
telegram-github-controller/
│
├── bot.py
├── github_api.py
├── database.py
├── requirements.txt
├── Dockerfile
└── start.sh
```
# Environment variables

BOT_TOKEN=telegram_bot_token
MONGO_URL=mongodb_connection_string

# Example usage in Telegram

**Add github account :**

/add_account main ghp_xxxxx

**Add repo :**

/add_repo main user/repository

**Add workflow :**
```json
/add_workflow user/repository build.yml

**run workflow :**

/run user/repository build.yml

**views runs :**

/runs user/repository

**cancel runs :**

/cancel user/repository 123456789

# Results 

Your Telegram bot becomes a multi-account GitHub CI controller.

Supports:

unlimited GitHub accounts

unlimited repositories

unlimited workflows

run / cancel / view runs

All stored safely in MongoDB.

# Made by Surya..!!!
