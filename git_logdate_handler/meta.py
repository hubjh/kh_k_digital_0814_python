class MetaData:
    def __init__(self, timezone, commit_message, git_dir, default_time, start_time_str, end_time_str):
        self.timezone = timezone
        self.commit_message = commit_message
        self.git_dir = git_dir
        self.default_time = default_time
        self.start_time_str = start_time_str
        self.end_time_str = end_time_str

    def get_timezone(self):
        return self.timezone

    def get_commit_message(self):
        return self.commit_message

    def get_git_dir(self):
        return self.git_dir

    def get_default_time(self):
        return self.default_time

    def get_start_time_str(self):
        return self.start_time_str

    def get_end_time_str(self):
        return self.end_time_str


class ArgsMetaData:
    def __init__(self, date, datetime, git, rand):
        self.date = date
        self.datetime = datetime
        self.git = git
        self.rand = rand

    def get_date(self):
        return self.date

    def get_datetime(self):
        return self.datetime

    def get_git(self):
        return self.git

    def get_rand(self):
        return self.rand

