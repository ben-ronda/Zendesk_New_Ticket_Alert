# ZenAlert

## A Python script that alerts when new Zendesk ticket comes in.
#### Created by: [Ben Ronda](https://github.com/ben-ronda)
***
## Description

This is a script that will play an audio file whenever a new Zendesk ticket is detected. It uses the Zendesk Support API to scan all Zendesk tickets for tickets with the status `new` then counts them and stores that number in a variable. It continues to do this until the number of new tickets in Zendesk is greater than the number of new tickets it counted on the previous scan. When that happens it plays the audio file, updates the local counter of Zendesk tickets and continues to scan for new tickets. If the number of new tickets in the Zendesk client is updated to be less than the count stored locally, it will update the ticket counter in the script without playing the audio file.
