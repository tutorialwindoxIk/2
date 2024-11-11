from AnonX.core.bot import AnonXBot
from AnonX.core.dir import dirr
from AnonX.core.git import git
from AnonX.core.userbot import Userbot
from AnonX.misc import dbb, heroku, sudo
from aiohttp import ClientSession

from .logging import LOGGER

# Directories
dirr()

# Check Git Updates
git()

# Initialize Memory DB
dbb()

# Heroku APP
heroku()

# Load Sudo Users from DB
sudo()

# Bot Client
app = AnonXBot()

# Assistant Client
userbot = Userbot()

from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()

aiohttpsession = ClientSession()
import asyncio
from aiohttp import ClientSession

# Async function jo ClientSession ko initialize karega
async def create_session():
    global aiohttpsession
    aiohttpsession = ClientSession()

# Async function ko run karne ke liye asyncio.run() ka use karenge
asyncio.run(create_session())
import asyncio
from aiohttp import ClientSession

# Global variable to store the aiohttp session
aiohttpsession = None

# Async function jo ClientSession ko initialize karega
async def create_session():
    global aiohttpsession
    aiohttpsession = ClientSession()

# Code ko async environment mein run karne ke liye isko wrap karte hain
def initialize_session():
    asyncio.run(create_session())

# Ab initialize_session ko call karke session start kar sakte hain
initialize_session()