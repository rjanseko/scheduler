beat_schedule = {
    'read_sensor': {
        'task': 'tasks.collect_sensor_data',
        'schedule': 5.0,
    },
    'read_camera': {
        'task': 'tasks.get_snapshot',
        'schedule': 20.0,
    }
}

beat_schedule_filename = '.celerybeat-schedule'

broker_url = 'redis://localhost:6379/0' 
backend_url = 'redis://localhost:6379/1'

enable_utc = True
timezone = 'MST'
