from celery import Celery
import celeryconfig


app = Celery('tasks')
app.config_from_object(celeryconfig)

@app.task
def read_sensor():
    return 'sensor stuff'


@app.task
def read_camera():
    return 'camera picture'


