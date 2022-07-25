from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
from telethon.tl.types import (
    PeerChannel
)

api_id = 17304508
api_hash = "1fa688006105dd573df6be757cc4f722"

# get the phone number and username
phone = +919717020263
username = "@CoronaVirus1234"

# Create the client and connect
client = TelegramClient(username, api_id, api_hash)


async def main(phone):
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

        offset = 0
        limit = 100
        all_participants = []

        while True:
            participants = await client(GetParticipantsRequest(
                my_channel, ChannelParticipantsSearch(''), offset, limit,
                hash=0
            ))
            if not participants.users:
                break
            all_participants.extend(participants.users)
            offset += len(participants.users)

        all_user_details = []
        for participant in all_participants:
            print(participant.first_name, participant.last_name, participant.username, participant.id)
            all_user_details.append(
                {"id": participant.id, "first_name": participant.first_name, "last_name": participant.last_name,
                 "user": participant.username, "phone": participant.phone, "is_bot": participant.bot})


with client:
    client.loop.run_until_complete(main(phone))
