import asyncio
from aiohttp import ClientSession
from AnonX.core.bot import AnonXBot
from AnonX.core.dir import dirr
from AnonX.core.git import git
from AnonX.core.userbot import Userbot
from AnonX.misc import dbb, heroku, sudo
from AnonX.platforms import YouTubeAPI, CarbonAPI, SpotifyAPI, AppleAPI, RessoAPI, SoundAPI, TeleAPI

dirr()
git()
dbb()
heroku()
sudo()

aiohttpsession = None

async def init_aiohttp_session():
    global aiohttpsession
    if aiohttpsession is None:
        aiohttpsession = ClientSession()

async def main():
    await init_aiohttp_session()
    app = AnonXBot()
    await app.start()
    userbot = Userbot()
    await userbot.start()

if name == "main":
    asyncio.run(main())