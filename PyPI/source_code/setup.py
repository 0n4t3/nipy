from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='nipyproto',
    version='1.1.1',
    description='Post only client for Nostr, Activity Pub, and AT',
    long_description=long_description,
    long_description_content_type='text/markdown',
    py_modules=['nipyproto'],
    install_requires=['pynostr', 'mastodon.py', 'atproto', 'keyring'],
    entry_points={
        'console_scripts': [
            'nipyproto = nipyproto:nipyproto',
        ],
    },
)
