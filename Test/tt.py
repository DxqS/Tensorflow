from wxpy import *

# bot = Bot()
# my_friend = bot.chats()
# # print(my_friend)
# # my_friend.send('Hello WeChat!')
#
#
# @bot.register()
# def print_others(msg):
#     print(msg)
#
#
# @bot.register(my_friend)
# def reply_my_friend(msg):
#     return 'hello,{},My Boss is busy now,please call him later.'.format(msg.sender.name)
bot = Bot()
my_friend = bot.chats().search(name="")
xiaoi = XiaoI('xv14dA0oeES7', 'xMZavtxt0TEx5G6qyWqe')


@bot.register(my_friend)
def reply_my_friend(msg):
    xiaoi.do_reply(msg)


embed()
