# Django Server Dev

- 서버 개발자가 하는일
  - API 개발
  - DB 테이블 생성 및 수정
  - 배치 프로그램 개발

- 서버 개발환경 세팅

  - 대기업, 금융권은 자체 IDC을 구축해놓고 자신들만의 프레임워크를 사용
  - 또한 대기업같은 경우 자체적으로 인프라 구축을 위한팀이 따로 존재
  - AWS EC2를 이용해 Django를 서버에 올리고 middleware인 nginx를 사용
  - DB는 mysql, docker를 이용해 같은 EC2 서버에 올릴 예정
  - 추가사항 : redis 사용 

- ubuntu 명령어

  ```
  sudo apt update
  sudo apt install python3
  sudo apt install python3-pip
  sudo apt install virtualenv
  pip install virtualenv
  ```

- 인바운드 규칙 편집 

  - SSH이외에 사용자 지정 TCP를 추가해 포트범위 8000, 위치설정하고 서버를 띄운다.
  - Django settings.py에서 ALLOWED_HOST 설정
  - 인스턴스IP 주소:8000 정상적으로 실행 확인

>  **AWS에서 EC2 인스턴스**를 생성하였고, 로컬 환경에서 **Django 프로젝트를 만들어 Github에 연동 그리고 **AWS EC2에서 git을 활용해 우리가 만든 Django 프로젝트를 불러와 실행**

- uWSGI 설치
  - uwsgi --http :8000 --module server_dev.wsgi
  - worker 1: 프로세서 1개
  - client > url 요청 > uwsgi > django >uwsgi > client
  - etc/uwsgi/sites sudo vi server_dev
  - ps -ef |grep uws(실행여부)
  - tail -f uwsgi.log(파일 추적)
- Nginx
  - sudo apt-get install Nginx
  - niginx 설정
  - sudo systemctl start nginx
  - ps -ef |grep nginx
- docker
  - django image 생성
  - nginx image 생성
  - docker compose
- API(client의 요청에 응답)
  - DRF를 이용
  - make_password 로 암호 hash화
  - 데이터를 어떻게 보내는게 효율적?
  - client의 "JSON데이터" 요청 => 데이터를 효율적으로 mapping = JSON 데이터를 Serializer 
  - 추가 column 은 serializers에 fields에 추가하면 된다.
  - serializer 사용하는 이유 : 많은 데이터를 한번에 조회 할 수 있다.
- ToDolist 만들기
  - 서버 개발자
    -  데이터를 어디에 저장할 것인가?(file, sam file, memory, DB)
    - 테이블은 어떻게 만들것인가?(fields, ORM)