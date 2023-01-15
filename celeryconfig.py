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

broker_url = 'redis://broker:6379/0' 
backend_url = 'redis://broker:6379/1'



