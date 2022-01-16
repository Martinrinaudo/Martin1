# winbot_test.py
import winbot
bot = winbot.MouseBot()


print(dir(bot))
poscursor = bot.getPosition()
bot.move(145, 43)
bot.click(1)
bot.scroll(vertical=-10)
