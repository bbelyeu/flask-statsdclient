"""Test the statsd extension module."""
import importlib
import sys
import time
import unittest
from unittest.mock import patch

import datadog
from flask import Flask

import flask_statsdclient  # isort:skip


def create_app():
    """Create a Flask app for context."""
    app = Flask(__name__)
    client = flask_statsdclient.StatsDClient()
    client.init_app(app)
    return app


class TestStatsD(unittest.TestCase):
    """Test StatsDClient class."""

    def setUp(self):
        """Set up tests."""
        # Force extension to load without datadog
        sys.modules['datadog'] = None
        importlib.reload(flask_statsdclient.extension)

        self.app = create_app()
        self.ctx = self.app.app_context()
        self.ctx.push()

    def tearDown(self):
        """Tear down tests."""
        self.ctx.pop()
        # Reload extension to restore sys.modules to correct state
        sys.modules['datadog'] = datadog
        importlib.reload(flask_statsdclient.extension)

    def test_default_config(self):
        """Test the default configs."""
        client = flask_statsdclient.StatsDClient(self.app)
        self.assertEqual(('127.0.0.1', 8125), client.statsd.__dict__['_addr'])

    def test_custom_app_config(self):
        """Test custom configs set on app."""
        self.app.config['STATSD_HOST'] = '10.1.1.1'
        self.app.config['STATSD_PORT'] = 9999
        self.app.config['STATSD_PREFIX'] = 'foo'

        client = flask_statsdclient.StatsDClient(self.app)
        self.assertEqual(('10.1.1.1', 9999), client.statsd.__dict__['_addr'])
        self.assertEqual('foo', client.statsd.__dict__['_prefix'])

    def test_custom_kwarg_config(self):
        """Test custom configs passed via kwargs."""
        config = {
            'STATSD_HOST': '1.2.3.4',
            'STATSD_PORT': 12345,
            'STATSD_PREFIX': 'foo.bar'
        }

        client = flask_statsdclient.StatsDClient(self.app, config)
        self.assertEqual(('1.2.3.4', 12345), client.statsd.__dict__['_addr'])
        self.assertEqual('foo.bar', client.statsd.__dict__['_prefix'])

    def test_decr(self):
        """Test decr wrapper."""
        client = flask_statsdclient.StatsDClient(self.app)
        with patch('statsd.StatsClient.decr') as mock_decr:
            client.decr('test.counter')
            mock_decr.assert_called_once_with('test.counter')

    def test_gauge(self):
        """Test gauge wrapper."""
        client = flask_statsdclient.StatsDClient(self.app)
        with patch('statsd.StatsClient.gauge') as mock_gauge:
            client.gauge('test', 1)
            mock_gauge.assert_called_once_with('test', 1)
            client.gauge('foo', 1, delta=True)
            mock_gauge.assert_called_with('foo', 1, delta=True)

    def test_incr(self):
        """Test incr wrapper."""
        client = flask_statsdclient.StatsDClient(self.app)
        with patch('statsd.StatsClient.incr') as mock_incr:
            client.incr('test.counter')
            mock_incr.assert_called_once_with('test.counter')
            client.incr('test.counter', 10)
            mock_incr.assert_called_with('test.counter', 10)
            client.incr('test.counter', rate=0.1)
            mock_incr.assert_called_with('test.counter', rate=0.1)

    def test_set(self):
        """Test set wrapper."""
        client = flask_statsdclient.StatsDClient(self.app)
        with patch('statsd.StatsClient.set') as mock_set:
            client.set('test.counter', 1)
            mock_set.assert_called_once_with('test.counter', 1)

    def test_timer(self):
        """Test timer wrapper."""
        client = flask_statsdclient.StatsDClient(self.app)
        with patch('statsd.StatsClient.timer') as mock_timer:
            client.timer('test.counter')
            mock_timer.assert_called_once_with('test.counter')

    def test_timing(self):
        """Test timing wrapper."""
        client = flask_statsdclient.StatsDClient(self.app)
        timestamp = int((time.time() - 1515191917) * 1000)
        with patch('statsd.StatsClient.timing') as mock_timing:
            client.timing('test.counter', timestamp)
            mock_timing.assert_called_once_with('test.counter', timestamp)
