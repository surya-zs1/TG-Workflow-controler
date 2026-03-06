import os

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from database import add_account,get_account,add_repo,get_repo,add_workflow,get_workflows
from github_api import start_workflow,list_runs,cancel_run


TOKEN=os.environ["BOT_TOKEN"]


async def start(update:Update,context:ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
"""
GitHub Controller

/add_account name token
/add_repo account user/repo
/add_workflow repo workflow.yml

/run repo workflow.yml

/runs repo
/cancel repo run_id
"""
)


async def add_account_cmd(update,context):

    name=context.args[0]
    token=context.args[1]

    await add_account(name,token)

    await update.message.reply_text("Account added")


async def add_repo_cmd(update,context):

    account=context.args[0]
    repo=context.args[1]

    await add_repo(account,repo)

    await update.message.reply_text("Repo added")


async def add_workflow_cmd(update,context):

    repo=context.args[0]
    workflow=context.args[1]

    await add_workflow(repo,workflow)

    await update.message.reply_text("Workflow saved")


async def run_cmd(update,context):

    repo=context.args[0]
    workflow=context.args[1]

    repo_data=await get_repo(repo)

    acc=await get_account(repo_data["account"])

    code=start_workflow(acc["token"],repo,workflow)

    if code==204:

        await update.message.reply_text("Workflow started")

    else:

        await update.message.reply_text("Failed")


async def runs_cmd(update,context):

    repo=context.args[0]

    repo_data=await get_repo(repo)

    acc=await get_account(repo_data["account"])

    data=list_runs(acc["token"],repo)

    text=""

    for r in data["workflow_runs"][:5]:

        text+=f"""
ID: {r['id']}
Name: {r['name']}
Status: {r['status']}
"""

    await update.message.reply_text(text)


async def cancel_cmd(update,context):

    repo=context.args[0]
    run_id=context.args[1]

    repo_data=await get_repo(repo)

    acc=await get_account(repo_data["account"])

    code=cancel_run(acc["token"],repo,run_id)

    if code==202:

        await update.message.reply_text("Cancelled")

    else:

        await update.message.reply_text("Failed")


app=ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start",start))
app.add_handler(CommandHandler("add_account",add_account_cmd))
app.add_handler(CommandHandler("add_repo",add_repo_cmd))
app.add_handler(CommandHandler("add_workflow",add_workflow_cmd))
app.add_handler(CommandHandler("run",run_cmd))
app.add_handler(CommandHandler("runs",runs_cmd))
app.add_handler(CommandHandler("cancel",cancel_cmd))

app.run_polling()
