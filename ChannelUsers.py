from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
from telethon.tl.types import (
    PeerChannel
)
from constants import *
from configuration_data import *


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