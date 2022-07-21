import configparser
import asyncio
import telethon.errors
import datetime

from telethon import TelegramClient
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

    # user_input_channel = input('enter entity(telegram URL or entity id):')
    # user_input_channel = 'https://t.me/teleTestingutkarsh'
    # user_channel_list = ["https://t.me/teleTestingutkarsh", "https://t.me/Chad_Crypto", "https://t.me/pj69100x",
    #                    "https://t.me/Chad_Crypto",
    #                   "https://t.me/R1C4RD0S4FUC4LLS", "https://t.me/erics_calls"]
    user_channel_list = ["https://t.me/pj69100x"]

    # iterate over the list of channels
    for channel_name in user_channel_list:
        if channel_name.isdigit():
            entity = PeerChannel(int(channel_name))
        else:
            entity = channel_name

        my_channel = await client.get_entity(entity)

        offset_id = 0
        limit = 100
        all_messages = []
        total_messages = 0
        total_count_limit = 0

        list_message = []

        # date_of_post = datetime.datetime(2022, 6, 12, 0, 0, 0)

        # start_time = datetime.datetime(2022, 1, 1, 0, 0, 0)
        # end_time = datetime.datetime(2022, 2, 1, 0, 0, 0)
        # full_msg_list = client.get_messages(my_channel, limit=200, offset_id=200)
        # next_200_list = client.get_messages(my_channel, limit=200, offset_id=full_msg_list[-1].id)
        # print(next_200_list)

        while True:
            # print("Current Offset ID is:", offset_id, "; Total Messages:", total_messages)
            history = await client(GetHistoryRequest(
                peer=my_channel,
                offset_id=offset_id,
                offset_date=None,
                # offset_date= date_of_post,
                add_offset=0,
                limit=limit,
                max_id=0,
                min_id=0,
                hash=0
            ))
            if not history.messages:
                break
            messages = history.messages
            for message in messages:
                all_messages.append(message.to_dict())
                # print only the message content
                # print(message.date, message.message)
                list_message.append([message.message, message.date])
            offset_id = messages[len(messages) - 1].id
            total_messages = len(all_messages)
            # print messages from the dictionary all_messages
            if total_count_limit != 0 and total_messages >= total_count_limit:
                break

        # print(list_message[0])
        # print(list_message[-1])
        # print(list_message[-2])
        # print(list_message[-3])
        print(list_message)
        print(len(list_message))


with client:
    client.loop.run_until_complete(main(phone))
