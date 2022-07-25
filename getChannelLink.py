from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
import re, itertools
# api_id and api_hash
api_id = 10468333
api_hash = "eab47309851da605d388b9ceee93acaf"

# get the phone number and username
phone = +918860377197
username = '@Gojo_2001'

# Create the client and connect
client = TelegramClient(username, api_id, api_hash)
search_matrix = ["https://t.me/", "https://telegram.me/"]
links = []

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
    # print(me)

    list_message = []

    try:
        async for message in client.iter_messages(1595324055):
            # print(message.text)
            # if the message contains https://t.me/ or https://telegram.me/ copy the message and save it in list
            # list_message
            if message.text is not None:
                for ele in search_matrix:
                    if ele in message.text:
                        list_message.append(message.text)
                        # print(message.text)
                        regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
                        url = re.findall(regex, message.text)
                        # print(url)
                        links.append(url[0][0])
                        print([x[0] for x in url])
                #         a = list(itertools.chain(*url))
        print(links)
    except Exception as e:
        print(e, "Some error occured")

    # print(*list_message, sep="\t message ends \n", end=" streaming ended")


with client:
    client.loop.run_until_complete(main(phone))
