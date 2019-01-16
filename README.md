# Flask-StatsClient

[![Build Status](https://travis-ci.org/bbelyeu/flask-statsdclient.svg?branch=master)](https://travis-ci.org/bbelyeu/flask-statsdclient)
[![Coverage Status](https://coveralls.io/repos/github/bbelyeu/flask-statsdclient/badge.svg?branch=master)](https://coveralls.io/github/bbelyeu/flask-statsdclient?branch=master)

## Requirements

This project requires Python 3.5+ and Flask 0.12. Test builds in Travis CI test 3.5 & 3.6.

## Installation

To install it, simply run

    pip install flask-statsdclient

If you're using Datadog(https://www.datadoghq.com/) for your metric collection, you can enable
the additional functionality of
dogstatsd(http://datadogpy.readthedocs.io/en/latest/#datadog-dogstatsd-module)
by installing it via

    pip install flask-statsdclient[Datadog]

## Usage

Import it and wrap app

    from flask import Flask
    from flask_statsdclient import StatsDClient

    app = Flask(__name__)
    statsd = StatsDClient(app)

You may modify the host, port and prefix with ``STATSD_HOST``, ``STATSD_PORT`` and
``STATSD_PREFIX`` options respectively in your Flask app config.

## Development

On a mac you can use the following commands to get up and running.
``` bash
brew install python3
```
otherwise run
``` bash
brew upgrade python3
```
to make sure you have an up to date version.

This project uses [pip-tools](https://pypi.org/project/pip-tools/) for dependency management. Install pip-tools

``` bash
pip3 install pip-tools
```

setup the project env
``` base
python -m venv venv
pip install -r requirements.txt -r requirements-dev.txt
```

Make sure the following environment variables are set
``` bash
export PYTHONPATH=`pwd`
```

Then load your virtualenv
```bash
source venv/bin/activate
```

### Running tests

``` bash
./linters.sh && coverage run --source=flask_statsdclient/ setup.py test
```

### Before committing any code

We have a pre-commit hook each dev needs to setup.
You can symlink it to run before each commit by changing directory to the repo and running

``` bash
cd .git/hooks
ln -s ../../pre-commit pre-commit
```
