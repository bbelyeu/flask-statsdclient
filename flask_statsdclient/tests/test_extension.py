import time
import unittest
from unittest.mock import patch

from flask import Flask
from flask_statsdclient import StatsDClient


def create_app():
    app = Flask(__name__)
    client = StatsDClient()
    client.init_app(app)
    return app


class TestStatsD(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.ctx = self.app.app_context()
        self.ctx.push()

    def tearDown(self):
        self.ctx.pop()

    def test_default_config(self):
        client = StatsDClient(self.app)
        self.assertEqual(('127.0.0.1', 8125), client.statsd.__dict__['_addr'])

    def test_custom_app_config(self):
        self.app.config['STATSD_HOST'] = '10.1.1.1'
        self.app.config['STATSD_PORT'] = 9999
        self.app.config['STATSD_PREFIX'] = 'foo'

        client = StatsDClient(self.app)
        self.assertEqual(('10.1.1.1', 9999), client.statsd.__dict__['_addr'])
        self.assertEqual('foo', client.statsd.__dict__['_prefix'])

    def test_custom_kwarg_config(self):
        config = {
            'STATSD_HOST': '1.2.3.4',
            'STATSD_PORT': 12345,
            'STATSD_PREFIX': 'foo.bar'
        }

        client = StatsDClient(self.app, config)
        self.assertEqual(('1.2.3.4', 12345), client.statsd.__dict__['_addr'])
        self.assertEqual('foo.bar', client.statsd.__dict__['_prefix'])

    def test_decr(self):
        client = StatsDClient(self.app)
        with patch('statsd.StatsClient.decr') as mock_decr:
            client.decr('test.counter')
            mock_decr.assert_called_once_with('test.counter')

    def test_gauge(self):
        client = StatsDClient(self.app)
        with patch('statsd.StatsClient.gauge') as mock_gauge:
            client.gauge('test', 1)
            mock_gauge.assert_called_once_with('test', 1)
            client.gauge('foo', 1, delta=True)
            mock_gauge.assert_called_with('foo', 1, delta=True)

    def test_incr(self):
        client = StatsDClient(self.app)
        with patch('statsd.StatsClient.incr') as mock_incr:
            client.incr('test.counter')
            mock_incr.assert_called_once_with('test.counter')
            client.incr('test.counter', 10)
            mock_incr.assert_called_with('test.counter', 10)
            client.incr('test.counter', rate=0.1)
            mock_incr.assert_called_with('test.counter', rate=0.1)

    def test_set(self):
        client = StatsDClient(self.app)
        with patch('statsd.StatsClient.set') as mock_set:
            client.set('test.counter', 1)
            mock_set.assert_called_once_with('test.counter', 1)

    def test_timer(self):
        client = StatsDClient(self.app)
        with patch('statsd.StatsClient.timer') as mock_timer:
            client.timer('test.counter')
            mock_timer.assert_called_once_with('test.counter')

    def test_timing(self):
        client = StatsDClient(self.app)
        ts = int((time.time() - 1515191917) * 1000)
        with patch('statsd.StatsClient.timing') as mock_timing:
            client.timing('test.counter', ts)
            mock_timing.assert_called_once_with('test.counter', ts)
