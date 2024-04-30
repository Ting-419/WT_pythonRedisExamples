import redis

# Connect to Redis
redis_client = redis.StrictRedis(host='192.168.0.106', port=6379, db=0)


def set_task(task):
    # Push the task to the end of the 'task_queue' list
    redis_client.rpush('task_queue', task)


if __name__ == "__main__":
    while True:
        task = input("Enter the task: ").strip()
        set_task(task)
