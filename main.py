from aiogram import Bot, Dispatcher

import asyncio

bot = Bot(token='6762147587:AAFpJzl4P1UBEFWQ7BqN821wM4c8tcnZyiQ')
dp = Dispatcher(bot=bot)

async def main():
    from handlers import dp
    try:
        await dp.start_polling()
    finally:
        await bot.session.close()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Bot stopped!')