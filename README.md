# E-Drone-Roul

환영합니다! 이 리포지토리는 RokitBrock와 Python을 연결해주는 소스코드가 포함되어있습니다.

## 기본적인 설치

## Windows
### Python 설치
파이썬 웹사이트에 들어가서, Download Windows x86-64 executable installer를 다운받으세요. 그 다음, path에 추가를 선택한다음 설치합니다. 
* [Web](https://www.python.org/downloads/windows/)

### Git 설치하기
깃을 설치합니다.
* [Git Website](https://git-scm.com/)

### Visual Studio Community
vs_community setup을 다운받은 후 실행합니다. 실행한 다음, 위크로드에서 "C++을 사용한 데스크톱 개발"을 체크해준 다음, 설치를 시작합니다. 설치가 완료된 다음, 컴퓨터를 재시작합니다.
* [Download](https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=Community&rel=16)


### Rocit Brock 다운로드
다운로드 받은 후 압축을 풀어서 사용해주세요.
* [32bit](http://robolink.ipdisk.co.kr/publist/HDD1/download/file/RBCoDrone_win32_1.2.3.zip)
* [64bit](http://robolink.ipdisk.co.kr/publist/HDD1/download/file/RBCoDrone_win64_1.2.3.zip)


### git clone 및 환경설정
cmd창에 아래의 명령어를 입력해주세요.
> git clone https://github.com/SDR-Roul/E-Drone-Roul.git Drone -b master

클론이 완료되었을 경우, 그 폴더로 들어가서, intall.bat을 **관리자 권한**으로 실행하여주세요.
배치파일이 설치를 완료한 다음, camera.py에 들어갑니다.
> # 내 PC 카메라 사용
> #self.video = cv2.VideoCapture(0)
        
> # 파일에서 영상을 사용 시
> #self.video = cv2.VideoCapture('abc.mp4')

> # URL 스트리밍에서 가져올시
> #self.video = cv2.VideoCapture('http://0.0.0.0/stream')
사용할 카메라 앞에 있는 #을 삭제해주세요.
### 실행
먼저 run_flask.py를 실행해주세요
> python run_flask.py
그 다음, 


-----

## Linux
### git 설치
아래의 명령어를 입력하세요
> sudo apt update

> sudo apt upgrade

> sudo apt install git

설치가 완료되었다면, 아래의 명령어를 입력해주세요
> git clone https://github.com/SDR-Roul/E-Drone-Roul.git Drone -b master

clone이 완료되었다면 install.sh를 실행해주세요.

### 설정
터미널에서 설치가 완료한 다음, camera.py에 들어갑니다.
> ## 내 PC 카메라 사용
> #self.video = cv2.VideoCapture(0)
        
> ## 파일에서 영상을 사용 시
> #self.video = cv2.VideoCapture('abc.mp4')

> ## URL 스트리밍에서 가져올시
> #self.video = cv2.VideoCapture('http://0.0.0.0/stream')

사용할 카메라 앞에 있는 #을 삭제해주세요.


exit data1
person data2
stats data3