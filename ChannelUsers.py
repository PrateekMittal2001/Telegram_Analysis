from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
from telethon.tl.types import (
    PeerChannel
)

# get the telegram credentials
api_id = 17653083
api_hash = "2ca12ca71050657b8c71a1621873d7f4"

# get the phone number and username
phone = +919039780234
username = "@tele_user1221"

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

    user_channel_list = ["https://t.me/teleTestingutkarsh", "https://t.me/PrateekTestingTelethon",
                         "https://t.me/Chad_Crypto", "https://t.me/R1C4RD0S4FUC4LLS", "https://t.me/pj69100x",
                         "https://t.me/erics_calls", "https://t.me/steezysgems", "https://t.me/KobesCalls",
                         "https://t.me/+Zx0NSl91_FljYjZh", 'https://t.me/Owl_Calls', 'https://t.me/Maestro007Joe',
                         'https://t.me/prince_calls', 'https://t.me/ZizzlesTrapHouse',
                         'https://t.me/mrbeast6000calls/10', 'https://t.me/venomcalls', 'https://t.me/Caesars_Calls',
                         'https://t.me/medusacalls', 'https://t.me/CowboyCallz', 'https://t.me/Kingdom_X100_CALLS',
                         'https://t.me/MarkGems',
                         'https://t.me/gollumsgems', 'https://t.me/SapphireCalls', 'https://t.me/DoxxedChannel',
                         'https://t.me/bruiserscalls', 'https://t.me/FatApeCalls', 'https://t.me/gubbinscalls',
                         'https://t.me/ValhallaCalls', 'https://t.me/TheSolitaireRoom',
                         'https://t.me/+Zx0NSl91_FljYjZh', 'https://t.me/steezysgems', 'https://t.me/KobesCalls',
                         'https://t.me/Chad_Crypto', 'https://t.me/+ZVqgZ6EDWlFiZGFl', 'https://t.me/erics_calls',
                         'https://t.me/R1C4RD0S4FUC4LLS']

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
