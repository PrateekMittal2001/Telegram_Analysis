import asyncio

from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.channels import GetFullChannelRequest, GetChannelsRequest
from telethon.tl.types import (PeerChannel)
from configuration_data import *
from constants import *

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

    # iterate over the list of channels
    for channel_name in user_channel_list:
        # channel_name = user_channel_list[0]
        if channel_name.isdigit():
            entity = PeerChannel(int(channel_name))
        else:
            entity = channel_name
        try:
            my_channel = await client.get_entity(entity)

            await asyncio.sleep(4)
            channel_data = await client(GetFullChannelRequest(
                channel='my_channel'
            ))

            # print("channel_data", channel_data)
            number_of_participants = channel_data.full_chat.participants_count
            date_of_creation = channel_data.chats[0].date

            channel_data2 = await client(GetChannelsRequest(
                id=[my_channel.id]
            ))

            # print(channel_data2)

            # print the megagroup status
            print("Megagroup:", my_channel.megagroup)

            # print the broadcast status
            print("Broadcast:", my_channel.broadcast)

            # print the gigagroup
            print("Gigagroup:", my_channel.gigagroup)

            # print the channel title
            print("\nchannel name = ", channel_data2.chats[0].title)

            # print the number of users in the channel
            print(f"number of participants = {number_of_participants}")

            # print the date of creation of the channel
            print(f"date of creation = {date_of_creation}")

            # print the chat id of the channel
            print(f"chat id = {my_channel.id}")

            async for dialog in client.iter_dialogs(
                    limit=None,
            ):
                print(f"dialog = {dialog}")
                if dialog.is_channel and dialog in user_channel_list:
                    print("dialoggg:  ", dialog.name)
                    print("Number of peeps: ", dialog.entity.participants_count)

        except Exception as e:
            print("Exception : ", e)
            # store the error in a file errorlog.txt
            with open("errorlog.txt", "a") as f:
                f.write(str(e))
                f.write("\n")


with client:
    client.loop.run_until_complete(main(phone))
