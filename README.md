# ZenAlert
#### Created by: [Ben Ronda](https://github.com/ben-ronda)
***
## Description

This is a script that will play an audio file whenever a new Zendesk ticket is detected. It uses the Zendesk Support API to scan all Zendesk tickets for tickets with the status `new` then counts them and stores that number in a variable. It continues to do this until the number of new tickets in Zendesk is greater than the number of new tickets it counted on the previous scan. When that happens it plays the audio file, updates the local counter of Zendesk tickets and continues to scan for new tickets. If the number of new tickets in the Zendesk client is updated to be less than the count stored locally, it will update the ticket counter in the script without playing the audio file.

***
## Dependencies

This project uses the following python modules:
* requests - `pip install requests`
* json
* time
* subprocess

If you don't have pip installed but you are using Python3 then try running `pip3` instead of `pip`

***
## Installation

The first thing you need to do is make sure you have Python3 installed on you machine. In your terminal, run:

`python3 --version`

If you do not have Python3 installed then you can install it via Homebrew:

`brew install python3`

___Note:___ _If you do not have Homebrew you can install it by running:_

`$ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`

_You can find more information about Homebrew on the official site:_ https://brew.sh/
