from bot import send_msg
import os
import time


def send_msg_on_PR():
    author = os.environ['GITHUB_AUTHOR']
    link = os.environ['GITHUB_PR_LINK']
    title = os.environ['GITHUB_PR_TITLE']
    body = os.environ['GITHUB_PR_BODY']

    repository = os.environ['GITHUB_REPOSITORY']
    date = time.ctime()
    text = f"📌 Pull Request  effectué par {author} 🧠 \n Date: {date}  \n Depôt: {repository} \n Title :{title}\n Comments: {body[:30]} ... \n sentez vous libre l'examiné  {link}"
    send_msg(text)


if __name__ == '__main__':
    send_msg_on_PR()
