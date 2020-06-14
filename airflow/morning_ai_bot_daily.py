import sys
from package.morning_ai_bot_common import *
from package.morning_ai_bot_config import *

dag = DAG(
    'morning_ai_bot_daily_v0.0',
    default_args=common_args,
    description='call funtion mornin_ai_bot',
    schedule_interval="05 22 *  *  *",
)

task1 = PythonOperator(
    task_id='morning_ai_bot',
    python_callable=exec_functions,
    provide_context=True,
    op_kwargs={
        "url": "https://us-central1-{}.cloudfunctions.net/morning_ai_bot".format(gcp_project),
        "token": sandbox_token
    },
    dag=dag,
)

task1 # >> task2