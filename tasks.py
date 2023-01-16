from celery import Celery


app = Celery('tasks')

@app.task
def read_sensor():
    return 'sensor'

@app.task
def read_camera():
    return 'camera'


app.conf.beat_schedule = {
    'sensor_5s': {
        'task': 'tasks.read_sensor',
        'schedule': 5.0,
    },
    'camera_15s': {
        'task': 'tasks.read_camera',
        'schedule': 15.0,
    }
}

