import asyncio

from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.channels import GetFullChannelRequest, GetChannelsRequest
from telethon.tl.functions.messages import (GetHistoryRequest)
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
                    list_message.append([message.message, message.date])
                offset_id = messages[len(messages) - 1].id
                total_messages = len(all_messages)
                if total_count_limit != 0 and total_messages >= total_count_limit:
                    break

            print(len(list_message))

        except Exception as e:
            print("Exception : ", e)
            # store the error in a file errorlog.txt
            with open("errorlog.txt", "a") as f:
                f.write(str(e))
                f.write("\n")


with client:
    client.loop.run_until_complete(main(phone))
