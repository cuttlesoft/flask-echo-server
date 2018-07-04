# Flask Echo Server

<a href="https://github.com/cuttlesoft/flask-echo-server/blob/master/LICENSE">
    <img alt="License: MIT" src="https://black.readthedocs.io/en/stable/_static/license.svg">
</a>
<a href="https://github.com/ambv/black">
    <img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg">
</a>

A simple Flask application that can be used to log and return HTTP requests. Useful for debugging API calls to third-party APIs or developing applications locally when you don't want to call real API endpoints.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development.

### Prerequisites

- [Python 3.6+][python]
- [Pipenv][pipenv]

### Installing

First, install dependencies:

```bash
pipenv install
```

Activate the virtual environment:

```bash
pipenv shell
```

## Usage

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

Please read [CONTRIBUTING.md][contributing] for details
on our code of conduct.

## Authors

- **[Emily Morehouse][github - emily morehouse]** - [Cuttlesoft][github - cuttlesoft]

## License

This project is licensed under the MIT License - see the [LICENSE][license] file for details

[contributing]: CONTRIBUTING.md
[flask]: http://flask.pocoo.org/
[github - cuttlesoft]: https://github.com/cuttlesoft
[github - emily morehouse]: https://github.com/emilyemorehouse
[license]: License
[pipenv]: https://docs.pipenv.org/
[python]: http://python.org/
