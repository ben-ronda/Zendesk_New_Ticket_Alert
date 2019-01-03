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

`$ python3 --version`
>If you do not have Python3 installed then you can install it via Homebrew:
>`$ brew install python3`

>___Note:___ _If you do not have Homebrew you can install it by running:_
>`$ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`
>
>_You can find more information about Homebrew on the official site:_ https://brew.sh/

Next, clone this repository to your machine: `$ git clone https://github.com/ben-ronda/Zendesk_New_Ticket_Alert.git`

Once you have done that you will need to `cd` in to the top level of the project directory and create a file called `auth.py`

`$ touch auth.py`

Inside you will need to write the following lines:

    # Zendesk Authentication
    url = 'https:/<your_subdomain.zendesk.com/api/v2/tickets.json'
    email = 'your_email'
    key = 'your_API_key'

This will allow the tickets script to authenticate the Zendesk API calls.

<!-- __Note:__ If you do not want to go through the effort of creating this file, you can manually enter these credentials inside the script itself on lines 11-13. If you do this, you may also get rid of or comment out line 8 which calls on auth.py to access those global variables. -->

You will need to place a .mp3 file in the top level of the project directory and change the file name on line 34 of tickets file where you see `subprocess.call(['afplay', 'you_suffer.mp3'])`. _You may also use m4a, WAV, AIFF, and supposedly a few other audio file types._

***
# Usage

To run this you, type the following command in the top level of the project directory:

`$ python3 tickets`

If you want to be able to run this without typing `python3` then run the following command as well:

`$ chmod -x tickets`

Now you can simply type `./tickets`
