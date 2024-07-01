from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Ensure the directory for storing subscribers exists
if not os.path.exists('data'):
    os.makedirs('data')

@app.route('/subscribe', methods=['POST'])
def subscribe():
    data = request.get_json()
    first_name = data.get('firstName')
    last_name = data.get('lastName')
    email = data.get('email')

    if not first_name or not last_name or not email:
        return jsonify({'message': 'Missing data'}), 400

    with open('data/subscribers.txt', 'a') as f:
        f.write(f'{first_name} {last_name} {email}\n')

    return jsonify({'message': 'Subscription successful'})

if __name__ == '__main__':
    app.run()


