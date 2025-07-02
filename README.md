# 🌤️ Weather Data Pipeline with Apache Airflow

## 📌 프로젝트 개요

- **OpenWeatherMap API**로 실시간 날씨 데이터 수집
- **pandas**로 CSV 저장
- 간단한 통계 분석 후 **Slack 알림 발송**
- **Apache Airflow**로 스케줄링 & DAG 관리
- **Docker Compose**로 로컬 컨테이너 환경 구성
- `.env`로 API 키 등 민감 정보 관리
- `Dockerfile` + `entrypoint.sh`로 빌드 & 초기화 자동화

---

## 🗂️ 폴더 구조

```bash
weather_pipeline/
├─ dags/ # Airflow DAG 코드
├─ plugins/ # (필요하면)
├─ data/ # 수집된 데이터 CSV (깃허브 제외)
├─ logs/ # Airflow 로그 (깃허브 제외)
├─ Dockerfile # Airflow 빌드 설정
├─ docker-compose.yml # 멀티 컨테이너 설정
├─ requirements.txt # Python 패키지 버전 관리
├─ entrypoint.sh # 초기화 + 사용자 생성 자동화 스크립트
├─ .env.example # 환경 변수 샘플 (API 키, 토큰)
├─ .gitignore # 민감정보 제외
├─ README.md # 프로젝트 설명서
```

---

## ⚙️ 주요 기술 스택

- **Python** (`pandas`, `requests`, `slack_sdk`, `dotenv`)
- **Apache Airflow**
- **Docker & Docker Compose**
- **PostgreSQL**
- **Slack Bot**

---

## ✅ 사전 준비

1️⃣ 깃 클론 후 `.env.example` 복사

```bash
cp .env.example .env
```

.env에 본인 OpenWeatherMap API Key, Slack Bot Token, 채널 이름 입력!
```bash
OPENWEATHERMAP_API_KEY=your_api_key
SLACK_TOKEN=your_slack_token
SLACK_CHANNEL=#your-channel
```

2️⃣ Slack에서 봇 생성 + 채널 초대

Slack App 만들기 → Bot Token 발급
채널에 @봇이름 초대

## ✅ 실행 방법

### 1️⃣ 컨테이너 빌드

```bash
docker-compose build
```

### 2️⃣ DB 초기화 & Admin 사용자 자동 생성

entrypoint.sh에서 자동 실행되므로 별도 db init/users create 필요 없음!

### 3️⃣ 컨테이너 실행 (백그라운드 모드)

```bash
docker-compose up -d
```

### 4️⃣ Airflow UI 접속

http://localhost:8080

ID: admin
PW: admin (entrypoint.sh에 고정)

### 5️⃣ DAG 실행

UI에서 weather_pipeline DAG ON

▶️ 버튼 클릭 → 실행!

Slack 채널에 알림 수신 확인

## 🔑 자주 쓰는 명령어

| 내용           | 명령어                                          |
| ------------ | -------------------------------------------- |
| 컨테이너 중지      | `docker-compose down`                        |
| 볼륨 포함 완전 중지  | `docker-compose down -v`                     |
| 실행 로그 보기     | `docker-compose logs -f`                     |
| webserver 접속 | `docker exec -it <webserver-container> bash` |

## ⚡️ 주요 기능

✅ 실시간 날씨 수집
✅ CSV 저장
✅ pandas 분석
✅ Slack 알림
✅ Airflow 스케줄 관리
✅ Docker + .env 안전 관리
✅ entrypoint로 자동 초기화 & 계정 생성

## 🔒 보안

.env는 절대 깃허브에 커밋하지 않음
.env.example만 제공하여 키 구조만 공유
requirements.txt로 라이브러리 버전 통일

## 🗝️ 확장 아이디어

S3 업로드 → 데이터 적재 자동화
BigQuery / Snowflake 연동
Streamlit 대시보드
Airflow XCom으로 Task간 데이터 전달 고도화