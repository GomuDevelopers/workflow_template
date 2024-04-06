from bot import send_msg
import os
import time


def send_msg_on_push():
    author = os.environ['GITHUB_AUTHOR']
    repository = os.environ['GITHUB_REPOSITORY']
    link = f"https://github.com/{repository}/tree/dev"
    commits = os.environ['GITHUB_COMMIT']
    # count = len(os.environ['GITHUB_PuSH_NUMBER'])
    date = time.ctime()
    text = f"📌 Push effectué  par {author} 🧠 \n Date: {date}  \n Depôt: {repository} \n Commits: {commits[:30]} ... \n sentez vous libre l'examiné  {link}"
    send_msg(text)


if __name__ == '__main__':
    send_msg_on_push()
