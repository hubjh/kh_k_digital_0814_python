import argparse
import datetime

VERSION = 0.1

# ASCII ART
print(
    f"""
 ___       ________  ________          ________  ________  _________  _______      
|\\  \\     |\\   __  \\|\\   ____\\        |\\   ___ \\|\\   __  \\|\\___   ___\\\\  ___ \\     
\\ \\  \\    \\ \\  \\|\\  \\ \\  \\___|        \\ \\  \\_|\\ \\ \\  \\|\\  \\|___ \\  \\_\\ \\   __/|    
 \\ \\  \\    \\ \\  \\\\\\  \\ \\  \\  ___       \\ \\  \\ \\\\ \\ \\   __  \\   \\ \\  \\ \\ \\  \\_|/__  
  \\ \\  \\____\\ \\  \\\\\\  \\ \\  \\|\\  \\       \\ \\  \\_\\\\ \\ \\  \\ \\  \\   \\ \\  \\ \\ \\  \\_|\\ \\ 
   \\ \\_______\\ \\_______\\ \\_______\\       \\ \\_______\\ \\__\\ \\__\\   \\ \\__\\ \\ \\_______\\
    \\|_______|\\|_______|\\|_______|        \\|_______|\\|__|\\|__|    \\|__|  \\|_______| v{VERSION}
"""
)

parser = argparse.ArgumentParser(
    description='git commit --amend --date "{datetime}" -m "{message}" 를 간편하게 해주는 프로그램입니다.'
)

parser.add_argument(
    "-dt",
    "--datetime",
    required=True,
    help="날짜와 시간을 입력해야합니다. ex) 2023-09-12T19:00:00",
    type=lambda s: datetime.datetime.strptime(s, "%Y-%m-%dT%H:%M:%S"),
)

parser.add_argument(
    "-g", "--git", required=False, default="./", help="git의 경로를 적어주세요.", type=str
)
parser.add_argument(
    "-m", "--message", required=False, default="", help="commit 메시지를 적어주세요.", type=str
)

args = parser.parse_args()

print(args)


git_date = args.datetime.strftime("%Y-%m-%dT%H:%M:%S")
command_pieces = [f'git commit --amend --date "{git_date}"']

if args.message:
    command_pieces.append(f'-m "{args.message}"')
