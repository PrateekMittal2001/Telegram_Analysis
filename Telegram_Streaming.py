import re
import db_connection as db
import asyncio
from constants import *
from configuration_data import *
from telethon import TelegramClient, events
from telethon.errors import SessionPasswordNeededError, FloodWaitError
from telethon.tl.functions.channels import JoinChannelRequest

# Create the client and connect
client = TelegramClient(username, api_id, api_hash)

filtered_user_channel_list = []
token_symbol = "$"

db = db.Database(user="root", password="", host="localhost", port=3306, db_name="twitter_bot")


# filter the channel list to get the unique user channels
def get_unique_channels(channel_list):
    channel_list = set(channel_list)
    channel_list = list(channel_list)
    return channel_list


user_channel_list = get_unique_channels(user_channel_list)

filename = "channels.csv"


# def non_joined_channels(channel_list):
#     #open file in read write mode
#     with open (filename, 'r+') as f:
#         reader = csv.reader(f)
#         data = list(reader)
#         print(data)
#         for channel in channel_list:
#             if channel


# non_joined_channels(user_channel_list)


async def join_channel(channel_list):
    for channel in channel_list:
        try:
            client.flood_sleep_threshold = 0  # Don't auto-sleep
            await client(JoinChannelRequest(channel))
            print("We fucking joined : ", channel)
            await asyncio.sleep(delay=4)
        except FloodWaitError as fwe:
            print(f'Waiting for {fwe}')
            await asyncio.sleep(delay=fwe.seconds)


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
        if not message.isdigit():
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
    # Firstly join the channels for streaming
    # await join_channel(user_channel_list)
    # Ensure you're authorized
    if not await client.is_user_authorized():
        await client.send_code_request(phone)
        try:
            await client.sign_in(phone, input('Enter the code: '))
        except SessionPasswordNeededError:
            await client.sign_in(password=input('Password: '))

    me = await client.get_me()

    # use telethon.events.newmessage.NewMessage to stream the new messages
    try:
        @client.on(events.NewMessage(chats=filtered_user_channel_list, incoming=True))
        # @client.on(events.NewMessage(incoming=True))
        async def handler(event):
            print(event)
            textty = event.text
            print("Message = ", textty)
            # print the channel name and the message
            print("channel id = ", event.chat_id)
            # using the chat_id print the channel name
            print(event.message.date)
            token = filter_token_from_message(textty)
            print("token = ", token, " Token ended")
            links = filter_links_from_message(textty)
            print("links = ", links, " Links ended")
            dexlink = weblink = telelink = tweetlink = "Not Found"
            if len(links) != 0:
                for link in links:
                    if "twitter" in link:
                        tweetlink = link
                    elif 'dextools' in link or 'dextools' in link:
                        dexlink = link
                        print("dexlink = ", dexlink)
                    elif 't.me' in link:
                        telelink = link
                        print("telelink = ", telelink)
                    elif '.com' in link:
                        weblink = link
                        print("websitelink = ", weblink)
                a = INSERT_COIN_DATA_TO_TABLE.format(
                    token=token,
                    dexlink=dexlink,
                    telelink=telelink,
                    weblink=weblink,
                    twitterlink=tweetlink
                )
                # db.execute_query(a)
                print("Data inserted")
            else:
                print("No link found in the message")
            # print the message is not text
            if len(textty) == 0:
                print("Ye non text hai, chup chaap text bhejo")
            print("\n")

        await client.run_until_disconnected()

    except Exception as e:
        print(e, "Some error occured")
        pass


# client.start()
# client.run_until_disconnected(main(phone))

with client:
    client.loop.run_until_complete(main(phone))
