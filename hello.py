from flask import Flask
# flask: 모듈(module)
# Flask: 클래스(class)
#       - Flask는 애플리케이션을 생성하는데 사용함.

app = Flask(__name__)
# Flask 애플리케이션 객체를 생성
# __name__은 현재 모듈의 이름이고,
# 이 이름을 애플리케이션의 이름으로 사용함.

@app.route('/')
# Flask 애플리케이션의 데코레이션
# 이 데코레이터는 특정 URL(여기서는 /)에 대해
# 해당 URL이 호출될 때 실행될 함수를지정함.
# '/'는 root(처음)URL을 의미하고
#  http://l    print("hello")
def index():
# root URL로 접근할 때 실행될 함수.
# Flask가 이 함수로 실행하여 응답을 생성함.
    return "안녕"

# hello() 함수의 반환 값.
# 문자열 '안녕'을 웹 브라우저에  표시함.
# root URL에 접속하면 웹 브라우저 화면에 '안녕'이 출력됨

if __name__ == "__main__":
# python에서 스크립트가 직접 실행되는 경우에만 실행되고.
# 임포트 될 때는 실행하지않도록 함.
    app.run(debug=True)
# Flask 애플리케이션을 실행함.
# 'deug=True 로 설정하면 디버그 모드가  활성화되어
# 코드 변경 시 서버가 자동으로 재시작됨.