from airflow import DAG
import datetime
import pendulum
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="dags_bash_operator", # DAG ID와 DAG 파일명은 일치시키는 게 좋음
    schedule="0 0 * * *", # 스케줄링 정보 (분/시/일/월/요일일)
    start_date=pendulum.datetime(2025, 2, 21, tz="Asia/Seoul"), # DAG 시작 날짜 설정 (한국 시간으로 설정 필요)
    catchup=False, # 과거 날짜 DAG 실행 여부 (False로 설정 시 과거 날짜 DAG는 실행되지 않음)
    # dagrun_timeout=datetime.timedelta(minutes=60), -> 60분 동안 실행이 완료되지 않으면 실패 처리
    # tags=["example", "example2"], -> DAG 태그 설정
    # params={"example_key": "example_value"}, -> task에 전달할 파라미터 설정
) as dag:
    bash_t1 = BashOperator(
        task_id="bash_t1", # 객체명과 태스크명은 일치시키는 게 좋음
        bash_command="echo whoami", # echo = print -> whoami를 출력
    )
    bash_t2 = BashOperator(
        task_id="bash_t2", 
        bash_command="echo $HOSTNAME", # wsl 터미널 이름 출력
    )

    bash_t1 >> bash_t2 # 태스크들의 실행 관계를 설정
