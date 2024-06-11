
from flask import Flask, jsonify, request
from flask_cors import CORS
import uuid;


app = Flask(__name__)
app.config.from_object(__name__)
CORS(app)

GAMES = [
    {
        "id": uuid.uuid4().hex,
        "title": "2K21",
        "genre": "sports",
        "played": True
    },
    {
        "id": uuid.uuid4().hex,
        "title": "Evil Within",
        "genre": "Horror",
        "played": False
    },
    {
        "id": uuid.uuid4().hex,
        "title": "The Last Of Us",
        "genre": "Survival",
        "played": True
    },
    {
        "id": uuid.uuid4().hex,
        "title": "Days Gone",
        "genre": "Hour/Survival",
        "played": False
    },
    {
        "id": uuid.uuid4().hex,
        "title": "Mario",
        "genre": "Retro",
        "played": True
    },
]

@app.route('/', methods=['GET'])
def greetings():
    return ("Hello world from arooba!")

@app.route('/games', methods=['GET', 'POST'])
def all_games():
    response_object = { "status": "Success"}
    if request.method == 'POST':
        post_data = request.get_json();
        GAMES.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'genre': post_data.get('genre'),
            'played': post_data.get('played'),
        })

        response_object['message'] = 'Game Added'
    else:
        response_object['games'] = GAMES
    return jsonify(response_object)

@app.route('/games/<gameID>', methods=['PUT', 'DELETE'])
def single_game(gameID):
    response_object = { "status": "Success"}
    if request.method == 'PUT':
        post_data = request.get_json();
        remove_game(gameID);
        GAMES.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'genre': post_data.get('genre'),
            'played': post_data.get('played'),
        })

        response_object['message'] = 'Game Update'
    if request.method == 'DELETE':
        remove_game(gameID);
        response_object['message'] = 'Game Deleted'

    return jsonify(response_object)


def remove_game(gameID):
    for game in GAMES:
        if game['id'] == gameID:
            GAMES.remove(game)
            return True
    else:
        return False


if __name__ == "__main__":
    app.run(debug=True)