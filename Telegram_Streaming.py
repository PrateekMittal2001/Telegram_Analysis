from telethon import TelegramClient, events
from telethon.errors import SessionPasswordNeededError


api_id = 17304508
api_hash = "1fa688006105dd573df6be757cc4f722"

# get the phone number and username
phone = +919717020263
username = "@CoronaVirus1234"


# Create the client and connect
client = TelegramClient(username, api_id, api_hash)


# create a search function to filter the data
def search(data, search_term):
    if search_term in data:
        return True


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
    @client.on(events.NewMessage(chats= ["@teleTestingutkarsh", "@PrateekTestingTelethon", "https://t.me/Chad_Crypto", "https://t.me/pj69100x", "https://t.me/Chad_Crypto"] , incoming=True ))
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


# client.start()
# client.run_until_disconnected(main(phone))

with client:
    client.loop.run_until_complete(main(phone))
