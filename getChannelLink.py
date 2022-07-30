import re

import db_connection as db
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError

from configuration_data import *
from constants import *

# api_id and api_hash

# Create the client and connect
client = TelegramClient(username, api_id, api_hash)
search_matrix = ["https://t.me/", "https://telegram.me/"]
links = []

db = db.Database(user="root", password="", host="localhost", port=3306, db_name="twitter_bot")


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
    # print(me)

    list_message = []

    try:
        async for message in client.iter_messages(1055173630):
            # print(message.text)
            # if the message contains https://t.me/ or https://telegram.me/ copy the message and save it in list
            # list_message
            if message.text is not None:
                for ele in search_matrix:
                    if ele in message.text:
                        list_message.append(message.text)
                        # print(message.text)
                        regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
                        url = re.findall(regex, message.text)
                        # print(url)
                        links.append(url[0][0])
                        print([x[0] for x in url])
                #         a = list(itertools.chain(*url))
        print(links, "links ended\n")
        # get the links from the database
        link_in_database = db.fetchall(GET_JOINING_LINKS)
        print(link_in_database, "link in database\n")
        for link in links:
            if link in search_matrix:
                print(link, "this is link")
                if link in link_in_database:
                    print(link, "is in the database")
                else:
                    print(link, "is not in the database")
                    b = INSERT_LINK_TO_TABLE.format(joining_link=link, joining_status="not_joined")
                    db.execute_query(b)
                    print(link, "is inserted to database")


    except Exception as e:
        print(e, "Some error occured")

    # print(*list_message, sep="\t message ends \n", end=" streaming ended")


with client:
    client.loop.run_until_complete(main(phone))
