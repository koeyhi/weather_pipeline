# ✅ 베이스 이미지
FROM apache/airflow:2.8.1

# ✅ 환경 변수
ENV AIRFLOW_HOME=/opt/airflow

# ✅ root로 전환
USER root
RUN apt-get update && \
    apt-get install -y build-essential libssl-dev libffi-dev libpq-dev gcc && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# ✅ DAG, plugins 복사
COPY ./dags ${AIRFLOW_HOME}/dags
COPY ./plugins ${AIRFLOW_HOME}/plugins

# entrypoint.sh 복사하고 실행 권한 부여
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# ✅ 2️⃣ airflow 사용자로 전환
USER airflow

# ✅ requirements 복사 + pip install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ✅ 기본 실행 명령 (웹서버)
ENTRYPOINT ["/entrypoint.sh"]
CMD ["webserver"]
