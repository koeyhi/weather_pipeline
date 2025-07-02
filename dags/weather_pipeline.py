from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import requests
import pandas as pd
from slack_sdk import WebClient
import os


# ==============================
# 설정값
# ==============================
API_KEY = os.getenv('OPENWEATHERMAP_API_KEY')
CITY = 'Daejeon'
SLACK_TOKEN = os.getenv('SLACK_TOKEN')
SLACK_CHANNEL = os.getenv('SLACK_CHANNEL')

# ==============================
# 함수들
# ==============================

def fetch_weather():
    url = f'https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric'
    res = requests.get(url)
    data = res.json()

    weather = {
        'datetime': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'city': CITY,
        'temp': data['main']['temp'],
        'humidity': data['main']['humidity'],
        'weather': data['weather'][0]['main']
    }

    df = pd.DataFrame([weather])
    df.to_csv('/opt/airflow/data/weather_data.csv', mode='a', header=False, index=False)
    print(f"✅ 데이터 저장: {weather}")

def analyze_weather():
    df = pd.read_csv('/opt/airflow/data/weather_data.csv', names=['datetime', 'city', 'temp', 'humidity', 'weather'])
    avg_temp = df['temp'].mean()
    rainy_days = df[df['weather'] == 'Rain'].shape[0]
    summary = f"🌤️ 평균 기온: {avg_temp:.2f}°C, 비가 온 날: {rainy_days}일"
    print(summary)

    # Slack 알림 보내기
    client = WebClient(token=SLACK_TOKEN)
    client.chat_postMessage(channel=SLACK_CHANNEL, text=summary)
    print("✅ Slack 알림 발송 완료")

# ==============================
# DAG 정의
# ==============================

default_args = {
    'owner': 'koeyhi',
    'depends_on_past': False,
    'start_date': datetime(2025, 7, 2),
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

with DAG(
    dag_id='weather_pipeline',
    default_args=default_args,
    schedule_interval='0 9 * * *',  # 매일 오전 9시
    catchup=False,
) as dag:

    t1 = PythonOperator(
        task_id='fetch_weather',
        python_callable=fetch_weather,
    )

    t2 = PythonOperator(
        task_id='analyze_weather',
        python_callable=analyze_weather,
    )

    t1 >> t2
