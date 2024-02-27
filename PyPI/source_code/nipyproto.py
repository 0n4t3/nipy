import json
import ssl
import time
import uuid
import sys
import os
import pkg_resources
import keyring
from pynostr.event import Event
from pynostr.relay_manager import RelayManager
from pynostr.filters import FiltersList, Filters
from pynostr.message_type import ClientMessageType
from pynostr.key import PrivateKey
from pkg_resources import DistributionNotFound
from mastodon import Mastodon
from atproto import Client, client_utils

# Nostr Post Module
def nostr():
	nos = (keyring.get_credential(service_name="nipy", username="nsec"))
	nsec = nos.password
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
	masto_api = (keyring.get_credential(service_name="nipy", username="mastoapi"))
	mastoapi = masto_api.password
	masto_server = (keyring.get_credential(service_name="nipy", username="mastoserver"))
	mastourl = masto_server.password
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
	at_name = (keyring.get_credential(service_name="nipy", username="blskyname"))
	atname = at_name.password
	at_api = (keyring.get_credential(service_name="nipy", username="blskyapi"))
	atapi = at_api.password

	client = Client()
	profile = client.login(atname, atapi)
	print('AT Post (most likely) Successful')

	text = client_utils.TextBuilder().text(at_post)
	post = client.send_post(text)
# End of BlueSky Stuffs

def configurecreds():
	print("Welcome to the NIPY/ni.py credential manager. This can add or update credentials stored in Keyring, when prompted please enter information. Make sure there is no extra spaces or other unintended characters as that can prevent the script from working until you re-do this process.")
	nsecinput = input("Please enter your Nostr nsec: ")
	keyring.set_password("nipy", "nsec", nsecinput)
	masto_apiinput = input("Please enter your Mastodon API Key: ")
	keyring.set_password("nipy", "mastoapi", masto_apiinput)
	masto_serverinput = input("Please enter the URL of your Mastodon API compatible server - e.g. https://example.com: ")
	keyring.set_password("nipy", "mastoserver", masto_serverinput)
	at_nameinput = input("Please enter your BlueSky username - e.g. username.blsky.social: ")
	keyring.set_password("nipy", "blskyname", at_nameinput)
	at_apiinput = input("Please enter your BlueSky app password: ")
	keyring.set_password("nipy", "blskyapi", at_apiinput)
	print("Credentials have been created/updated. You are now ready to make a post with ni.py")

#Help tool
def helptool():
	print("NIPY, or ni.py, is a Python-based post-only client that works with the three largest non-centralized social media protocols: Nostr, Activity Pub, and the AT Protocol. Credential management is performed by the OS instead of the script with the Keyring Python module. Please run the credentials tool for initial configuration, or if you have recently updated your credentials. For assistance please check the GitHub repo at https://github.com/0n4t3/nipy or contact me on Nostr at nate@nate.mecca1.net or on Activity Pub at nate0@nerdica.net.")
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
	
sys.exit()