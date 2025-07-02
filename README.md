# 🌤️ Weather Data Pipeline with Airflow

## 📌 개요
- OpenWeatherMap API에서 날씨 데이터를 자동으로 수집
- pandas로 CSV 저장
- 간단한 통계 분석
- Slack으로 리포트 알림 전송
- Apache Airflow로 스케줄 관리

---

## 🗂️ 프로젝트 구조
weather_pipeline/
├─ dags/ # Airflow DAG 코드
├─ data/ # 수집된 CSV (깃허브 제외)
├─ plugins/ # 추가 플러그인 (선택)
├─ logs/ # Airflow 로그 (깃허브 제외)
├─ docker-compose.yml # 컨테이너 설정
├─ .env.example # 환경 변수 예시
├─ .gitignore # 깃허브 제외 파일 설정
├─ README.md # 설명서


---

## ⚙️ 사용 방법

### 1️⃣ `.env` 설정
`.env.example`을 복사해서 `.env`를 만들고, 실제 API 키와 Slack 토큰을 입력합니다.

```bash
cp .env.example .env
```

### 2️⃣ Docker 컨테이너 실행
```bash
docker-compose up
```

### 3️⃣ Airflow 웹 UI 접속
브라우저에서 http://localhost:8080 접속
초기 사용자 계정은 docker-compose 실행 후 아래 명령어로 생성:

```bash
docker-compose run airflow-webserver airflow db init
docker-compose run airflow-webserver airflow users create \
  --username admin \
  --firstname admin \
  --lastname admin \
  --role Admin \
  --email admin@example.com
```


### 4️⃣ DAG 활성화 & 실행
Airflow UI에서 weather_pipeline DAG 켜기

▶️ 버튼으로 수동 실행

Slack으로 알림 확인!

### 5️⃣ 데이터 확인
data/weather_data.csv 파일 확인

### 6️⃣ 로그 확인
logs/airflow.log 파일 확인