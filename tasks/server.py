import redis

# Connect to Redis
redis_client = redis.StrictRedis(host='192.168.0.106', port=6379, db=0)


def assign_task_to_worker(task):
    # Publish the task to the 'task_queue' channel
    redis_client.publish('task_queue', task)


def listen_for_tasks():
    pubsub = redis_client.pubsub()
    pubsub.subscribe('task_queue')

    for message in pubsub.listen():
        if message['type'] == 'message':
            task = message['data'].decode('utf-8')
            print(f"Assigned task: {task}")


if __name__ == "__main__":
    listen_for_tasks()
