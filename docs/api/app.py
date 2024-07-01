import flask

app = flask.Flask(__name__)

@app.route('/subscribe', methods=['POST'])
def subscribe():
    data = flask.request.get_json()
    first_name = data.get('firstName')
    last_name = data.get('lastName')
    email = data.get('email')

    if not first_name or not last_name or not email:
        return flask.jsonify({'message': 'Missing data'}), 400

    with open('subscribers.txt', 'a') as f:
        f.write(f'{first_name} {last_name} {email}\n')

    return flask.jsonify({'message': 'Subscription successful'})

if __name__ == '__main__':
    app.run(debug=True)
