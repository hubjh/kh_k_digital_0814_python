# 플라스크 : 웹개발을 위한 모듈
# Django는 매우 다양한 기능을 제공하는 웹 개발 프레임 워크이고,
# Flask는 웹 애플리케이션 개발을 위한 간결하고 유연한 도구입니다.
# Flask는 마이크로 프레임워크로 분류되며, 작고 간단한 핵심 기능을 제공하면서도 확장성과 유연성을 갖추고 있습니다.

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, Flaks !!!!!"

if __name__ == '__main__':
    app.run()