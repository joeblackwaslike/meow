# CatAPI
An example of a decoupled flask app.

* Uses FlaskSQLAlchemy, but models are vanilla SQLA and don't depend on Flask
* No global `app` object which is a well known anti-pattern
* Components setup/register themselves
* Empty top level `__init__.py` no `app` object
* app is instantiated in `wsgi.py` which flask is set to autodetect
* CLI commands for db initialization

## Installation
```zsh
$ python -m venv .venv
$ source .venv/bin/activate
$ python -m pip install -r requirements.txt
```

## Init DB
```zsh
$ python -m flask db init
$ python -m flask db load-breeds
```

## Launch Dev Server
```zsh
$ python -m flask run
```

## API Endpoints
### `/breeds`
Get all breeds
```zsh
$ curl http://localhost:5000/breeds/ | python -m json.tool
```

Get one breed
```zsh
$ curl http://localhost:5000/breeds/4 | python -m json.tool
```

### `/temperaments`
Get all temperaments
```zsh
$ curl http://localhost:5000/temperaments/ | python -m json.tool
```

Get one temperament
```zsh
$ curl http://localhost:5000/temperaments/4 | python -m json.tool
```

## Tests
```zsh
$ python -m pytest tests
```