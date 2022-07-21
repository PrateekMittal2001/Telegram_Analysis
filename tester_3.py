import asyncio
from telethon import events
import configparser
import datetime
import asyncio
from telethon import TelegramClient, events

from telethon import TelegramClient
from telethon.tl.functions.messages import SearchRequest
from telethon.tl.types import InputMessagesFilterEmpty
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.messages import (GetHistoryRequest)
from telethon.tl.types import (
    PeerChannel
)

# Reading Configs
config = configparser.ConfigParser()
config.read("configPrateek.ini")

# Setting configuration values
api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']

api_hash = str(api_hash)

phone = config['Telegram']['phone']
username = config['Telegram']['username']

# Create the client and connect
client = TelegramClient(username, api_id, api_hash)

await client.start()
print("Client Created")
# Ensure you're authorized
if not await client.is_user_authorized():
    await client.send_code_request(phone)
    try:
        await client.sign_in(phone, input('Enter the code: '))
    except SessionPasswordNeededError:
        await client.sign_in(password=input('Password: '))

me = await client.get_me()


@client.on(events.NewMessage(pattern='(?i)hello.+'))
async def handler(event):
    # Respond whenever someone says "Hello" and something else
    await event.reply('Hey!')


@client.on(events.NewMessage(outgoing=True, pattern='!ping'))
async def handler(event):
    # Say "!pong" whenever you send "!ping", then delete both messages
    m = await event.respond('!pong')
    await asyncio.sleep(5)
    await client.delete_messages(event.chat_id, [event.id, m.id])
