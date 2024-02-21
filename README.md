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

## Installation
**Linux/Windows/Mac**
* Install Python & Pip such as e.g. `sudo apt install python3 pip` on a Debian based Linux distro. If you're on Windows or Mac download Python from the [official Python downloads](https://www.python.org/downloads/) and install the software. After downloading and installing Python on Windows/Mac then follow [these instructions](https://pip.pypa.io/en/stable/installation/) to install Pip.
* Install the Python dependencies with pip `pip install pynostr mastodon.py atproto`

*Note: If you're on a Linux distro and it warns you that the python environment is externally managed you may wish to use a virtual environment. Alternatively, I doubt the three dependencies listed above would actually conflict and in my case I just used the  `--break-systems-packages` flag. Don't do that with keyring though if you can avoid it in the keyring config section.*

**Android (Termux)**
* Run Updates `pkg update && pkg upgrade`
* Install Python `pkg add python`
* Install Compiling Tools `pkg install build-essential`
* Install Termux Specific Python Dependencies `pkg install binutils` & `pkg install python-cryptography`
* Compile Coincurve using Pip `pip install coincurve --no-binary all`
* Install Python Dependencies with Pip `pip install setuptools pynostr mastodon.py`
* Run with python (e.g. `python ~/scripts/ni.py`) and consider configuring an alias
* *Note: The atproto dependency is not working on pip in Termux at the moment. You will need to use the simplified script and delete lines 15, 64-72, and 104-108 in order to run the script. I will update this if I find a fix.*

## Config (keyring version)

#### Part 1
*Keyring is a Python module that hands off the handling of passwords and other data to the OS on Windows, recent versions of Mac, and on the more established Linux Desktops. Instead of hardcoding your nsec and API keys into the script you can hand that off to the OS which will provide you with a level of security that more resembles a real client as opposed to a hacky Python script.*
* Follow the installation steps above
* Install the Python module `keyring` and it's dependency `dbus-python`. This can be done with `pip install keyring dbus-python` on Windows or Mac.
* On Linux it's highly recommended to use the versions from your native package manager if available, such as with `apt install python3-keyring python3-dbus.mainloop.pyqt6` on a Debian based distro. If you're on Linux, but your package manager doesn't have the applicable packages, defer to the installation with Pip.

#### Part 2A
If you installed keyring on Linux via a package manager run the following commands:
* `keyring set nipy nsec` and then enter your Nostr nsec
* `keyring set nipy mastoapi` and then enter your Mastodon API Token
* `keyring set nipy mastoserver` and then enter the URL of the Mastodon API compatible server in the form of `https://example.com`
* `keyring set nipy blskyname` and then enter your BlueSky username in the form of `user.bluesky.com`
* `keyring set nipy blskyapi` and then enter your BlueSky API/App Specific Password
* You can now run the script via CLI (e.g. `python3 ~/scripts/ni.py`) and you may want to consider configuring an alias

#### Part 2B
If you installed keyring via pip then do the following:
* Open a python shell in your commandline (usually by typing `python` or `python3`)
* type `import keyring`
* type `keyring.set_password(service_name="nipy", username="nsec", password="-")` replacing the `-` with your Nostr nsec
* type `keyring.set_password(service_name="nipy", username="mastoapi", password="-")` replacing the `-` with your Mastodon API Token
* type `keyring.set_password(service_name="nipy", username="mastoserver", password="-")` replacing the `-` with the URL of the Mastodon API compatible server in the form of `https://example.com`
* type `keyring.set_password(service_name="nipy", username="blskyname", password="-")` replacing the `-` with your BlueSky username in the form of `user.bluesky.com`
* type `keyring.set_password(service_name="nipy", username="blskyapi", password="-")` replacing the `-` with your BlueSky API/App Specific Password
* Exit the python shell by typing `exit()` or by pressing ctrl + d
* You can now run the script via CLI (e.g. `python3 ~/scripts/ni.py`) and you may want to consider configuring an alias

## Config (single script version)
* (Optional) Lines 21-25: Add add, remove, or change to your preferred relays
* Line 18: Insert your Nostr private key
* Line 19: Insert your Mastodon API Token
* Line 20: Set the URL of a Mastodon API Compatible server
* Line 21: Set your BlueSky username
* Line 22: Set your BlueSky API Key/App Specific Password
* Optional: Diable Nostr by commenting out lines 93-96
* Optional: Disable Activity Pub by commenting out lines 99-102
* Optional: Disable BlueSky/AT by commenting out lines 105-108
* You can now run the script via CLI (e.g. `python3 ~/scripts/ni.py`) and you may want to consider configuring an alias

## Posting Options
By default, when running the script it will prompt you to enter one post and then broadcast the same post to the three protocols (assuming they havn't been disabled by editing the script). If you'd like to post different messages to each protocol (for example, using the tag #asknostr and #askfedi on the applicable protocol) instead of typing a post just type `dif` to instead be prompted to type each protocol's post individually. If you want to skip posting to a particular protocol, when prompted to write the post specific to it (after using dif) type `s` to skip writing a post for that network.

## To Do
* Allow multiple paragraphs
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

