import asyncio
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from telethon.tl.types import (PeerChannel)
from configuration_data import *
from db_connection import *

db = Database(user="root", password="", host="localhost", port=3306, db_name="twitter_bot")

string = ["https://t.me/maythouscalls", "https://t.me/Caesars_Calls", "https://t.me/Paradoxes1",
          'https://t.me/luffysgemscalls', 'https://t.me/RickandMortysCalls', 'https://t.me/doracalls',
          'https://t.me/saulsafucalls', 'https://t.me/KilluaZoldyckCalls', 'https://t.me/zekecalls',
          'https://t.me/DobbysGems', 'https://t.me/vegetacalls', 'https://t.me/gumballsgemcalls01',
          'https://t.me/WOLFS_GEM_CALLS', 'https://t.me/OnePunchCallsOfficial', 'https://t.me/bagcalls',
          'https://t.me/travladdsafureviews', 'https://t.me/drakosmoonshotz', 'https://t.me/Rickscalls',
          'https://t.me/R1C4RD0S4FUC4LLS', 'https://t.me/rockefellerscalls', 'https://t.me/jammas100x',
          'https://t.me/gollumsgems', 'https://t.me/SKULLSGEMS', 'https://t.me/Noodles_calls',
          'https://t.me/travladdsafucalls', 'https://t.me/pj69100x', 'https://t.me/DeFiWinners',
          'https://t.me/matadormoonshots', 'https://t.me/CKGEMSANN', 'https://t.me/chiroscalls',
          'https://t.me/UniApes', 'https://t.me/Chad_Crypto', 'https://t.me/SKULLSGEMSx100',
          'https://t.me/cryptocuckd', 'https://t.me/defiangelsDEALFLOW', 'https://t.me/DumpsterDAO',
          'https://t.me/Kingdom_X100_Calls_Chat', 'https://t.me/powsdegencamp', 'https://t.me/mcm_tg',
          'https://t.me/rektsfamily', 'https://t.me/goobygamblers', 'https://t.me/CryptCallsPublic',
          'https://t.me/REtardCEntrAl', 'https://t.me/bishopgemsx100', 'https://t.me/earlyapes',
          'https://t.me/CatfishcallsbyPoe', 'https://t.me/erics_calls', 'https://t.me/Joe420Calls',
          'https://t.me/thorshammergems', 'https://t.me/AeonsGems', 'https://t.me/tryTelethon1',
          'https://t.me/PrateekTestingTelethon', "https://t.me/Kingdom_X100_CALLS", "https://t.me/goobygambles",
          "https://t.me/SirGmiCalls", "https://t.me/BGAlphaDogs"]

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

    channel_present_in_db = []
    GET_CHANNEL_NAME = "SELECT channel_name FROM channel_and_id;"
    channel_in_database = db.fetchall(GET_CHANNEL_NAME)
    for i in range(len(channel_in_database)):
        user_channel = channel_in_database[i][0]
        channel_present_in_db.append(user_channel)
    print("Channel already in database are: ", channel_present_in_db)
    for channel_name in string:
        if channel_name.isdigit():
            entity = PeerChannel(int(channel_name))
        else:
            entity = channel_name
        try:
            my_channel = await client.get_entity(entity)
            channel_id = my_channel.id
            # get the channels in the channel_name column
            if channel_name in channel_present_in_db:
                print(f"{channel_name} already exists in the database")
            else:
                await asyncio.sleep(5)
                print(f"channel_name = {channel_name}, channel_id = {channel_id}")
                # enter the channel name and the id into the database of table channel_and_id
                INSERT_CHANNEL_AND_ID = "INSERT INTO channel_and_id (channel_name, id) VALUES ('{channel_name}', '{id}');"
                db.execute_query(INSERT_CHANNEL_AND_ID.format(channel_name=channel_name, id=channel_id))

        except Exception as e:
            print(e)
            continue


with client:
    client.loop.run_until_complete(main(phone))
