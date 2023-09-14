from datetime import datetime, timedelta
import meta
import pytz
import random
import json
import argparse


def make_rand_datetime(meta, args):
    # start_time = meta.get_start_time_str()
    # end_time = meta.get_end_time_str()
    # # print(meta.get_timezone())
    # args_date = args.get_date()
    # args_datetime = args.get_datetime()
    # args_git = args.get_git()
    # args_rand = args.get_rand()

    # print(args_date, args_datetime, args_git, args_rand)

    if args.get_date():
        # date 이외의 형식을 받으면 오류 리턴
        if validate_date(args.get_date()):
            return make_rand_time(meta, args)

    if args.get_datetime():
        # datetime 이외의 형식을 받으면 오류 리턴
        if validate_datetime(args.get_datetime()):
            return make_datetime(meta, args)


def make_rand_time(meta, args):
    st = pytz.timezone(meta.get_timezone())
    st_str = check_st(meta.get_timezone())

    # json의 시작 시간과 끝 시간의 차이로 랜덤한 시간 추출
    end_time = datetime.strptime(meta.get_end_time_str(), "%H:%M:%S").replace(tzinfo=pytz.utc)
    start_time = datetime.strptime(meta.get_start_time_str(), "%H:%M:%S").replace(tzinfo=pytz.utc)
    second = (end_time - start_time).total_seconds()
    rand_second = random.uniform(0, second)
    delta = timedelta(seconds=rand_second)
    start_time_st = start_time.replace(tzinfo=st)

    # StandardTime 시간 계산
    random_time_st = (start_time_st + delta).strftime('%H:%M:%S')
    datetime_str = args.get_date() + 'T' + random_time_st
    curr_date = datetime.strptime(datetime_str, '%Y-%m-%dT%H:%M:%S')
    curr_date = curr_date.strftime(f'%b %d %a %Y %H:%M:%S {st_str}')
    return curr_date

def make_datetime(meta, args):
    st_str = check_st(meta.get_timezone())
    curr_date = datetime.strptime(args.get_datetime(), '%Y-%m-%dT%H:%M:%S')
    curr_date = curr_date.strftime(f'%b %d %a %Y %H:%M:%S {st_str}')
    return curr_date

# def git_to_ptyz(git_timezone):
#     if git_timezone == "UTC":
#         return 'UTC'
#     if git_timezone == "KST":
#         return 'Asia/Seoul'
def check_st(timezone):
    # UTC (협정 세계시)
    # KST (한국 표준시)
    if timezone == "UTC":
        return 'UTC'
    if timezone == "Asia/Seoul":
        return 'KST'

def validate_date(date_string):
    try:
        datetime.strptime(date_string, '%Y-%m-%d')
        return True  # 날짜 형식이 일치함
    except ValueError:
        return False  # 날짜 형식이 일치하지 않음

def validate_datetime(datetime_string):
    try:
        datetime.strptime(datetime_string, '%Y-%m-%dT%H:%M:%S')
        return True  # 날짜 형식이 일치함
    except ValueError:
        return False  # 날짜 형식이 일치하지 않음