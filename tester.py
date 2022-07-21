import configparser
import asyncio
from telethon import TelegramClient, events
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.messages import (GetHistoryRequest)
from telethon.tl.functions.messages import SearchRequest
from telethon.tl.types import InputMessagesFilterEmpty
from telethon.tl.types import (
    PeerChannel
)

# Reading Configs
# config = configparser.ConfigParser()
# config.read("config.ini")
#
# # Setting configuration values
# api_id = config['Telegram']['api_id']
# api_hash = config['Telegram']['api_hash']
#
# api_hash = str(api_hash)
#
api_id = 17304508
api_hash = "1fa688006105dd573df6be757cc4f722"


# get the phone number and user name
phone = +919717020263
username = "@CoronaVirus1234"

# phone = config['Telegram']['phone']
# username = config['Telegram']['username']

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

    # user_channel_list = ["https://t.me/PrateekTestingTelethon"]
    #
    # # iterate over the list of channels
    # for channel_name in user_channel_list:
    #     if channel_name.isdigit():
    #         entity = PeerChannel(int(channel_name))
    #     else:
    #         entity = channel_name
    #
    #     my_channel = await client.get_entity(entity)

        # use the NewMessage to stream the messages
        # async for message in client.iter_messages(my_channel, limit=None):
        #     print(message.message)
        #     print(message.date)
        #     print(message.sender_id)
        #     print("\n")
        #     await asyncio.sleep(1)

        # # use the NewMessage to stream the new messages
        # async for message in client.iter_messages(my_channel, limit=None, reverse=True):
        #     print(message.message)
        #     print(message.date)
        #     print(message.sender_id)
        #     print("\n")
        #     await asyncio.sleep(1)

        # # use the newmessage.newMessage to stream the new messages
        # async for message in client.iter_new_messages(my_channel, limit=None):
        #     print(message.message)
        #     print(message.date)
        #     await asyncio.sleep(1)

        # use telethon.events.newmessage.NewMessage to stream the new messages
    @client.on(events.NewMessage(chats="@teleTestingutkarsh", incoming=True))
    # @client.on(events.NewMessage(incoming=True))
    async def handler(event):
        print(event.raw_text)
        print(event.message.date)
        print(event.message.sender_id)
        print("\n")
        await asyncio.sleep(1)

        # call the event handler to stream the new messages

    await client.run_until_disconnected()

        # offset_id = 0
        # limit = 100
        # all_messages = []
        # total_messages = 0
        # total_count_limit = 0
        #
        # list_message = []

        # date_of_post = datetime.datetime(2022, 6, 12, 0, 0, 0)

        # end_time = datetime.datetime(2021, 1, 1, 0, 0, 0)
        # # end_time = datetime.datetime(2022, 2, 1, 0, 0, 0)
        # start_time = datetime.datetime.now()
        # # full_msg_list = client.get_messages(my_channel, limit=200, offset_id=200)
        # # next_200_list = client.get_messages(my_channel, limit=200, offset_id=full_msg_list[-1].id)
        # # print(next_200_list)
        #
        # filter_ = InputMessagesFilterEmpty()
        # result = await client(SearchRequest(
        #     peer=my_channel,  # On which chat/conversation
        #     q='$',  # What to search for
        #     filter=filter_,  # Filter to use (maybe filter for media)
        #     min_date=start_time,  # Minimum date
        #     max_date=end_time,  # Maximum date
        #     offset_id=0,  # ID of the message to use as offset
        #     add_offset=0,  # Additional offset
        #     limit=10,  # How many results
        #     max_id=0,  # Maximum message ID
        #     min_id=0,  # Minimum message ID
        #     from_id=None,  # Who must have sent the message (peer)
        #     hash=0  # Hash of the message to search for
        # ))

    # print(result.messages)


# client.start()
# client.run_until_disconnected(main(phone))

with client:
    client.loop.run_until_complete(main(phone))

# @client.on(events.NewMessage)
# async def my_event_handler(event):
#     if 'hello' in event.raw_text:
#         await event.reply('hi!')
#
#
# client.start()
# client.run_until_disconnected()
