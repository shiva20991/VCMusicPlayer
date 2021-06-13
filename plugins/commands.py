"""
VC Music Player, Telegram Voice Chat Userbot
Copyright (C) 2021  Zaute Km | TGVCSETS

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
"""

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters



HOME_TEXT = "<b>Helo, [{}](tg://user?id={})\n\nI am @TAMILROCKERSVPN Music Player"
HELP = """

<b>.

Start a VoiceChat

Use /play <song name> or use /play as a reply to an audio file or youtube link.

You can also use /dplay <song name> to play a song from Deezer.</b>

**Common Commands**:

**/play**  Reply to an audio file or YouTube link to play it or use /play <song name>.
**/dplay** Play music from Deezer, Use /dplay <song name>
**/player**  Show current playing song.
**/help** Show help for commands
**/playlist** Shows the playlist.

**Admin Commands**:
**/skip** [n] ...  Skip current or n where n >= 2
**/join**  Join voice chat.
**/leave**  Leave current voice chat
**/vc**  Check which VC is joined.
**/stop**  Stop playing.
**/radio** Start Radio.
**/stopradio** Stops Radio Stream.
**/replay**  Play from the beginning.
**/clean** Remove unused RAW PCM files.
**/pause** Pause playing.
**/resume** Resume playing.
**/mute**  Mute in VC.
**/unmute**  Unmute in VC.
**/restart** Restarts the Bot.
"""



@Client.on_message(filters.command('start'))
async def start(client, message):
    buttons = [
        [
        InlineKeyboardButton('👥 Group', url='https://t.me/tamilblasterslive'),
        InlineKeyboardButton('Dubbed', url='https://t.me/TRVPN'),
    ],
    [
        InlineKeyboardButton('🤫 Source', url='https://t.me/TRVPN'),
        InlineKeyboardButton('Channel 📢', url='https://t.me/TAMILROCKERSVPN'),
    ],
    [
        InlineKeyboardButton('🔻Help & Information 🔻', callback_data='help'),
        
    ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply(HOME_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)



@Client.on_message(filters.command("help"))
async def show_help(client, message):
    buttons = [
        [
            InlineKeyboardButton('👥 Group', url='https://t.me/tamilblasterslive'),
            InlineKeyboardButton('movie', url='https://t.me/Trvpn'),
        ],
        [
            InlineKeyboardButton('🙄 Source', url='https://t.me/trvpn'),
            InlineKeyboardButton('Channel 📢', url='https://t.me/trvpn'),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_text(
        HELP,
        reply_markup=reply_markup
        )
