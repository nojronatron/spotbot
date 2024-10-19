# spotbot

## Description

Spotbot is an Azure Function App to convert [HamAlert](https://hamalert.org/) alerts from [POTA](https://pota.app) or [SOTA](https://www.sota.org.uk/) in to a message format that can be forwarded on to a Discord channel webhook.

| HamAlert Configuration |
| -- |
| ![image](https://github.com/user-attachments/assets/c25f8966-e107-4e67-838c-11ada7c5309d) |

| Discord Message |
| -- |
| ![image](https://github.com/user-attachments/assets/f664d60f-2042-4b2d-9c88-4ce4051f17c7) |


The function uses a Table in an Azure Storage Account to store the `messageId` of the last message posted for each callsign. If that message was posted recently (as defined by `LOOKBACK_SECONDS`), it will _update_ the message instead of posting a new one to reduce the chatter of the bot.

You can find a live, working version of this bot in the [Cascadia Radio](https://www.cascadiaradio.org/) Discord server, in the `#spots` channel. Join us!

## Config

The Azure Function App expects three environment variables: 
- `TARGET_URL` - the webhook URL from the target Discord channel.
- `LOOKBACK_SECONDS` - the number of seconds to look backwards for previous messages to update instead of posting a new one
- `TABLE_NAME` - the name of the table in the Azure Storage Account where the last messageIds will be stored for each callsign

## Deploy Notes

- Some basic tests run in `tests.py` on the creation of a new PR
- To deploy, manually run `main_hamalertspotbot.yml`
    - This will deploy to the staging slot for testing. 
    - The staging `TARGET_URL` points to my private Discord server
    - `LOOKBACK_SECONDS` is set to only 300 (instead of 7200) for easier testing.

## The 2k Character Limit

The Discord 2,000 character limit looks like this:

```text
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
```

## SpotBot entries look like this

N7KOM | [sotawatch](https://sotl.as/activators/N7KOM) | freq: 146.520 | mode: fm | loc: W6/NE-074 freq: 7.235 | mode: ssb | loc: W7I/NI-203

Theoretically, 20 'sotawatch' entries could be made before reaching the 2k character limit (not tested).

If SpotBot updates an entry the Discord API will add an `(edited)` comment to the post.

## Discord Webhook API Note

Use of 'Embeds' property might be useful? Although it is limited to a total of 10 items.

To add-on updates (rather than overwrite), the `fields` array (properties 'name': string, 'value': string, 'inline': bool) could get the job done. Just push a new 'field' object with each subsequent HamAlert where Band and/or Mode has changed.

_Note_: Wierdly, 'name' and 'value' properties get displayed in block-style within the 'embeds' portion of the message.
