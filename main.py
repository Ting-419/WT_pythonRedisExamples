import json

import redis

# Connect to Redis
redis_client = redis.StrictRedis(host='192.168.0.106', port=6379, db=0)


def create_poll():
    question = input("Enter the poll question: ")
    choices = input("Enter the choices separated by commas: ").split(",")

    poll_data = {f"choice_{i}": {"text": choice.strip(), "votes": 0} for i, choice in enumerate(choices)}
    serialized_poll_data = {key: json.dumps(value) for key, value in poll_data.items()}

    redis_client.hmset(question, serialized_poll_data)
    print("Poll created successfully.")


def vote_in_poll():
    question = input("Enter the poll question: ")
    choices = redis_client.hkeys(question)

    if not choices:
        print("Poll not found.")
        return

    print("\nChoices:")
    for i, choice in enumerate(choices):
        print(f"{i + 1}. {choice.decode('utf-8')}")

    choice_num = input("Enter your choice number (0 to return to main menu): ")

    if choice_num == '0':
        return
    elif choice_num.isdigit() and 0 < int(choice_num) <= len(choices):
        vote(question, choices[int(choice_num) - 1].decode('utf-8'))
    else:
        print("Invalid choice number. Please enter a valid choice.")


def vote(poll_question, choice):
    # Retrieve the current vote count as a string
    poll_dict = json.loads(redis_client.hget(poll_question, choice))

    # Increment the vote count in Python
    poll_dict["votes"] = int(poll_dict["votes"]) + 1

    # Store the updated vote count back in Redis as a JSON-encoded string
    redis_client.hset(poll_question, choice, json.dumps(poll_dict))

    print("Vote counted successfully.")


def show_poll_results():
    question = input("Enter the poll question: ")
    poll_data = redis_client.hgetall(question)

    if not poll_data:
        print("No results found for the poll.")
        return

    total_votes = sum(int(json.loads(poll)["votes"]) for poll in poll_data.values())
    print("Results for the poll:")
    for choice, poll in poll_data.items():
        choice_text = choice.decode('utf-8')
        poll_dict = json.loads(poll)
        votes = int(poll_dict["votes"])
        percentage = (votes / total_votes) * 100 if total_votes > 0 else 0
        print(f"{poll_dict['text']}: {votes} votes ({percentage:.2f}%)")


def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Create a poll")
        print("2. Vote in a poll")
        print("3. See poll results")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            create_poll()
        elif choice == '2':
            vote_in_poll()
        elif choice == '3':
            show_poll_results()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main_menu()
