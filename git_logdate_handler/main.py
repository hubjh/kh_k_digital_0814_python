from method import *
from meta import *
import json
import argparse


with open('config.json', 'r') as f:
    json_data = json.load(f)


time_zone = json_data['setting']['time_zone']
commit_message = json_data['setting']['default']['commit_message']
git_dir = json_data['setting']['default']['git_dir']
default_time = json_data['setting']['default']['time']
start_time_str = json_data['setting']['default']['random_time']["start_time"]
end_time_str = json_data['setting']['default']['random_time']["end_time"]


parser = argparse.ArgumentParser(description='git commit --amend --date "{datetime}" -m "{message}" 를 간편하게 해주는 프로그램입니다.')
group = parser.add_mutually_exclusive_group()
group.add_argument('-d', '--date', required=False, help='날짜를 입력해야합니다. ex) 2023-09-12')
group.add_argument('-dt', '--datetime', required=False, help='날짜와 시간을 입력해야합니다. ex) 2023-09-12T19:00:00')
parser.add_argument('-r', '--random', required=False, action='store_true', help='랜덤하게 시간대를 생성하시겠습니까?')
parser.add_argument('-g', '--git', required=False, help='git의 경로를 적어주세요.')
parser.add_argument('-m', '--message', required=False, help='commit 메시지를 적어주세요.')

args = parser.parse_args()
meta_data = MetaData(time_zone, commit_message, git_dir, default_time, start_time_str, end_time_str)


# args_meta_data = ArgsMetaData(args.date, args.datetime, args.git, args.random, args.message)

# print(args.random) # 랜덤 옵션을 넣으면 true false 중 하나 반환
# print(args.date)    # date , None
# print(args.git)    # git_dir  , None
# print(args.datetime)    # datetime  , None

print(make_git_command(meta_data, args_meta_data))








