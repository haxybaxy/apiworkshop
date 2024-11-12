import requests
import json

API_URL = "http://127.0.0.1:5000/joke"


def get_random_joke():
    response = requests.get(API_URL)
    if response.status_code == 200:
        joke = response.json().get("joke")
        print(f"Random joke: {joke}")
    else:
        print("Failed to retrieve a joke.")


def add_new_joke(new_joke):
    response = requests.post(API_URL, json={"joke": new_joke})
    if response.status_code == 201:
        print(f"Added joke: {response.json().get('joke')}")
    else:
        print("Failed to add the joke.")


def replace_joke(joke_id, new_joke):
    response = requests.put(f"{API_URL}/{joke_id}", json={"joke": new_joke})
    if response.status_code == 200:
        print(f"Replaced joke at index {joke_id}: {response.json().get('joke')}")
    else:
        print("Failed to replace the joke. Make sure the ID is correct.")


def update_joke(joke_id, updated_text):
    response = requests.patch(f"{API_URL}/{joke_id}", json={"joke": updated_text})
    if response.status_code == 200:
        print(f"Updated joke at index {joke_id}: {response.json().get('joke')}")
    else:
        print("Failed to update the joke. Make sure the ID is correct.")


def delete_joke(joke_id):
    response = requests.delete(f"{API_URL}/{joke_id}")
    if response.status_code == 200:
        print(f"Deleted joke: {response.json().get('joke')}")
    else:
        print("Failed to delete the joke. Make sure the ID is correct.")

def get_all_jokes():
    response = requests.get(f"{API_URL}s")
    if response.status_code == 200:
        jokes = response.json().get("jokes")
        print("All jokes:")
        for idx, joke in enumerate(jokes):
            print(f"{idx}: {joke}")
    else:
        print("Failed to retrieve jokes.")

if __name__ == '__main__':
    # Get a random joke
    print("GET /joke:")
    get_random_joke()

    # Get all jokes
    print("\nGET /jokes:")
    get_all_jokes()

    # Add a new joke
    print("\nPOST /joke:")
    new_joke_text = "Why did the scarecrow win an award? Because he was outstanding in his field!"
    add_new_joke(new_joke_text)

    # Replace an existing joke at index 0
    print("\nPUT /joke/0:")
    replace_joke(0, "What time did the man go to the dentist? Tooth hurt-y.")

    # Partially update an existing joke at index 1
    print("\nPATCH /joke/1:")
    update_joke(1, "I used to play piano by ear, but now I use my hands.")

    # Delete a joke at index 2
    print("\nDELETE /joke/2:")
    delete_joke(2)
