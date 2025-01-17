# Music Player - v2.2

- An Telegram Bot to Play Radio/Music in Channel or Group Voice Chats.
- A Telegram Bot to Play Audio in Voice Chats With Youtube and Deezer support.
- Supports Live streaming from YouTube.

## How to deploy 

Click the below button to watch the video tutorial on deploying

<a href="https://youtu.be/FGZr-V2lCo8"><img src="https://img.shields.io/badge/How%20To%20Deploy-blue.svg?logo=Youtube"></a>
<a href="https://youtu.be/FGZr-V2lCo8"><img src="https://img.shields.io/youtube/views/FGZr-V2lCo8?style=social">

## Deploy to Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/LushaiMusic/VCMusicPlayer)

### Deploy to VPS

```sh
git clone https://github.com/LushaiMusic/VCMusicPlayer
cd VCMusicPlayer
pip3 install -r requirements.txt
# <Create Variables appropriately>
python3 main.py
```

# Configs Vars:
1. `API_ID` : Get From [my.telegram.org](https://my.telegram.org) or [@UseTGzKBot](https://telegram.dog/UseTGzKBot).
2. `API_HASH` : Get from [my.telegram.org](https://my.telegram.org) or [@UseTGzKBot](https://telegram.dog/UseTGzKBot).
3. `ARQ_API` : Get it for free from [@ARQRobot](https://telegram.dog/ARQRobot), This is required for /dplay to work.
4. `BOT_TOKEN` : [@Botfather](https://t.me/BotFather).
5. `SESSION_STRING` : Generate From here [![GenerateStringName](https://img.shields.io/badge/repl.it-generateStringName-yellowgreen)](https://replit.com/@ZauteKm/GenerateStringSession)
6. `CHAT` : ID of Channel/Group where the bot plays Music. Channel ID Get From [@UseTGidBot](https://t.me/UseTGidBot).
7. `LOG_GROUP` : Group to send Playlist, if CHAT is a Group
8. `ADMINS` : ID of users who can use admin commands.
9. `STREAM_URL` : Stream URL of radio station to stream when the bot starts or with /radio command.

- Enable the worker after deploy the project to Heroku
- Bot will starts radio automatically in given `CHAT` with given `STREAM_URL` after deploy.(24*7 Music even if heroku restarts, radio stream restarts automatically.)  
- To play a song use /play as a reply to audio file or a youtube link.
- Use /play <song name> to play song from youtube and /dplay <song name> to play from Deezer.
- Use /help to know about other commands.

### Features:

- Playlist, queue
- Supports Live streaming from youtube
- Supports both deezer and youtube to search songs.
- Play from telegram file supported.
- Starts Radio after if no songs in playlist.
- Automatically downloads audio for the first two tracks in the playlist to ensure smooth playing
- Automatic restart even if heroku restarts.

## Requirements

- Python 3.6 or higher.
- A
  [Telegram API key](https://docs.pyrogram.org/intro/quickstart#enjoy-the-api)
  and a Telegram account.
- [FFmpeg Python](https://www.ffmpeg.org/)
- Telegram [String Session](http://t.me/UsePyrogramBot) of the account.
- Userbot Needs To Be Admin In The Channel or Group.
- Must Start A Voice Chat In Channel/Group Before Running The Bot.

## License
```sh
VC Music Player, Telegram Voice Chat Userbot
Copyright (C) 2021  Zaute Km

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
```

## Credits

- [Zaute Km](https://github.com/ZauteKm) [Dev]
- [Dash Eclipse](https://github.com/dashezup) [For tgvc_userbot]
- [Marshal X](https://github.com/MarshalX) [For pytgcalls]
