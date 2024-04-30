import redis

# Connect to Redis
redis_client = redis.StrictRedis(host='192.168.0.106', port=6379, db=0)


def set_user_online(username):
    redis_client.hset('online_users', username, 'online')
    redis_client.publish('user_status', username)


def set_user_offline(username):
    redis_client.hdel('online_users', username)
    redis_client.publish('user_status', username)


if __name__ == "__main__":
    while True:
        action = input("Enter 'online' to go online, 'offline' to go offline, or 'exit' to quit: ").strip().lower()

        if action == 'exit':
            break
        elif action == 'online':
            username = input("Enter your username: ").strip()
            set_user_online(username)
        elif action == 'offline':
            username = input("Enter your username: ").strip()
            set_user_offline(username)
        else:
            print("Invalid action. Please enter 'online', 'offline', or 'exit'.")
