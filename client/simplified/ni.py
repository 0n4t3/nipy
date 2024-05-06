import json
import ssl
import time
import uuid
import sys
import os
import pkg_resources
from pynostr.event import Event
from pynostr.relay_manager import RelayManager
from pynostr.filters import FiltersList, Filters
from pynostr.message_type import ClientMessageType
from pynostr.key import PrivateKey
from pkg_resources import DistributionNotFound
from mastodon import Mastodon
from atproto import Client, client_utils

# Credential Management
nsec = "nsec123" #enter your nsec
mastoapi = "123abc" #enter your Activity Pub account API key
mastourl = "https://example.com" #enter the url of your Mastodon API compatible fedi server
atname = "username.bsky.social" #enter your username on BlueSky
atapi = "abc123" #enter your app specific password
# End of Credential Management Stuffs

# Nostr Post Module
def nostr():
	relay_manager = RelayManager(timeout=6) #Relay Management from PyNostr, add or remove your relays below
	relay_manager.add_relay("wss://nos.lol")
	relay_manager.add_relay("wss://relay.damus.io")
	relay_manager.add_relay("wss://relay.primal.net")
	relay_manager.add_relay("wss://offchain.pub")
	relay_manager.add_relay("wss://nostr.oxtr.dev")

	private_key = PrivateKey.from_nsec(nsec)
	filters = FiltersList([Filters(authors=[private_key.public_key.hex()], limit=100)])
	subscription_id = uuid.uuid1().hex
	relay_manager.add_subscription_on_all_relays(subscription_id, filters)
	event = Event(nostr_post)
	event.sign(private_key.hex())

	relay_manager.publish_event(event)
	relay_manager.run_sync()
	time.sleep(5)
	while relay_manager.message_pool.has_ok_notices():
		ok_msg = relay_manager.message_pool.get_ok_notice()
	while relay_manager.message_pool.has_events():
		event_msg = relay_manager.message_pool.get_event()
	print("Nostr Post (most likely) Successful")
# End of Nostr Stuffs

# ActivityPub/Mastodon API Module
def masto():
	server = mastourl
	token = mastoapi
	mastodon = Mastodon(
		access_token = token,
		api_base_url = server
	)

	tooter = mastodon.toot(ap_post)
	print("AP Post Successful: ", tooter['uri'])
# End of AP Stuffs

# BlueSky/AT Protocol Module
def at_proto():

	client = Client()
	profile = client.login(atname, atapi)
	print('AT Post (most likely) Successful')

	text = client_utils.TextBuilder().text(at_post)
	post = client.send_post(text)
# End of BlueSky Stuffs

def configurecreds():
	print("You are currently using the simplified version of the NIPY script. Credential management is hard-coded directly into the script itself, to set yours please open the script in a text editor. If you are on a system that supports it, I highly recommend using the keyring version which delegates managing your credentials to your OS or Desktop Environment.")

#Help tool
def helptool():
	print("NIPY, or ni.py, is a Python-based post-only client that works with the three largest non-centralized social media protocols: Nostr, Activity Pub, and the AT Protocol. Credential management would generally be managed by the OS instead of the script; however you are on the simplified script which does not rely on keyring for credential managment. Please run creds for more information. For assistance please check the GitHub repo at https://github.com/0n4t3/nipy or contact me on Nostr at nate@nate.mecca1.net or on Activity Pub at nate0@nerdica.net.")
	print(" ")
	print("NIPY is licensed GPLv3. NI.PY is also experimental software and comes with no warranties, explicit or implied.")
	print(" ")
	print("Thank you for using NI.PY")

#Startup Script
print("Welcome to NI.PY. Please enter broadcast to send a broadcast to all accounts, post to enter individual posts for each account, creds to perform initial setup or to re-configure existing credentials, and help for more info.")
prompt = input("Enter Option: ")

if prompt == "broadcast":
	print("Enter Post to Broadcast. When finished press enter and then CTL + D on Linux/Mac or CTL + Z on Windows")
	post = sys.stdin.read()
	#Post Messages
	print("Yeet!")
	nostr_post = post
	ap_post = post
	at_post = post
	nostr()
	masto()
	at_proto()

elif prompt == "post":
	print("Enter Nostr Post. When finished press enter and then CTL + D on Linux/Mac or CTL + Z on Windows")
	nostr_post = sys.stdin.read()
	print("Nostr Post Saved :)")
	print("Enter Activity Pub Post. When finished press enter and then CTL + D on Linux/Mac or CTL + Z on Windows")
	ap_post = sys.stdin.read()
	print("AP Post Saved :)")
	print("Enter AT Protocol Post. When finished press enter and then CTL + D on Linux/Mac or CTL + Z on Windows")
	at_post = sys.stdin.read()
	print("AT Post Saved :)")
	#Post Messages
	print("Yeet!")
	nostr()
	masto()
	at_proto()

elif prompt == "creds":
	configurecreds()
elif prompt == "help":
	helptool()
else:
	print("Input Unrecognized, please try again.")
