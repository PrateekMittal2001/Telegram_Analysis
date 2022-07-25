from telethon import TelegramClient, events
from telethon.errors import SessionPasswordNeededError
from constants import *
import cryptg


# get the telegram credentials
api_id = 17653083
api_hash = "2ca12ca71050657b8c71a1621873d7f4"

# get the phone number and username
phone = +919039780234
username = "@tele_user1221"


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

    # use telethon.events.newmessage.NewMessage to stream the new messages
    # @client.on(events.NewMessage(chats="@teleTestingutkarsh", incoming=True, from_users= [@teleTestingutkarsh", "https://t.me/Chad_Crypto", "https://t.me/pj69100x"))
    try:
        @client.on(events.NewMessage(chats= user_channel_list , incoming=True ))
        # @client.on(events.NewMessage(incoming=True))
        async def handler(event):
            # print("event :", event)
            print(event.text)
            textty = event.text
            print(event.message.date)
            # print(event.message.sender_id)
            # print the utf id of text
            if len(textty) != 0:
                print(ord(textty[0]))
            else:
                print("Fuck You Bitch")
            print("\n")
            # await asyncio.sleep(1)

            # call the event handler to stream the new messages

        await client.run_until_disconnected()

    except Exception as e:
        print(e, "Some error occured")
        pass


# client.start()
# client.run_until_disconnected(main(phone))

with client:
    client.loop.run_until_complete(main(phone))
