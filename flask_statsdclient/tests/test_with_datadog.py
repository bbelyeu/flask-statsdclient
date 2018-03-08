"""Test the statsd extension module."""
import time
import unittest
from unittest.mock import patch

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
        self.app = create_app()
        self.ctx = self.app.app_context()
        self.ctx.push()

    def tearDown(self):
        """Tear down tests."""
        self.ctx.pop()

    def test_decr(self):
        """Test decr wrapper."""
        client = flask_statsdclient.StatsDClient(self.app)
        with patch('datadog.statsd.decrement') as mock_decr:
            client.decr('test.counter')
            mock_decr.assert_called_once_with('test.counter')

    def test_gauge(self):
        """Test gauge wrapper."""
        client = flask_statsdclient.StatsDClient(self.app)
        with patch('datadog.statsd.gauge') as mock_gauge:
            client.gauge('test', 1)
            mock_gauge.assert_called_once_with('test', 1)
            client.gauge('foo', 1, delta=True)
            mock_gauge.assert_called_with('foo', 1, delta=True)

    def test_incr(self):
        """Test incr wrapper."""
        client = flask_statsdclient.StatsDClient(self.app)
        with patch('datadog.statsd.increment') as mock_incr:
            client.incr('test.counter')
            mock_incr.assert_called_once_with('test.counter')
            client.incr('test.counter', 10)
            mock_incr.assert_called_with('test.counter', 10)
            client.incr('test.counter', rate=0.1)
            mock_incr.assert_called_with('test.counter', rate=0.1)

    def test_set(self):
        """Test set wrapper."""
        client = flask_statsdclient.StatsDClient(self.app)
        with patch('datadog.statsd.set') as mock_set:
            client.set('test.counter', 1)
            mock_set.assert_called_once_with('test.counter', 1)

    def test_timing(self):
        """Test timing wrapper."""
        client = flask_statsdclient.StatsDClient(self.app)
        timestamp = int((time.time() - 1515191917) * 1000)
        with patch('datadog.statsd.timing') as mock_timing:
            client.timing('test.counter', timestamp)
            mock_timing.assert_called_once_with('test.counter', timestamp)
