# Flask Echo Server

<a href="https://github.com/cuttlesoft/flask-echo-server/blob/master/LICENSE">
    <img alt="License: MIT" src="https://black.readthedocs.io/en/stable/_static/license.svg">
</a>
<a href="https://github.com/ambv/black">
    <img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg">
</a>

A simple Flask application that can be used to test HTTP calls. It simply logs
out the request and request data then returns an object with the request
information. Useful for debugging HTTP calls to third-party APIs by making the
same calls to this server or developing applications locally when you don't
want to call real API endpoints.

## Getting Started

These instructions will get you a copy of the project up and running on your
local machine for development.

### Prerequisites

- [Python 3.6+][python]
- [Pipenv][pipenv]

### Install Dependencies

First, install dependencies:

```bash
$ pipenv install
Creating a virtualenv for this project…
...
Virtualenv location: /Users/user/.virtualenvs/flask-echo-server-zyMB51yv
Installing dependencies from Pipfile.lock (8a3288)…
  🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 6/6 — 00:00:04
To activate this project's virtualenv, run the following:
 $ pipenv shell
```

Activate the virtual environment:

```bash
$ pipenv shell
Spawning environment shell (/bin/zsh). Use 'exit' to leave.
(flask-echo-server-zyMB51yv) $
```

### Start the Application

Run the application:

```bash
$ export FLASK_ENV=development; flask run
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: XXX-XXX-XXX
```

## Usage

### Example: POST JSON

```bash
$ curl -d '{"key1":"value1", "key2":"value2"}' -H "Content-Type: application/json" -X POST 127.0.0.1:5000/api/v1/test
{
  "data": "{\"key1\":\"value1\", \"key2\":\"value2\"}",
  "endpoint": "api/v1/test",
  "form": {},
  "json": {
    "key1": "value1",
    "key2": "value2"
  }
}
```

Server log:

```bash
*** Received data at: api/v1/test
data b'{"key1":"value1", "key2":"value2"}'
form ImmutableMultiDict([])
json {'key1': 'value1', 'key2': 'value2'}
```

### Example: POST Form Data

```bash
$ curl -d "param1=value1&param2=value2" -X POST 127.0.0.1:5000/api/v1/test
{
  "data": "",
  "endpoint": "api/v1/test",
  "form": {
    "param1": "value1",
    "param2": "value2"
  },
  "json": null
}
```

Server log:

```bash
*** Received data at: api/v1/test
data b''
form ImmutableMultiDict([('param1', 'value1'), ('param2', 'value2')])
json None
```

## Built With

- [Python][python]
- [Flask][flask]
- [Pipenv][pipenv]

## Contributing

Please read [CONTRIBUTING.md][contributing] for details on our code of conduct.

## Authors

- **[Emily Morehouse][github - emily morehouse]** - [Cuttlesoft][github - cuttlesoft]

## License

This project is licensed under the MIT License - see the [LICENSE][license]
file for details

[contributing]: CONTRIBUTING.md
[flask]: http://flask.pocoo.org/
[github - cuttlesoft]: https://github.com/cuttlesoft
[github - emily morehouse]: https://github.com/emilyemorehouse
[license]: LICENSE
[pipenv]: https://docs.pipenv.org/
[python]: http://python.org/

## Wanna Cuttle?

- 🐙 [Cuttlesoft.com](https://cuttlesoft.com)
- 🐦 [@cuttlesoft](https://twitter.com/cuttlesoft)
- 📩 hello [at] cuttlesoft [dot] com
