import logging
import azure.functions as func
import pyodbc

server = 'verticaldynamix.database.windows.net'
database = 'VerticalDynamix'
username = 'VerticalDynamix'
password = 'Golemw#153'
driver = '{ODBC Driver 17 for SQL Server}'

connection_string = f"Driver={driver};Server={server};Database={database};Uid={username};Pwd={password};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"
conn = pyodbc.connect(connection_string)

# server = os.environ.get('verticaldynamix.database.windows.net')
# database = os.environ.get('VerticalDynamix')
# username = os.environ.get('VerticalDynamix')
# password = os.environ.get('Golemw#153')
# driver = os.environ.get('DB_DRIVER', '{ODBC Driver 17 for SQL Server}')

# connection_string = (
#     f"Driver={driver};Server={server};Database={database};"
#     f"Uid={username};Pwd={password};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"
# )

# conn = pyodbc.connect(connection_string)

def record_model_target_tb():
    cursor = conn.cursor()
    cursor.execute(
        'insert into TargetModel(Map_Style,Target) values(?,?);',
        ('Test', 150)
    )
    conn.commit()

app = func.FunctionApp()

@app.schedule(schedule='0 */1 * * * *', arg_name="myTimer", run_on_startup=True,
              use_monitor=False) 
def timer_trigger01esatusVelik(myTimer: func.TimerRequest) -> None:
    if myTimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function executed.')
    job()


def job():
    # print("Running job...222333")
    record_model_target_tb()



