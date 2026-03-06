import os
from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient(os.environ["MONGO_URL"])

db = client.github_controller

accounts = db.accounts
repos = db.repos
workflows = db.workflows


async def add_account(name, token):

    await accounts.insert_one({
        "name": name,
        "token": token
    })


async def get_account(name):

    return await accounts.find_one({"name": name})


async def add_repo(account, repo):

    await repos.insert_one({
        "account": account,
        "repo": repo
    })


async def get_repo(repo):

    return await repos.find_one({"repo": repo})


async def add_workflow(repo, workflow):

    await workflows.insert_one({
        "repo": repo,
        "workflow": workflow
    })


async def get_workflows(repo):

    cursor = workflows.find({"repo": repo})

    return await cursor.to_list(length=50)
