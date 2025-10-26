# Python 베이스 이미지 선택
FROM python:3.14-slim-bookworm

# 작업 디렉토리 설정
WORKDIR /app

# requirements.txt 먼저 복사 (캐싱 최적화)
COPY requirements.txt .

# 필요한 패키지 설치
RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션 파일 복사
COPY . . 

# Streamlit 포트 노출
EXPOSE 8501

# Streamlit 실행
ENTRYPOINT ["streamlit","run","app.py"]