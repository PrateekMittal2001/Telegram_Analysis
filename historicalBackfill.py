import asyncio

from db_connection import *
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.messages import (GetHistoryRequest)
from telethon.tl.types import (PeerChannel)
from configuration_data import *
from constants import *

# Create the client and connect
client = TelegramClient(username, api_id, api_hash)

db = Database(user="root", password="", host="localhost", port=3306, db_name="twitter_bot")

"""# CODE TO ENTER THE DATA INTO DATABASE


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

        while True:
            try:
                history = await client(GetHistoryRequest(
                    peer=my_channel,
                    offset_id=offset_id,
                    offset_date=None,
                    add_offset=0,
                    limit=limit,
                    max_id=0,
                    min_id=0,
                    hash=0
                ))
            except Exception as e:
                print("Error:", e)
            if not history.messages:
                break
            messages = history.messages
            for message in messages:
                all_messages.append(message.to_dict())
                list_message.append([message.message, message.date, message.id, my_channel.id])
            offset_id = messages[len(messages) - 1].id
            total_messages = len(all_messages)
            if total_count_limit != 0 and total_messages >= total_count_limit:
                break

        for message in list_message:
            print(f"message: {message}\n")

        # enter the message id, message date and message to the database historical_data
        # for message in list_message:
        for message in range(len(list_message) - 1, 0, -1):
            ENTER_ID_DATE_MESSAGE_TO_DATABASE = "INSERT INTO historical_data (Message, message_id, date_of_message, channel_id) VALUES ('{message}', '{idd}', '{dates}' , '{ch_id}')"
            db.execute_query(ENTER_ID_DATE_MESSAGE_TO_DATABASE.format(message=list_message[message][0], idd=list_message[message][2], dates=list_message[message][1], ch_id=list_message[message][3]))
            print("Message inserted")

    except Exception as e:
        print("Exception : ", e)
        # store the error in a file errorlog.txt
        with open("errorlog.txt", "a") as f:
            f.write(str(e))
            f.write("\n")
"""


async def main(phone):
    """
    To enter backfill data to the database
    :param phone:
    :return:
    """
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
    # for channel_name in user_channel_list:
    channel_name = user_channel_list[0]
    if channel_name.isdigit():
        entity = PeerChannel(int(channel_name))
    else:
        entity = channel_name
    try:
        my_channel = await client.get_entity(entity)

        # get the last message id and not none value from the database historical_data
        GET_FIRST_MESSAGE_ID = "SELECT message_id FROM historical_data WHERE message_id != 'None' ORDER BY message_id DESC LIMIT 1"
        last_message_id = db.fetchall(GET_FIRST_MESSAGE_ID)
        last_message_id = last_message_id[0][0]
        print(f"last_message_id: {last_message_id}")

        offset_id = 0
        limit = 100
        all_messages = []
        total_messages = 0
        total_count_limit = 0
        list_message = []

        # await asyncio.sleep(2)

        while True:
            try:
                history = await client(GetHistoryRequest(
                    peer=my_channel,
                    offset_id=offset_id,
                    offset_date=None,
                    add_offset=0,
                    limit=limit,
                    max_id=0,
                    min_id=last_message_id,
                    hash=0
                ))
            except Exception as e:
                print("Error:", e)
            if not history.messages:
                break
            messages = history.messages
            for message in messages:
                all_messages.append(message.to_dict())
                list_message.append([message.message, message.date, message.id, my_channel.id])
            offset_id = messages[len(messages) - 1].id
            total_messages = len(all_messages)
            if total_count_limit != 0 and total_messages >= total_count_limit:
                break

        for message in list_message:
            print(f"message: {message}\n")
        # print(list_message)

        # print the messages after the last message id
        # print(list_message[0][2])
        # if last_message_id == list_message[0][2]:
        #     print("No new messages")
        # else:
        #     for message in list_message:
        #         if message[2] > last_message_id:
        #             print(f"message: {message}\n")
        #             # enter the message id, message date and message to the database historical_data
        #             ENTER_ID_DATE_MESSAGE_TO_DATABASE = "INSERT INTO historical_data (Message, message_id, date_of_message, channel_id) VALUES ('{message}', '{idd}', '{dates}' , '{ch_id}')"
        #             db.execute_query(ENTER_ID_DATE_MESSAGE_TO_DATABASE.format(message=message[0], idd=message[2], dates=message[1], ch_id=message[3]))
        #             print("Message inserted")

    except Exception as e:
        print("Exception : ", e)
        # store the error in a file errorlog.txt
        with open("errorlog.txt", "a") as f:
            f.write(str(e))
            f.write("\n")


with client:
    client.loop.run_until_complete(main(phone))
