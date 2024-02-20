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

# Keyring Credential Management
nos = (keyring.get_credential(service_name="nipy", username="nsec"))
nsec = nos.password
masto_api = (keyring.get_credential(service_name="nipy", username="mastoapi"))
mastoapi = masto_api.password
masto_server = (keyring.get_credential(service_name="nipy", username="mastoserver"))
mastourl = masto_server.password
at_name = (keyring.get_credential(service_name="nipy", username="blskyname"))
atname = at_name.password
at_api = (keyring.get_credential(service_name="nipy", username="blskyapi"))
atapi = at_api.password


#Nostr Portion

relay_manager = RelayManager(timeout=6)

#Add or remove relays
relay_manager.add_relay("wss://nos.lol")
relay_manager.add_relay("wss://relay.damus.io")
relay_manager.add_relay("wss://relay.primal.net")
relay_manager.add_relay("wss://offchain.pub")
relay_manager.add_relay("wss://nostr.oxtr.dev")

#Insert your nsec
private_key = PrivateKey.from_nsec(nsec)

filters = FiltersList([Filters(authors=[private_key.public_key.hex()], limit=100)])
subscription_id = uuid.uuid1().hex
relay_manager.add_subscription_on_all_relays(subscription_id, filters)

event_content = input("Enter Post: ")
print("Yeet!")
event = Event(event_content)
event.sign(private_key.hex())

relay_manager.publish_event(event)
relay_manager.run_sync()
time.sleep(5)
while relay_manager.message_pool.has_ok_notices():
    ok_msg = relay_manager.message_pool.get_ok_notice()
while relay_manager.message_pool.has_events():
    event_msg = relay_manager.message_pool.get_event()
print("Nostr Post (most likely) Successful")

#Fedi Portion

#Set your server and access token
server = mastourl
token = mastoapi

mastodon = Mastodon(
    access_token = token,
    api_base_url = server
)

tooter = mastodon.toot(event_content)
print("AP Post Successful: ", tooter['uri'])

#AT Portion
def atproto():
    client = Client()
    profile = client.login(atname, atapi)
    print('AT Post (most likely) Successful')

    text = client_utils.TextBuilder().text(event_content)
    post = client.send_post(text)

atproto()
