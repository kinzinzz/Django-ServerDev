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
