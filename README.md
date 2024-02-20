ni.py or "Nate's Inane Post Yeeter" is about as serious of a project as the name implies. It's a CLI Python client designed to post plain text messages simultaneously to Nostr relays of your choosing, a server that supports the Mastodon API, and BlueSky. It's a work in progress so use it as such.

## What's with the name?
* Acronym for a funny set of words
* Short, and works with the .py extention of python
* NIP, short for Nostr Imlplementation Protocol, is a quick nod to my favorite of the three

## Why?
I was bored.

However, I can see this being a handy tool for me or others. The ability to share a quick thought from the command line to one or more networks could be an easy way to send a post or ask a question, and the ability to post to multiple networks at once could be handy to those who use multiple regularly and especially useful to content creators looking to share their content. It also has has a cool retro feel and makes me think I'm a "l33t h4ck3r" because it's in the terminal.

Finally, this is also useful as a proof of concept. What I'd love to see is a GUI client that can post to the two networks, have a following feed combining users on both protocols, and be able to reply to others (and see other's replies) on multiple protocols. It wouldn't hurt to show something like that is possible by making a more primitive version that's aligned with my (lack of) skills.


## Dependencies
`pynostr`, `mastodon.py`, and `atproto` for both versions. Additionally dependencies `keyring` and `debus-python` for the keyring version.

## Installation
**Linux/Windows/Mac**
* Install Python & Pip such as e.g. `sudo apt install python3 pip` on a Debian based linux distro. If you're on Windows or Mac download Python from the [official python downloads](https://www.python.org/downloads/) and install the software. After downloading and installing Python on Windows/Mac then follow [these instructions](https://pip.pypa.io/en/stable/installation/) to install Pip.
* Install the python dependencies with pip `pip install pynostr mastodon.py atproto`
* Run via commandline (e.g. `python3 ~/scripts/ni.py`) and consider configuring an alias

*Note: If you're on a Linux distro and it warns you that the python environment is externally managed you may wish to use a virtual environment. Alternativly, I doubt the three dependencies listed above would actually conflict and in my case I just used the  `--break-systems-packages` flag. Don't do that with keyring though if you can avoid it in the keyring config section.*

**Android (Termux)**
* Run Updates `pkg update && pkg upgrade`
* Install Python `pkg add python`
* Install Compiling Tools `pkg install build-essential`
* Install Termux Specific Python Dependencies `pkg install binutils` & `pkg install python-cryptography`
* Compile Coincurve using Pip `pip install coincurve --no-binary all`
* Install Python Dependencies with Pip `pip install setuptools pynostr mastodon.py`
* Run with python (e.g. `python ~/scripts/ni.py`) and consider configuring an alias
*Note: The atproto dependency is not working on pip in Termux at the moment. You will need to delete lines 15 and 64-74 (AT/Bluesky) in order to run the script. I will update this if I find a fix.*

## Config (keyring version)

#### Part 1
*Keyring is a Python module that hands off the handling of passwords and other data to the OS on Windows, recent versions of Mac, and on the more established Linux Desktops. Instead of hardcoding your nsec and API keys into the script you can hand that off to the OS which will provide you with a level of security that more resembles a real client as apposed to a hacky python script.*
* Follow the installation steps above
* Install the Python module `keyring` and it's dependency `dbus-python`. This can be done with `pip install keyring dbus-python` on Windows or Mac. On Linux it's highly reccomended to use the versions from your native package manager if availible, such as with `apt install python3-keyring python3-dbus.mainloop.pyqt6` on a Debian based distro. If you're on Linux, but your package manager doesn't have the applicable packages, defer to the installation with Pip.

#### Part 2A
If you installed keyring on Linux via a package manager run the following commands:
* `keyring set nipy nsec` and then enter your Nostr nsec
* `keyring set nipy mastoapi` and then enter your Mastodon API Token
* `keyring set nipy mastoserver` and then enter the url of the Mastodon API compatible server in the form of `https://example.com`
* `keyring set nipy blskyname` and then enter your BlueSky username in the form of `user.bluesky.com`
* `keyring set nipy blskyapi` and then enter your BlueSky API/App Specific Password
* *With Keyring configured you are now set to run the keyring version of the ni.py script.*

#### Part 2B
If you installed keyring via pip then do the following:
* Open a python shell in your commandline (usually by typing `python` or `python3`)
* type `import keyring`
* type `keyring.set_password(service_name="nipy", username="nsec", password="-")` replacing the `-` with your Nostr nsec
* type `keyring.set_password(service_name="nipy", username="mastoapi", password="-")` replacing the `-` with your Mastodon API Token
* type `keyring.set_password(service_name="nipy", username="mastoserver", password="-")` replacing the `-` with the url of the Mastodon API compatible server in the form of `https://example.com`
* type `keyring.set_password(service_name="nipy", username="blskyname", password="-")` replacing the `-` with your BlueSky username in the form of `user.bluesky.com`
* type `keyring.set_password(service_name="nipy", username="blskyapi", password="-")` replacing the `-` with your BlueSky API/App Specific Password
* Exit the python shell by typing `exit()` or by pressing ctrl + d
* *With Keyring configured you are now set to run the keyring version of the ni.py script.*

## Config (single script version)
* (Optional) Lines 21-25: Add add, remove, or change to your preferred relays
* Line 28: Insert your Nostr private key
* Line 51: Set the URL of a Mastodon API Compatible server
* Line 52: Insert your Mastodon API Token
* Line 67: Insert your BlueSky Username and API Token/App Specific Password
* Optional: Delete Acivity Pub Portion by removing lines 14 & 50-36
* Optional: Delete AT/Bluesky portion by removeing lines 15 & 64-74

## To Do
* Add a configuration to prompt seperate posts for each platform
* Allow multiple paragraphs
* Look into why hashtages are misbehaving on Nostr
* Look into a potential way to get links to linkify themselves on BlueSky
* Look into Atproto dependencies on Termux
* De-Spaghettification my code to make it easier to modify/configure
* Maybe: Add a GUI and/or package it like you would a normal piece of software
* Pipe Dream: Add a tool that downloads the posts made by those who you follow over a specific time period (e.g. 24hrs) and export it to a text document for consumption
* Pipe Dream: Check for replies on your posts and be able to reply to other posts

## Updates
Add this repo's [RSS feed](https://github.com/0n4t3/nipy/releases.atom) to your favorite feed reader or [just about anything](https://followanything.dns7.top/). 

Or follow me on:
[Nostr](https://njump.me/npub1jy90jpcdl447ae3lp4924s65khdpvnttkg7fepmvmafycusyueksrvllx9) or [Friendica (AP Compatible)](https://nerdica.net/profile/nate0)

I also might setup a Nostr and Mastodon account for ni.py in the future to push out updates 'n stuff.

## Credit
All the hard work was done for me. Credit to [PYNostr](https://github.com/holgern/pynostr), [Mastodon.PY](https://github.com/halcy/Mastodon.py), [atproto](https://atproto.blue/en/latest/), and [Keyring](https://pypi.org/project/keyring/) for making this possible.

