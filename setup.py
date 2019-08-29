from os.path import isfile
from setuptools import setup, find_packages


def auto_upgrade():

    upgrades = ['patch', 'minor', 'major']
    upgrade = ''

    while upgrade not in upgrades:
        upgrade = input(
            'Please select the type of upgrade: (major|minor|patch) > ')

    if isfile('version.cfg'):
        with open('version.cfg', 'r') as f:
            version = f.read()
    else:
        with open('version.cfg', 'w') as f:
            version = '0.0.0'
            f.write(version)

    version = version.replace('.', '')
    major = int(version[0])
    minor = int(version[1])
    patch = int(version[2])

    if upgrade == 'major':
        major += 1
        minor = 0
        patch = 0
    elif upgrade == 'minor':
        minor += 1
        patch = 0
    elif upgrade == 'patch':
        patch += 1

    version = f'{major}.{minor}.{patch}'

    with open('version.cfg', 'w') as f:
        f.write(version)

    return version


setup(
    name="YDLH",
    version=auto_upgrade(),
    packages=find_packages(),
)
