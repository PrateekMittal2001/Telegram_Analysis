from telethon.tl.functions.messages import GetMessagesViewsRequest
from telethon.tl.types import PeerChannel

from constants import *
from configuration_data import *
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError

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

    # set the floodwait to 0
    client.flood_sleep_threshold = 0

    # for channel_name in user_channel_list:
    channel_name = user_channel_list[1]
    if channel_name.isdigit():
        entity = PeerChannel(int(channel_name))
    else:
        entity = channel_name
    my_channel = await client.get_entity(entity)

    # print(my_channel)
    # print(type(my_channel))
    message_id = [i for i in range(1, 500)]

    try:
        # while True:
        details = await client(GetMessagesViewsRequest(
            peer=my_channel,
            id=message_id,
            increment=False,
        ))
        # peer="PrateekTestingTelethon", id=message_id, increment=True))
        # print the number of views of the message
        print(details)
        # print(type(details.views))
        ii = 0
        for i in details.views:
            print(ii, i)
            # print(type(i))
            ii += 1
            print("\n")

    except Exception as e:
        print(e, "Some error occured")
        pass

    # get the number of views of a message
    # for message in my_channel.messages:
    #     if message.id == message_id:
    #         response = await client(GetMessagesViewsRequest(
    #             PeerChannel(int(user_channel[-10:])),
    #             [message.id]
    #         ))
    #         print(response.views)
    #         break


with client:
    client.loop.run_until_complete(main(phone))

"""
photo=ChatPhoto(photo_id=6291846881134883456, dc_id=5, has_video=False, 
stripped_thumb=b'\x01\x08\x08\xa1o\x85%\\\x02\xa4u\xf4\xa2\x8a*[c\xe4[\x9f')
"""
