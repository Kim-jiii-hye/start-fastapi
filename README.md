# FastAPI 웹 애플리케이션

## 기술 스택

- Python 3.13+
- FastAPI
- Docker & Docker Compose
- Nginx
- Gunicorn

## 프로젝트 구조

```
.
├── app (FastAPI 코드)
│   ├── main.py
│   └── ...
├── Dockerfile
├── Dockerfile.dev (개발 환경용 Dockerfile)
├── docker-compose.yml
├── nginx.conf
├── requirements.txt
└── README.md
```

## 실행 방법

1. 프로젝트 디렉토리로 이동
2. `docker-compose up -d` 명령 실행
3. 브라우저에서 `http://localhost:3000`으로 접속

## 개발 환경 실행 방법

1. 프로젝트 디렉토리로 이동
2. `docker build -f Dockerfile.dev -t fastapi-dev .` 명령 실행
3. 브라우저에서 `http://localhost:8000`으로 접속
4. `docker run -p 8000:8000 -v $(pwd):/app fastapi-dev`