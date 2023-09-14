from datetime import datetime, timedelta
import pytz
import random



def make_git_datetime_command_str(meta, args):
    # start_time = meta.get_start_time_str()
    # end_time = meta.get_end_time_str()
    # # print(meta.get_timezone())
    args_date = args.get_date()
    args_datetime = args.get_datetime()
    args_git = args.get_git()
    # args_deft = args.get_default_time()
    args_rand = args.get_rand()

    # print(args_git,"g - r", args_rand)


    # if args.get_git():
        # 깃 위치


    if args.get_date():
        # date 이외의 형식을 받으면 오류 리턴
        if validate_date(args.get_date()):
            print(make_rand_time(meta, args))
            return make_rand_time(meta, args)


    if args.get_datetime():
        # datetime 이외의 형식을 받으면 오류 리턴
        if validate_datetime(args.get_datetime()):
            print(make_datetime(meta, args.get_datetime()))
            return make_datetime(meta, args.get_datetime())

def make_rand_time(meta, args):
    if args.get_rand():
        st = pytz.timezone(git_to_ptyz(meta.get_timezone()))

        # json의 시작 시간과 끝 시간의 차이로 랜덤한 시간 추출
        end_time = datetime.strptime(meta.get_end_time_str(), "%H:%M:%S").replace(tzinfo=pytz.utc)
        start_time = datetime.strptime(meta.get_start_time_str(), "%H:%M:%S").replace(tzinfo=pytz.utc)
        second = (end_time - start_time).total_seconds()
        rand_second = random.uniform(0, second)
        delta = timedelta(seconds=rand_second)
        start_time_st = start_time.replace(tzinfo=st)

        # StandardTime 시간 계산
        return build_datetime_from_time_str(args, meta, (start_time_st + delta))

    else:
        default_time_str = datetime.strptime(meta.get_default_time(), '%H:%M:%S')
        return build_datetime_from_time_str(args, meta, default_time_str)

def build_datetime_from_time_str(args, meta, time_str):
    random_time_st = (time_str).strftime('%H:%M:%S')
    datetime_str = args.get_date() + 'T' + random_time_st
    return make_datetime(meta, datetime_str)

def make_datetime(meta, datetime_str):
    st_str = check_st(meta.get_timezone())
    curr_date = datetime.strptime(datetime_str, '%Y-%m-%dT%H:%M:%S')
    curr_date = curr_date.strftime(f'%b %d %a %Y %H:%M:%S {st_str}')
    return curr_date

# KST 를 입력 받으면 ptyz의 매개변수로 Asia/Seoul를 줄 수 있게 하는 함수
def git_to_ptyz(git_timezone):
    if git_timezone == "UTC":
        return 'UTC'
    if git_timezone == "KST":
        return 'Asia/Seoul'
def check_st(timezone):
    # UTC (협정 세계시)
    # KST (한국 표준시)
    if timezone == "UTC":
        return 'UTC'
    if timezone == "KST":
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

def make_git_command():
    pass
