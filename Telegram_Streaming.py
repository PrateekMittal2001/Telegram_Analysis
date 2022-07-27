import re
import db_connection
import asyncio
from constants import *
from config import *
from telethon import TelegramClient, events
from telethon.errors import SessionPasswordNeededError, FloodWaitError
from telethon.tl.functions.channels import JoinChannelRequest

# Create the client and connect
client = TelegramClient(username, api_id, api_hash)

filtered_user_channel_list = []
token_symbol = "$"

db = db_connection.db_connection(user=user, password=password, host=host, port=port, db_name=db_name)

# join channel function
async def join_channel(channel_list):
    for channel in channel_list:
        try:
            await client(JoinChannelRequest(channel))
        except FloodWaitError as fwe:
            print(f'Waiting for {fwe}')
            await asyncio.sleep(delay=fwe.seconds)


# join_channel(user_channel_list)


# function to filter the user_channel_list
def filter_user_channel_list(user_channel_list):
    list_sliced = []
    for i in user_channel_list:
        # split the names using /
        sliced = i.split("/")
        sliced = "@" + sliced[-1]
        list_sliced.append(sliced)
    set_sliced = set(list_sliced)
    list_sliced = list(set_sliced)
    return list_sliced


filtered_user_channel_list = filter_user_channel_list(user_channel_list)


def filter_token_from_message(message):
    if token_symbol in message:
        message = message.split(token_symbol)
        message = message[1]
        message = message.split(" ")
        message = message[0]
        message = "$" + message
        return message


def filter_links_from_message(message):
    # data = re.compile('(?:(?:https?|ftp):\/\/)[\w/\-?=%.]+\.[\w/\-&?=%.]+')
    # print("message = ", message)
    data = re.compile('(?:(?:https?|ftp):\/\/)[\w/\-?=%.]+\.[\w/\-&?=%.]+')
    new = data.findall(message)
    return new


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

    # use telethon.events.newmessage.NewMessage to stream the new messages
    # @client.on(events.NewMessage(chats="@teleTestingutkarsh", incoming=True, from_users= [@teleTestingutkarsh", "https://t.me/Chad_Crypto", "https://t.me/pj69100x"))
    try:
        @client.on(events.NewMessage(chats=filtered_user_channel_list, incoming=True))
        # @client.on(events.NewMessage(incoming=True))
        async def handler(event):
            textty = event.text
            print(event.message.date)
            token = filter_token_from_message(textty)
            print("token = ", token, " Token ended")
            links = filter_links_from_message(textty)
            print("links = ", links, " Links ended")
            print(event.message.sender_id)
            # print the utf id of text
            if len(textty) == 0:
                print("Ye non text hai, zyada aesthetic ke chode mat bano, chup chaap text bhejo")
            print("\n")
            # await asyncio.sleep(1)

            # call the event handler to stream the new messages

        await client.run_until_disconnected()

    except Exception as e:
        print(e, "Some error occured")
        pass


# client.start()
# client.run_until_disconnected(main(phone))

with client:
    client.loop.run_until_complete(main(phone))
