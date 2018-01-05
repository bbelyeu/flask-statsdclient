Flask-StatsClient
=================

# Installation

To install it, simply run

    pip install flask-statsdclient

# Usage

Import it and wrap app

    from flask import Flask
    from flask_statsdclient import StatsDClient

    app = Flask(__name__)
    statsd = StatsDClient(app)

You may modify the host, port and prefix with ``STATSD_HOST``, ``STATSD_PORT`` and
``STATSD_PREFIX`` options respectively in your Flask app config.

# Development

This project was written and tested with Python 3.6.

On a mac you can use the following commands to get up and running.
``` bash
brew install python3
```
otherwise run
``` bash
brew upgrade python3
```
to make sure you have an up to date version.

This project uses [pipenv](https://docs.pipenv.org) for dependency management. Install pipenv
``` bash
pip3 install pipenv
```

setup the project env
``` base
pipenv install --three --dev
```

create a .env file using this sample
``` bash
export PYTHONPATH=`pwd`
```

now load virtualenv and any .env file
```bash
pipenv shell
```

## Running tests

``` bash
python setup.py test
```

## Before committing any code

We have a pre-commit hook each dev needs to setup.
You can symlink it to run before each commit by changing directory to the repo and running

``` bash
cd .git/hooks
ln -s ../../pre-commit pre-commit
```
