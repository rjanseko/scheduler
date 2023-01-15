from celery import Celery
import celeryconfig


app = Celery('tasks')
app.config_from_object(celeryconfig)

@app.task
def collect_sensor_data():
    return {'yo': 'man'}


@app.task
def get_snapshot():
    return 'camera picture'




