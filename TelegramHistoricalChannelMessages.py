from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.messages import (GetHistoryRequest)
from telethon.tl.types import (
    PeerChannel
)

api_id = 17304508
api_hash = "1fa688006105dd573df6be757cc4f722"

# get the phone number and user name
phone = +919717020263
username = "@CoronaVirus1234"

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

    user_channel_list = ["https://t.me/teleTestingutkarsh", "https://t.me/Chad_Crypto", "https://t.me/pj69100x",
                         "https://t.me/Chad_Crypto", "https://t.me/R1C4RD0S4FUC4LLS", "https://t.me/erics_calls"]

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

        while True:
            # print("Current Offset ID is:", offset_id, "; Total Messages:", total_messages)
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
            if not history.messages:
                break
            messages = history.messages
            for message in messages:
                all_messages.append(message.to_dict())
                list_message.append([message.message, message.date])
            offset_id = messages[len(messages) - 1].id
            total_messages = len(all_messages)
            # print messages from the dictionary all_messages
            if total_count_limit != 0 and total_messages >= total_count_limit:
                break

        print(list_message[0])
        print(list_message[1])
        print(list_message[2])
        print(list_message[-1])
        print(list_message[-2])
        print(list_message[-3])
        # print(list_message)
        print(len(list_message))


with client:
    client.loop.run_until_complete(main(phone))
