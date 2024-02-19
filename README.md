ni.py or "Nate's Inane Post Yeeter" is about as serious of a project as the name implies. It's a CLI Python client designed to post plain text messages simultaneously to Nostr relays of your choosing and a server that supports the Mastodon API. It's a work in progress so use it as such.

## Why?
I was bored.

However, I can see this being a handy tool for me or others. The ability to share a quick thought from the command line to one or more networks could be an easy way to send a post or ask a question, and the ability to post to multiple networks at once could be handy to those who use multiple regularly and especially useful to content creators looking to share their content. It also has has a cool retro feel and makes me think I'm a "l33t h4ck3r" because it's in the terminal.

Finally, this is also useful as a proof of concept. What I'd love to see is a GUI client that can post to the two networks, have a following feed combining users on both protocols, and be able to reply to others (and see other's replies) on multiple protocols. It wouldn't hurt to show something like that is possible by making a more primitive version that's aligned with my (lack of) skills.


## Dependencies
`pynostr` and `mastodon.py`

## Installation

**Linux (pipx)**
* coming soon

**Linux (pip)**
* Install Python & Pip (e.g. `sudo apt install python3 pip`)
* Install Dependencies `pip install pynostr mastodon.py atproto`
* Run via commandline (e.g. `python3 [path to file]`) and consider configuring an alias

**Windows**
* coming soon

**Android (Termux)**
* Run Updates `pkg update && pkg upgrade`
* Install Python `pkg add python`
* Install Compiling Tools `pkg install build-essential`
* Install Termux Specific Python Dependencies `pkg install binutils` & `pkg install python-cryptography`
* Compile Coincurve using Pip `pip install coincurve --no-binary all`
* Install Python Dependencies with Pip `pip install setuptools pynostr mastodon.py`
* Run with `python [path to script]` amd consider configuring an alias
* **Note:** The atproto dependency is not working on pip in Termux at the moment. You will need to delete lines 15 and 64-74 (AT/Bluesky) in order to run the script. I will update this if I find a fix.

**MAC/IOS**
* Lol I'm not some Apple cultist (fine, coming soon)

## Config
* (Optional) Lines 21-25: Add add, remove, or change to your preferred relays
* Line 28: Insert your Nostr private key
* Line 51: Set the URL of a Mastodon API Compatible server
* Line 52: Insert your Mastodon API Token
* Line 67: Insert your BlueSky Username and API Token/App Specific Password
* Optional: Delete Acivity Pub Portion by removing lines 14 & 50-36
* Optional: Delete AT/Bluesky portion by removeing lines 15 & 64-74

## To Do
* Definitely: store Nostr key and Activity Pub API key in encrypted form and prompt for a password when posting
* Definitely: add the option to post different messages to each network
* Maybe: Add addition protocols (e.g. AT)
* Maybe: Add a GUI option
* Pipe Dream: Add a tool that downloads the posts made by those who you follow over a specific time period (e.g. 24hrs) and export it to a text document for consumption
* Pipe Dream: Check for replies on your posts and be able to reply to other posts

## Updates
Add this repo's [RSS feed](https://github.com/0n4t3/nipy/releases.atom) to your favorite feed reader or [just about anything](https://followanything.dns7.top/). 

Or follow me on:
[Nostr](https://njump.me/npub1jy90jpcdl447ae3lp4924s65khdpvnttkg7fepmvmafycusyueksrvllx9) or [Friendica (AP Compatible)](https://nerdica.net/profile/nate0)

I also might setup a Nostr and Mastodon account for ni.py in the future to push out updates 'n stuff.

## Credit
All the hard work was done for me. Credit to [PYNostr](https://github.com/holgern/pynostr) and [Mastodon.PY](https://github.com/halcy/Mastodon.py) for making this possible.

