from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from constants import *
from configuration_data import *
from db_connection import *

# Create the client and connect
client = TelegramClient(username, api_id, api_hash)

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

    try:
        # get the links from the database
        link_in_database = db.fetchall(GET_JOINING_LINKS)
        link_in_database = [x[0] for x in link_in_database]
        print(link_in_database, "link in database\n")
        for link in user_channel_list:
            if link in link_in_database:
                print(link, "is in the database")
            else:
                print(link, "is not in the database")
                # insert the link and joining_status as joined in the database
                db.execute_query(INSERT_LINK_TO_TABLE.format(joining_link=link, joining_status='not_joined'))
                db.commit()
                print(link, "is inserted to database")

    except Exception as e:
        print("There some error occured", e)
        pass



with client:
    client.loop.run_until_complete(main(phone))