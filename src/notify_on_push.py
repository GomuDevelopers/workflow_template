from bot import send_msg
import os
import time


def send_msg_on_push():
    author = os.environ['GITHUB_AUTHOR']
    repository = os.environ['GITHUB_REPOSITORY']
    link = f"https://github.com/{repository}"
    commits = os.environ['GITHUB_COMMIT']
    count = len(os.environ['GITHBU_PuSH_NUMBER'])
    date = time.ctime()
    text = f"📌 Push effectué par {author} 🧠 \n Date: {date} \n Push n*: {count} \n Commits: {commits[:20]}... \n sentez vous libre l'examiné  {link}"
    send_msg(text)


if __name__ == '__main__':
    send_msg_on_push()
