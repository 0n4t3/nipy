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

## Installation (Pip/Pipx - Recommended)
* Install Python and Pip/Pipx. On Linux use your package manager, e.g. `apt install python3 pipx` then `pipx ensurepath` to make sure CLI prompts work. Get [Python from here](https://www.python.org/downloads/) and [Pip with these instructions](https://pip.pypa.io/en/stable/installation/) on Windows/Mac.
* Install NIPY using `pip install nipyproto` or `pipx install nipyproto`
* Run NIPY by entering `nipyproto` in your CLI. Run creds to configure creds when prompted, then you're ready to post :)


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
* *Note: The atproto dependency is not working standard Termux shell. It does, however, work in my Debian proot distro. The keyring version will not work in either, however, as Keyring requires a compatible Desktop Environment to delegate credential management to.*

## Installation (Simplified Version) Win/Linux/Mac
**Install Python & Pip**
* Use your package manager on Linux, e.g. `apt install python3 pip`
* Install [Python from here](https://www.python.org/downloads/) and [Pip with these instructions](https://pip.pypa.io/en/stable/installation/) on Windows/Mac

**Download they simplified script**
* Download and extract the latest release, and copy the simplified script to your preferred directory (such as a "scripts" folder in your home directory)

**Install Dependencies**
Run `pip install setuptools pynostr mastodon.py atproto`

**Configure the Script**
* (Optional) Lines 28-32: Add add, remove, or change to your preferred Nostr relays
* Line 18: Insert your Nostr private key
* Line 19: Insert your Mastodon API Token
* Line 20: Set the URL of a Mastodon API Compatible server
* Line 21: Set your BlueSky username
* Line 22: Set your BlueSky API Key/App Specific Password
* Optional: Disable Nostr by commenting out lines 98 & 114
* Optional: Disable Activity Pub by commenting out lines 99 & 115
* Optional: Disable BlueSky/AT by commenting out lines 100 & 116

**Run the Script**
* You can now run the script via CLI (e.g. `python3 ~/scripts/ni.py`) and you may want to consider configuring an alias

## To Do
Honestly, this is mostly pretty much how I expect the project to stay. Thanks to libraries that will keep themselves updated there's no real worry about it becoming incompatible or running into security issues - my code is pretty simple and is mostly just instructions to pipe info into libraries that do the heavy lifting.

This was largely created as a proof of concept and a possibly useful tool in a very specific set of circumstances (like, say, trying to create a way for people to follow blog posts on all platforms). It can accomplish both, and I got to toy around with Python, so I'd call that a win.

Things maybe worth looking into:
* Look into why hashtags & embedded posts are misbehaving on Nostr
* Look into a potential way to get links to linkify themselves on Bluesky

## Updates
Add this repo's [RSS feed](https://github.com/0n4t3/nipy/releases.atom) to your favorite feed reader or [just about anything](https://followanything.dns7.top/).

Or follow me on:
[Nostr](https://njump.me/npub1jy90jpcdl447ae3lp4924s65khdpvnttkg7fepmvmafycusyueksrvllx9) or [Friendica (AP Compatible)](https://nerdica.net/profile/nate0)

*Note, Nerdica.ca has been having some trouble. Not sure if it'll be back online or not, but I may not get your message if you @ me there.*

Semi official NIPY announcement/test accounts [Nostr](https://njump.me/npub1lpv9fq53dta94ddm7ax9j64gedlemurgejd3sl37cg2hw28msdjsf7kjnz) - [ActivityPub](https://mstdn.party/@nipy) - and [BlueSky](https://bsky.app/profile/nipy.bsky.social)

## Credit
All the hard work was done for me. Credit to [PYNostr](https://github.com/holgern/pynostr), [Mastodon.PY](https://github.com/halcy/Mastodon.py), [atproto](https://atproto.blue/en/latest/), and [Keyring](https://pypi.org/project/keyring/) for making this possible.

