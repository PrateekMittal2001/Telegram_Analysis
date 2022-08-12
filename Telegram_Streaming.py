import re
from db_connection import *
from constants import *
from configuration_data import *
from telethon import TelegramClient, events
from telethon.tl.types import PeerUser, PeerChat, PeerChannel
from telethon.errors import SessionPasswordNeededError

# Create the client and connect
client = TelegramClient(username, api_id, api_hash)

filtered_user_channel_list = []
token_symbol = "$"

db = Database(user="root", password="", host="localhost", port=3306, db_name="twitter_bot")


# filter the channel list to get the unique user channels
def get_unique_channels(channel_list):
    channel_list = set(channel_list)
    channel_list = list(channel_list)
    return channel_list


# function to filter the user_channel_list
def filter_user_channel_list(channel_list):
    list_sliced = []
    for i in channel_list:
        # split the names using /
        sliced = i.split("/")
        sliced = "@" + sliced[-1]
        list_sliced.append(sliced)
    set_sliced = set(list_sliced)
    list_sliced = list(set_sliced)
    return list_sliced


filtered_user_channel_list = filter_user_channel_list(user_channel_list)


def filter_token_from_message(message):
    if token_symbol in message:
        message = message.split(token_symbol)
        message = message[1]
        message = message.split(" ")
        message = message[0]
        if not message.isdigit():
            message = "$" + message
            return message


def filter_links_from_message(message):
    data = re.compile('(?:(?:https?|ftp):\/\/)[\w/\-?=%.]+\.[\w/\-&?=%.]+')
    new = data.findall(message)
    return new


def get_pair_id_from_dex(dexlink):
    dexlink = dexlink.split("/")
    if len(dexlink[-1]) > 1:
        dexlink = dexlink[-1]
    else:
        dexlink = dexlink[-2]
    return dexlink


def get_token_symbol(token):
    symbol = db.fetchall(GET_TOKEN_SYMBOL.format(pair_id=token))
    print("symbol = ", symbol)
    if len(symbol) == 0:
        symbol = "Not Found"
        return "Not_Found"
    else:
        return symbol[0][0]


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

    # use telethon.events.newmessage.NewMessage to stream the new messages
    try:
        @client.on(events.NewMessage(chats=filtered_user_channel_list, incoming=True))
        # @client.on(events.NewMessage(incoming=True))
        async def handler(event):
            print(event)
            textty = event.text
            print("Message = ", textty)
            # print the channel name and the message
            print("channel id = ", event.chat_id)
            # using the chat_id print the channel name
            print(event.message.date)
            token = filter_token_from_message(textty)
            print("token = ", token, " Token ended")
            links = filter_links_from_message(textty)
            print("links = ", links, " Links ended")
            dexlink = weblink = telelink = tweetlink = "Not Found"
            if len(links) != 0:
                for link in links:
                    if 'dextools' in link or 'dexscreener' in link:
                        dexlink = link
                        print("dexlink = ", dexlink)
                    elif "twitter" in link:
                        tweetlink = link
                    elif 't.me' in link:
                        telelink = link
                        print("telelink = ", telelink)
                    elif '.com' in link:
                        weblink = link
                        print("websitelink = ", weblink)
                dex_pair_id = get_pair_id_from_dex(dexlink)
                print("dex_pair_id = ", dex_pair_id)
                token_symbol = get_token_symbol(dex_pair_id)

                # if token_symbol not in tweetlink:
                #     twitterlink = "Not Found"
                # if token_symbol not in telelink:
                #     telelink = "Not Found"
                # if token_symbol not in weblink:
                #     weblink = "Not Found"

                # print("token_symbol", token_symbol)
                # if token_symbol != "Not_Found":
                #     a = INSERT_COIN_DATA_TO_TABLE.format(
                #         token=token_symbol,
                #         dexlink=dexlink,
                #         telelink=telelink,
                #         weblink=weblink,
                #         twitterlink=tweetlink,
                #     )
                #     db.execute_query(a)
                #     print("Data inserted")
            else:
                print("No link found in the message")
            # print the message is not text
            if len(textty) == 0:
                print("Ye non text hai, chup chaap text bhejo")
            print("\n")
            print(client.get_entity(PeerChannel(textty.chat_id)))

        await client.run_until_disconnected()

    except Exception as e:
        print(e, "Some error occured")
        pass


with client:
    client.loop.run_until_complete(main(phone))
