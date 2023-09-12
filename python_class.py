# 생성자는 클래스가 객체로 만들어 질 때 자동으로 호출 되며, 객체의 초기값을 지정 할 수 있습니다.
# 생성자 키워드 : __init__
# self는 자신의 객체를 가리키는 변수
class TV:
    def __init__(self, name, is_on, channel, volume):
        self.name = name
        self.is_on = is_on
        self.channel = channel
        self.volume = volume
    def set_on(self, is_on):
        self.is_on = is_on
    def set_channel(self, cnl):
        self.channel = cnl
    def set_volume(self, vol):
        self.volume = vol
    def get_on(self):
        return self.is_on
    def get_channel(self):
        return self.channel
    def get_volume(self):
        return self.volume
    def view_tv(self):
        power = "OFF", "ON"
        print(f"이름 : {self.name}")
        print(f"전원 : {self.is_on}")
        print(f"채널 : {self.channel}")
        print(f"볼륨 : {self.volume}")