from . import app, bot
from .utils import lookup_zodiac, lookup_chinese_zodiac, generate_meme


@bot.message_handler(regexp=r'^/about$')
def help(message):
    app.logger.debug("'about' command detected")
    about_text = (
        'CSUIBot v0.0.1\n\n'
        'Dari Fasilkom, oleh Fasilkom, untuk Fasilkom!'
    )
    bot.reply_to(message, about_text)


@bot.message_handler(regexp=r'^/zodiac \d{4}\-\d{2}\-\d{2}$')
def zodiac(message):
    app.logger.debug("'zodiac' command detected")
    _, date_str = message.text.split(' ')
    _, month, day = parse_date(date_str)
    app.logger.debug('month = {}, day = {}'.format(month, day))

    try:
        zodiac = lookup_zodiac(month, day)
    except ValueError:
        bot.reply_to(message, 'Month or day is invalid')
    else:
        bot.reply_to(message, zodiac)


@bot.message_handler(regexp=r'^/shio \d{4}\-\d{2}\-\d{2}$')
def shio(message):
    app.logger.debug("'shio' command detected")
    _, date_str = message.text.split(' ')
    year, _, _ = parse_date(date_str)
    app.logger.debug('year = {}'.format(year))

    try:
        zodiac = lookup_chinese_zodiac(year)
    except ValueError:
        bot.reply_to(message, 'Year is invalid')
    else:
        bot.reply_to(message, zodiac)


@bot.message_handler(regexp=r'^/notes view')
def view(message):
    bot.reply_to(message, 'Wkwkwkw')


@bot.message_handler(regexp=r'^/notes (.*)')
def write(message):
    bot.reply_to(message, 'Wkwkwkw')


def parse_date(text):
    return tuple(map(int, text.split('-')))


@bot.message_handler(regexp=r'^/meme (<.+>) (<.+>)$')
def meme(message):
    app.logger.debug("'meme' command detected")

    try:
        top, bottom = message.text[7:-1].split('> <')
        app.logger.debug("text0 = {}\ntext1 = {}".format(top, bottom))
        meme = generate_meme(top, bottom)
    except ValueError as e:
        bot.reply_to(message, 'Invalid meme command format, ' + str(e))
    else:
        bot.reply_to(message, meme)
