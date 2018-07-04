import json
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def hello_world(path):
    print(f"*** Received data at: {path}")
    print("data", request.data)
    print("form", request.form)
    print("json", request.get_json())

    return jsonify(
        {
            "endpoint": path,
            "data": json.dumps(request.data.decode("utf-8")),
            "form": request.form,
            "json": request.get_json(),
        }
    )


if __name__ == "__main__":
    app.run()
