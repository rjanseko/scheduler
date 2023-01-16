beat_schedule = {
    'sensor_5s': {
        'task': 'tasks.read_sensor',
        'schedule': 5.0,
    },
    'camera_15s': {
        'task': 'tasks.read_camera',
        'schedule': 15.0,
    }
}

broker_url = 'redis://broker:6379/0' 
result_backend = 'redis://broker:6379/1'
