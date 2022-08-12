import asyncio
import re

from telethon.tl.functions.messages import GetFullChatRequest
from telethon.tl.types import PeerChannel

from db_connection import *
from constants import *
from configuration_data import *
from telethon import TelegramClient, events
from telethon.errors import SessionPasswordNeededError

# Create the client and connect
client = TelegramClient(username, api_id, api_hash)

filtered_user_channel_list = []

db = Database(user="root", password="", host="localhost", port=3306, db_name="twitter_bot")


async def main(phone):
    global user_channel
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

    # get full chat messages using getFullChatRequest
    # iterate over the list of channels
    # for channel_name in user_channel_list:
    channel_name = user_channel_list[0]
    if channel_name.isdigit():
        entity = PeerChannel(int(channel_name))
    else:
        entity = channel_name
    try:
        my_channel = await client.get_entity(entity)

        offset_id = 0
        limit = 100
        all_messages = []
        total_messages = 0
        total_count_limit = 0
        list_message = []

        await asyncio.sleep(2)

        full_chat = await client(GetFullChatRequest(
            chat_id=my_channel.id
        ))
        print("Full_chattt = ", full_chat)


    except Exception as e:
        print(e, "Some error occured")
        pass


with client:
    client.loop.run_until_complete(main(phone))
