ni.py or "Nate's Inane Post Yeeter" is about as serious of a project as the name implies. It's a CLI Python client designed to post plain text messages simultaneously to Nostr relays of your choosing, a server that supports the Mastodon API, and BlueSky. It's a work in progress so use it as such.

## What's with the name?
* Acronym for a funny set of words
* Short, and works with the .py extension of python
* NIP, short for Nostr Implementation Protocol, is a quick nod to my favorite of the three

## Why?
I was bored.

However, I can see this being a handy tool for me or others. The ability to share a quick thought from the command line to one or more networks could be an easy way to send a post or ask a question, the ability to post to multiple networks at once could be handy to those who use multiple regularly, and this could be useful to content creators looking to share their content across the interwebs. It also has a cool retro feel and makes me think I'm a "l33t h4ck3r" because it's in the terminal.

Finally, this is also useful as a proof of concept. What I'd love to see is a GUI client that can post to the three networks, have a following feed combining users on the protocols, and be able to reply to others (and see other's replies) on multiple protocols. It wouldn't hurt to show something like that is possible by making a more primitive version that's aligned with my (lack of) skills.


## Dependencies
`pynostr`, `mastodon.py`, and `atproto` for both versions. Additionally dependencies `keyring` and `dbus-python` for the keyring version.

## Installation (Keyring Edition)

**Install Python & Pip**
* Use your package manager on Linux, e.g. `apt install python3 pip`
* Install [Python from here](https://www.python.org/downloads/) and [Pip with these instructions](https://pip.pypa.io/en/stable/installation/) on Windows/Mac

**Download they keyring script**
* Download and extract the latest release, and copy the keyring script to your preferred directory (such as a "scripts" folder in your home directory)

**Install Dependencies**
* If on Linux, run `pip install setuptools pynostr mastodon.py atproto` (normally, or in a virtual environment). Additionally, install keyring and dbus-python from your package manager such as `apt install python3-keyring python3-dbus.mainloop.pyqt6`
* On Windows, Mac, or a Linux distro without keyring/dbus-python in it's repos, run `pip install setuptools pynostr mastodon.py atproto keyring dbus-python`

**(optional) Configure the script**
* Add/Remove/Change Nostr Relays in lines 23-27
* Disable Nostr by commenting out lines 9-13, 19-43, 80-81, 109, 112, 117-119, and 128
* Disable Activity Pub by commenting out lines 15, 47-60, 82-85, 110, 113, 120-122, and 129
* Disable BlueSky/AT by commenting out lines 16, 64-75, 86-89, 111, 114, 123-125 and 130

**Configure credentials**
* Run the script in the command line (or by double clicking it on some systems). When prompted for options, enter `creds` to configure your credentials to be stored in Keyring, and enter the relevant credentails when prompted.
* *Note: be sure to avoid entering unwanted characters, such as a space after a credential or a `/` after a URL. This would prevent the script from running and require you to re-run the credential configuration option.*

**Run Script**
* You can now run the script and choose the broadcast or post option. When prompted, type up your post, pressing enter to move to the next paragraph. When finished with the last paragraph, press enter and then `ctrl + d` (Linux/Mac) or `ctrl + z` (Win) to submit your post.
* Consider configuring an alias to allow you to run the script more easily from a command line

## Installation (Termux)
**Android (Termux)**
* Run Updates `pkg update && pkg upgrade`
* Install Python `pkg add python`
* Install Compiling Tools `pkg install build-essential`
* Install Termux Specific Python Dependencies `pkg install binutils` & `pkg install python-cryptography`
* Compile Coincurve using Pip `pip install coincurve --no-binary all`
* Install Python Dependencies with Pip `pip install setuptools pynostr mastodon.py`
* Download the latest release, and extract the simplified script.
* Run with python (e.g. `python ~/scripts/ni.py`) and consider configuring an alias
* *Note: The atproto dependency is not working on pip in Termux at the moment. You will need to use the simplified script and delete lines 15, 64-72, and 104-108 in order to run the script. I will update this if I find a fix.*

## Installation (Simplified Version) Win/Linux/Mac

**Install Python & Pip**
* Use your package manager on Linux, e.g. `apt install python3 pip`
* Install [Python from here](https://www.python.org/downloads/) and [Pip with these instructions](https://pip.pypa.io/en/stable/installation/) on Windows/Mac

**Download they simplified script**
* Download and extract the latest release, and copy the simplified script to your preferred directory (such as a "scripts" folder in your home directory)

**Install Dependencies**
Run `pip install setuptools pynostr mastodon.py atproto`

**Configure the Script**
* (Optional) Lines 21-25: Add add, remove, or change to your preferred relays
* Line 18: Insert your Nostr private key
* Line 19: Insert your Mastodon API Token
* Line 20: Set the URL of a Mastodon API Compatible server
* Line 21: Set your BlueSky username
* Line 22: Set your BlueSky API Key/App Specific Password
* Optional: Disable Nostr by commenting out lines 93-96
* Optional: Disable Activity Pub by commenting out lines 99-102
* Optional: Disable BlueSky/AT by commenting out lines 105-108

**Run the Script**
* You can now run the script via CLI (e.g. `python3 ~/scripts/ni.py`) and you may want to consider configuring an alias

## To Do
* Look into why hashtags are misbehaving on Nostr
* Look into a potential way to get links to linkify themselves on BlueSky
* Look into Atproto dependencies on Termux
* Maybe: Add a GUI and/or package it like you would a normal piece of software
* Pipe Dream: Add a tool that downloads the posts made by those you follow over a specific time period (e.g. 24hrs) and export it to a text document for consumption
* Pipe Dream: Check for replies on your posts and be able to reply to other posts

## Updates
Add this repo's [RSS feed](https://github.com/0n4t3/nipy/releases.atom) to your favorite feed reader or [just about anything](https://followanything.dns7.top/).

Or follow me on:
[Nostr](https://njump.me/npub1jy90jpcdl447ae3lp4924s65khdpvnttkg7fepmvmafycusyueksrvllx9) or [Friendica (AP Compatible)](https://nerdica.net/profile/nate0)

Semi official NIPY announcement/test accounts [Nostr](https://njump.me/npub1lpv9fq53dta94ddm7ax9j64gedlemurgejd3sl37cg2hw28msdjsf7kjnz) - [ActivityPub](https://mstdn.party/@nipy) - and [BlueSky](https://bsky.app/profile/nipy.bsky.social)

## Credit
All the hard work was done for me. Credit to [PYNostr](https://github.com/holgern/pynostr), [Mastodon.PY](https://github.com/halcy/Mastodon.py), [atproto](https://atproto.blue/en/latest/), and [Keyring](https://pypi.org/project/keyring/) for making this possible.

