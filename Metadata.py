import asyncio
import requests as requests
import time

from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.channels import GetFullChannelRequest, GetChannelsRequest
from telethon.tl.types import (PeerChannel)
from configuration_data import *
from constants import *
from db_connection import *

# Create the client and connect
client = TelegramClient(username, api_id, api_hash)

db = Database(user="root", password="", host="localhost", port=3306, db_name="twitter_bot")


def get_number_of_subscribers(channel):
    channel_name = channel.split('/')
    channel_name = channel_name[-1]
    # sleep for 2 seconds
    time.sleep(2)
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/getChatMemberCount?chat_id=@{channel_name}"
    response = requests.get(url=url).json()
    print(response)
    while True:
        if response['ok']:
            print(f"INFO: Member count of channel {channel_name} is {response['result']}")
            break
        elif response['error_code'] == 400:
            print(f"ERROR: Channel not found for {channel_name}")
            break
        elif response['error_code'] == 429:
            print(f"ERROR: {response['description']}")
            break
        else:
            print(f"ERROR: {response['description']}")
            break

    return response['result']


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

    # iterate over the list of channels
    for channel_name in deployed_channels:
        # channel_name = user_channel_list[0]
        if channel_name.isdigit():
            entity = PeerChannel(int(channel_name))
        else:
            entity = channel_name
        try:
            my_channel = await client.get_entity(entity)

            channel_data = await client(GetFullChannelRequest(
                channel='my_channel'
            ))

            channel_data2 = await client(GetChannelsRequest(
                id=[my_channel.id]
            ))

            print("channel_data1: ", channel_data)
            print("channel_data2: ", channel_data2)

            # print the megagroup status
            print("Megagroup:", my_channel.megagroup)
            # print the broadcast status
            print("Broadcast:", my_channel.broadcast)
            # print the gigagroup
            print("Gigagroup:", my_channel.gigagroup)

            channel_status = 0
            if my_channel.megagroup:
                channel_status = "Group"
            elif my_channel.broadcast:
                channel_status = "Channel"

            # print the channel title
            print("channel name = ", channel_data2.chats[0].title)
            # print the date of creation of the channel
            date_of_creation = channel_data.chats[0].date
            print(f"date of creation = {date_of_creation}")
            # print the chat id of the channel
            print(f"chat id = {my_channel.id}\n")

            # print the number of participants in the channel
            number_of_participants = get_number_of_subscribers(channel_name)
            print(f"number of participants = {number_of_participants}")

            if number_of_participants > 0:
                # enter the channel and get the member count to the database metadata
                ENTER_CHANNEL_SUBSCRIBERS_COUNT = "INSERT INTO metadata (channel_name, number_of_subscribers, channel_or_group, time_updated) VALUES ('{channel_name}', '{number_of_subscribers}', '{channel_or_group}', '{time_updated}')"
                db.execute_query(ENTER_CHANNEL_SUBSCRIBERS_COUNT.format(channel_name=channel_name,
                                                                        number_of_subscribers=number_of_participants,
                                                                        channel_or_group=channel_status,
                                                                        time_updated=date_of_creation))
                print(f"INFO: Member count of channel {channel_name} is {number_of_participants} and is added to the database.")

            else:
                ENTER_CHANNEL_SUBSCRIBERS_COUNT = "INSERT INTO metadata (channel_name, number_of_subscribers, channel_or_group, time_updated) VALUES ('{channel_name}', '{number_of_subscribers}', '{channel_or_group}', '{time_updated}');"
                db.execute_query(ENTER_CHANNEL_SUBSCRIBERS_COUNT.format(channel_name=channel_name,
                                                                        number_of_subscribers=number_of_participants,
                                                                        channel_or_group=channel_status,
                                                                        time_updated=date_of_creation))
            print(f"INFO: Member count of channel {channel_name} is {number_of_participants} and is NOT added to the database.")

            # sleep for 4 seconds
            time.sleep(4)

        except Exception as e:
            print("Exception : ", e)
            # store the error in a file errorlog.txt
            with open("errorlog.txt", "a") as f:
                f.write(str(e))
                f.write("\n")


with client:
    client.loop.run_until_complete(main(phone))
