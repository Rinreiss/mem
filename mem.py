import telebot
import urllib

bot = telebot.TeleBot("1812853434:AAHvXai47j1k3MdKkZFCLYIgjtEAU-jOYTM")
my_url='https://sun9-24.userapi.com/impg/7wlVbB3zBQZATnQ2U-cWwWeh8TDm7tOHWGdciQ/RkaUmVU9C2Y.jpg?size=480x315&quality=96&sign=e0018b8dd328fb60223d1c005857b811&type=album'

f = open('out.jpg','wb')
f.write(urllib.request.urlopen(my_url).read())
f.close()


@bot.message_handler(func=lambda message: True)
def get_sms(message):
        img = open('out.jpg', 'rb')
        bot.send_photo(message.from_user.id, img, None)
        img.close()

bot.polling()
