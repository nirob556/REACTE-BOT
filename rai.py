import asyncio
import random
from telethon import TelegramClient, events, Button
from telethon.tl.functions.messages import SendReactionRequest
from telethon.tl.types import ReactionEmoji

api_id = 21589295
api_hash = '06082f4a839cccdd6d147f10ad8a359c'
bot_token = '8108469874:AAFHXbn7cnI7X0JchG_vXUcnkWdReIhQE3o'

client = TelegramClient('VIP_REACT_BOT', api_id, api_hash).start(bot_token=bot_token)

# ✅ শুধুমাত্র valid emoji রাখো
react_emojis = [
    '👍', '👎', '❤️', '🔥', '😂', '😢', '😡', '🤯', '🤔', '👏',
    '🎉', '💯', '😎', '🙏', '😨', '🤡', '🥳', '🤩', '🫶',
    '😴', '💥', '💔', '🤤', '🤮', '🥶', '😵', '😇', '😘', '🗿',
    '👀', '🫠', '😬', '😱', '🤕', '🤐', '🥲', '🥱', '🤓', '🧡',
    '😭', '😁', '😐', '🤬', '🙉', '🌚', '👻', '🍓', '😈',
    '🆒', '🌟', '🌭', '🥰', '🥴', '🏆', '🤗', '🤨', '🍌',
    '👾', '⚡', '🤝'
]

authorized_chats = set()

@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    btn = [Button.url("➕ Add Me To Channel/Group", f"https://t.me/{(await client.get_me()).username}?startgroup=true")]
    await event.respond("👋 Welcome to SPEED_X VIP React Bot!\n\n➤ Add me to your **channel or group** to start reacting automatically to each post. No spam, only reactions. 💎 OWNER : @fakeyou55 ☠️", buttons=btn)

@client.on(events.ChatAction())
async def on_added(event):
    if event.user_added or event.user_joined:
        authorized_chats.add(event.chat_id)
        print(f"✅ Bot added to: {event.chat.title} ({event.chat_id})")

@client.on(events.NewMessage(incoming=True))
async def react_to_post(event):
    chat_id = event.chat_id
    if chat_id in authorized_chats and event.is_channel:
        try:
            emoji = random.choice(react_emojis)
            await client(SendReactionRequest(
                peer=event.peer_id,
                msg_id=event.id,
                reaction=[ReactionEmoji(emoticon=emoji)]
            ))
            print(f"🎯 Reacted with {emoji} in {chat_id}")
        except Exception as e:
            print(f"❌ Failed to react: {e}")

print("🚀 VIP😈 Reaction Bot is running...")
client.run_until_disconnected()
