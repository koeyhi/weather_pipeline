#!/usr/bin/env bash

# 초기화 스크립트
echo "✅ Initializing Airflow DB..."
airflow db init

echo "✅ Creating Airflow Admin User..."
airflow users create \
    --username admin \
    --firstname admin \
    --lastname admin \
    --role Admin \
    --email admin@example.com \
    --password admin  # ✅ 여기 비밀번호 직접 지정!

# 실행 명령 (웹서버 or scheduler)
exec airflow "$@"
