from flask import Flask, request, jsonify
from flask_coney import Coney

app = Flask(__name__)
app.config["CONEY_BROKER_URI"] = "amqp://user:password@rabbitmq"
coney = Coney(app)

processed_data = []


@app.route("/processed", methods=["GET"])
def processed():
    return jsonify(processed_data)


@coney.queue(queue_name="process")
def process_queue(ch, method, params, body):
    # do something with body
    processed_body = body
    processed_data.append(processed)

