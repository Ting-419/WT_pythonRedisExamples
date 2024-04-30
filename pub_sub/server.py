import redis

# Connect to Redis
redis_client = redis.StrictRedis(host='192.168.0.106', port=6379, db=0)


def get_online_users():
    return redis_client.hkeys('online_users')


def listen_for_online_users():
    pubsub = redis_client.pubsub()
    pubsub.subscribe('user_status')

    for message in pubsub.listen():
        if message['type'] == 'message':
            online_users = get_online_users()
            print("Online users:", [username.decode('utf-8') for username in online_users])


if __name__ == "__main__":
    listen_for_online_users()
