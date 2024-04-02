from bot import send_msg
import os
import time


def send_msg_on_push():
    author = os.environ['GITHUB_AUTHOR']
    repository = os.environ['GITHUB_REPOSITORY']
    link = f"https://github.com/{repository}"
    date = time.ctime()
    text = f"Push 🗞 Made by *{author}* on {date} \n\n Feel free to review it at {link}"
    send_msg(text)


if __name__ == '__main__':
    send_msg_on_push()
