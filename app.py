from flask import Flask, jsonify, request
import random
import os

app = Flask(__name__)

# List of dad jokes
jokes = [
    "What do you call a fake noodle? An impasta.",
    "I entered 10 puns in a contest to see which would win. No pun in ten did.",
    "Want to hear a pizza joke? Never mind, it's too cheesy.",
    "I wondered why the baseball was getting bigger. Then it hit me.",
    "I waited my whole life to have a 40-year-old joke.",
    "How do you organize a space party? You planet.",
    "I tried to catch some fog earlier. I mist.",
    "When does a joke become a 'dad' joke? When it becomes apparent.",
    "I used to be addicted to soap, but I'm clean now.",
    "I'm not saying I'm a superhero, but have you ever seen me and Superman in the same room together?",
    "What did the lake say to the computer? 'Water way to compute!'",
    "What do you call a bear with no teeth? A gummy bear.",
    "What do you call a fish wearing a bowtie? Sofishticated.",
    "I was wondering why the baseball was getting bigger. Then it hit me.",
    "What do you call a magic dog? A labracadabrador.",
    "What do you call a funny mountain? Hill-arious.",
    "I was wondering why the baseball was getting bigger. Then it hit me.",
    "What do you call a boomerang that doesn't come back? A stick.",
    "I wondered why the baseball was getting bigger. Then it hit me.",
    "What do you get when you cross a snowman with a vampire? Frostbite.",
    "What do you call an alligator in a vest? An investigator.",
    "What do you call a bear with no socks? Bare-footed.",
    "I'm reading a book about anti-gravity. It's impossible to put down.",
    "What do you call a fake noodle? An impasta.",
    "What do you call a bear with no teeth? A gummy bear.",
    "I don't have a solution, but I do have an idea.",
    "Why can't a bike stand up by itself? Because it's two-tired.",
    "My boss asked me who is the bossiest person I know. I told him I'd have to boss over that one.",
    "What do you call a fake noodle? An impasta.",
    "Why can't a leopard hide? Because he's always spotted.",
    "What do you call a pig that does karate? A pork chop.",
    "Why did the tomato turn red? Because it saw the salad dressing!",
    "Why don't scientists trust atoms? Because they make up everything.",
    "What kind of music do planets listen to? Neptunes.",
    "I wondered why the baseball was getting bigger. Then it hit me.",
    "What do you call a fish wearing a bow tie? Sofishticated.",
    "What do you call a fake noodle? An impasta.",
    "What do you call a bear with no socks? Bare-footed.",
    "What do you call a boomerang that doesn't come back? A stick.",
    "I was wondering why the baseball was getting bigger. Then it hit me.",
    "What did the fish say when he swam into a wall? Dam!",
    "What did the bra say to the hat? You go on a head, I'll give these two a lift.",
    "What do you call a dog magician? A labracadabrador.",
    "What do you call a bear with no teeth? A gummy bear.",
    "What do you call a pig that does karate? A pork chop.",
    "What do you call a fake noodle? An impasta."
]

# GET: Retrieve all jokes
@app.route('/jokes', methods=['GET'])
def get_all_jokes():
    return jsonify({"jokes": jokes})


# GET: Retrieve a random joke
@app.route('/joke', methods=['GET'])
def get_joke():
    joke = random.choice(jokes)
    return jsonify({"joke": joke})

# POST: Add a new joke to the list
@app.route('/joke', methods=['POST'])
def add_joke():
    data = request.get_json()
    new_joke = data.get("joke")
    if new_joke:
        jokes.append(new_joke)
        return jsonify({"message": "Joke added!", "joke": new_joke}), 201
    else:
        return jsonify({"error": "No joke provided"}), 400

# PUT: Replace an existing joke with a new one (by index)
@app.route('/joke/<int:joke_id>', methods=['PUT'])
def replace_joke(joke_id):
    if joke_id < 0 or joke_id >= len(jokes):
        return jsonify({"error": "Joke not found"}), 404
    data = request.get_json()
    new_joke = data.get("joke")
    if new_joke:
        jokes[joke_id] = new_joke
        return jsonify({"message": "Joke replaced!", "joke": new_joke}), 200
    else:
        return jsonify({"error": "No joke provided"}), 400

# PATCH: Update part of an existing joke (by index)
@app.route('/joke/<int:joke_id>', methods=['PATCH'])
def update_joke(joke_id):
    if joke_id < 0 or joke_id >= len(jokes):
        return jsonify({"error": "Joke not found"}), 404
    data = request.get_json()
    updated_text = data.get("joke")
    if updated_text:
        jokes[joke_id] = updated_text
        return jsonify({"message": "Joke updated!", "joke": updated_text}), 200
    else:
        return jsonify({"error": "No joke provided"}), 400

# DELETE: Remove a joke by its index
@app.route('/joke/<int:joke_id>', methods=['DELETE'])
def delete_joke(joke_id):
    if joke_id < 0 or joke_id >= len(jokes):
        return jsonify({"error": "Joke not found"}), 404
    deleted_joke = jokes.pop(joke_id)
    return jsonify({"message": "Joke deleted!", "joke": deleted_joke}), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)

