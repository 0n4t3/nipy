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

# Prompt for post.
# Enter "dif" to be prompted to post different posts to different protocols
# If you are entering different posts for different protocols, typing "s" will skip posting to that particular protocol.
post = input("Enter Post: ")

if post == "dif":
	nostr_post = input("Enter Nostr Post: ")
	ap_post = input("Enter AP Post: ")
	at_post = input("Enter AT Post: ")
else:
	nostr_post = post
	ap_post = post
	at_post = post
# End of post prompts

#Post Messages
print("Yeet!")

#run Nostr Module
if nostr_post == "s":
	print("Skipping Nostr Post")
else:
	nostr()

#run Mastodon API Module
if ap_post == "s":
	print("Skipping Activity Pub Post")
else:
	masto()

#run AT Module
if at_post == "s":
	print("Skipping AT Post:")
else:
	at_proto()
#End of message posting stuffs

