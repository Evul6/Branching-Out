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
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["name"].lower() == name.lower()]
    return filtered_users


def filter_users_by_age(age):
    """
    Filter users by their age from a JSON file.

    Args:
        age (str or int): The age to filter users by. Can be a string that can be converted to an integer.

    Returns:
        list: A list of user dictionaries that match the given age.
              Returns an empty list if no matches are found or if there's an error.
              Handles and reports errors for invalid age input, missing files, and invalid JSON.
    """
    try:
        age = int(age)
        with open("users.json", "r") as file:
            users = json.load(file)
        
        filtered_users = [user for user in users if user.get("age") == age]
        return filtered_users
    except ValueError:
        print("Please enter a valid age (number).")
        return []
    except FileNotFoundError:
        print("Error: users.json file not found.")
        return []
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in users.json")
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
    filter_option = input("What would you like to filter by? (name/age): ").strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        users = filter_users_by_name(name_to_search)
        print_users(users)
    elif filter_option == "age":
        age_to_search = input("Enter an age to filter users: ").strip()
        users = filter_users_by_age(age_to_search)
        print_users(users)
    else:
        print("Filtering by that option is not supported. Please choose 'name' or 'age'.")