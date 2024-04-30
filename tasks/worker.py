import time

import redis

# Connect to Redis
redis_client = redis.StrictRedis(host='192.168.0.106', port=6379, db=0)


def perform_task(task):
    print(f"Performing task: {task}")
    time.sleep(10)
    print(f"Performed task: {task}")


if __name__ == "__main__":
    while True:
        # Wait for a task from the 'task_queue' channel
        task = redis_client.brpop('task_queue')[1].decode('utf-8')
        perform_task(task)
