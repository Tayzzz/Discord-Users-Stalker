try:
    import discord
    import colorama
except ModuleNotFoundError as e:
    modulename = str(e).split("No module named ")[1].replace("'", "")
    input(f"Please install module with: pip install {modulename}")
    exit()

from discord import Client
from colorama import Fore, init
import json
from datetime import datetime

init(convert=True)
client = Client()
config = json.load(open("config.json", encoding="utf-8"))


@client.event
async def on_ready():
    pass


@client.event
async def on_message(ctx):

    date = datetime.now().strftime("%H:%M:%S")

    for trackerID in config["usersID"]:
        if str(ctx.author.id) == str(trackerID):

            if len(ctx.content) == 0 and ctx.attachments:
                msg = "an attachment"
            elif ctx.content and not ctx.attachments:
                msg = ctx.content
            elif ctx.content and ctx.attachments:
                msg = ctx.content + " " + "with an attachment"

            print(f"""[{date}] {Fore.GREEN}Message Sent{Fore.RESET}\n> Auhtor  - {ctx.author}\n> ID      - {ctx.author.id}\n> Server  - {ctx.guild}\n> Channel - #{ctx.channel}\n> Content - {msg}\n""")


@client.event
async def on_message_delete(ctx):

    date = datetime.now().strftime("%H:%M:%S")

    if len(ctx.content) == 0 and ctx.attachments:
        msg = "an attachment"
    elif ctx.content and not ctx.attachments:
        msg = ctx.content
    elif ctx.content and ctx.attachments:
        msg = ctx.content + " " + "with an attachment"

    for trackerID in config["usersID"]:
        if str(ctx.author.id) == str(trackerID):
            print(f"""[{date}] {Fore.RED}Message Deleted{Fore.RESET}\n> Auhtor  - {ctx.author}\n> ID      - {ctx.author.id}\n> Server  - {ctx.guild}\n> Channel - #{ctx.channel}\n> Content - {ctx.content}\n""")


@client.event
async def on_message_edit(oldctx, newctx):

    date = datetime.now().strftime("%H:%M:%S")

    for trackerID in config["usersID"]:
        if str(newctx.author.id) == str(trackerID):
            print(f"""[{date}] {Fore.YELLOW}Message Edited{Fore.RESET}\n> Auhtor  - {newctx.author}\n> ID      - {newctx.author.id}\n> Server  - {newctx.guild}\n> Channel - #{newctx.channel}\n> Old content - {oldctx.content}\n> New content - {newctx.content}\n""")


@client.event
async def on_reaction_add(reaction, user):

    date = datetime.now().strftime("%H:%M:%S")

    for trackerID in config["usersID"]:
        if str(user.id) == str(trackerID):
            print(f"""[{date}] Reaction Add\n> Auhtor  - {user}\n> ID      - {user.id}\n> Server  - {reaction.message.guild}\n> Channel - #{reaction.message.channel}\n> Message - {reaction.message.content} sent by {reaction.message.author}\n""")

if __name__ == "__main__":
    client.run(config["token"], bot=False)
