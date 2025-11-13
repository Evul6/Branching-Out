import json


def filter_users_by_name(name):
    """
    Filter users by their name from a JSON file.

    Args:
        name (str): The name to filter users by (case-insensitive).

    Returns:
        list: A list of user dictionaries that match the given name.
              Returns an empty list if no matches are found or if there's an error.
    """
    try:
        with open("users.json", "r") as file:
            users = json.load(file)
        return [user for user in users if user.get("name", "").lower() == name.lower()]
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error: {str(e)}")
        return []


def filter_users_by_email(email):
    """
    Filter users by their email from a JSON file.

    Args:
        email (str): The email address to filter users by (case-insensitive).

    Returns:
        list: A list of user dictionaries that match the given email.
              Returns an empty list if no matches are found or if there's an error.
    """
    try:
        with open("users.json", "r") as file:
            users = json.load(file)
        return [user for user in users if user.get("email", "").lower() == email.lower()]
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error: {str(e)}")
        return []


def filter_users_by_age(age):
    """
    Filter users by their age from a JSON file.

    Args:
        age (str or int): The age to filter users by. Can be a string that can be converted to an integer.

    Returns:
        list: A list of user dictionaries that match the given age.
              Returns an empty list if no matches are found or if there's an error.
    """
    try:
        age = int(age)
        with open("users.json", "r") as file:
            users = json.load(file)
        return [user for user in users if user.get("age") == age]
    except ValueError:
        print("Error: Please enter a valid age (number).")
        return []
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error: {str(e)}")
        return []


def print_users(users):
    """
    Print user information in a readable format.

    Args:
        users (list): A list of user dictionaries to be displayed.
                     If the list is empty, a 'no users found' message is displayed.
    """
    if not users:
        print("No users found matching the criteria.")
    else:
        for user in users:
            print(user)


if __name__ == "__main__":
    filter_option = input("What would you like to filter by? (name/email/age): ").strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        users = filter_users_by_name(name_to_search)
        print_users(users)
    elif filter_option == "email":
        email_to_search = input("Enter an email to filter users: ").strip()
        users = filter_users_by_email(email_to_search)
        print_users(users)
    elif filter_option == "age":
        age_to_search = input("Enter an age to filter users: ").strip()
        users = filter_users_by_age(age_to_search)
        print_users(users)
    else:
        print("Filtering by that option is not supported. Please choose 'name', 'email', or 'age'.")