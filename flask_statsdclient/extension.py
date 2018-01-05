"""Flask StatsDClient Extension module."""
from statsd import StatsClient


class StatsDClient(object):
    """Class to wrap Flask app and provide access to statsd."""

    def __init__(self, app=None, config=None):
        self.config = None
        self.statsd = None
        if app is not None:
            self.app = app
            self.init_app(app, config)
        else:
            self.app = None

    def init_app(self, app, config=None):
        """Init Flask Extension."""
        if config is not None:
            self.config = config
        elif self.config is None:
            self.config = app.config

        self.config.setdefault('STATSD_HOST', 'localhost')
        self.config.setdefault('STATSD_PORT', 8125)
        self.config.setdefault('STATSD_PREFIX', None)

        self.statsd = StatsClient(
            host=self.config['STATSD_HOST'],
            port=self.config['STATSD_PORT'],
            prefix=self.config['STATSD_PREFIX']
        )

    def decr(self, *args, **kwargs):
        """Wrap statsd decr.

        https://statsd.readthedocs.io/en/latest/types.html#counters
        """
        return self.statsd.decr(*args, **kwargs)

    def gauge(self, *args, **kwargs):
        """Wrap statsd gauge.

        https://statsd.readthedocs.io/en/latest/types.html#gauges
        """
        return self.statsd.gauge(*args, **kwargs)

    def incr(self, *args, **kwargs):
        """Wrap statsd incr.

        https://statsd.readthedocs.io/en/latest/types.html#counters
        """
        return self.statsd.incr(*args, **kwargs)

    def set(self, *args, **kwargs):
        """Wrap statsd set.

        https://statsd.readthedocs.io/en/latest/types.html#sets
        """
        return self.statsd.set(*args, **kwargs)

    def timer(self, *args, **kwargs):
        """Wrap statsd timer.

        https://statsd.readthedocs.io/en/latest/timing.html#timing-chapter
        """
        return self.statsd.timer(*args, **kwargs)

    def timing(self, *args, **kwargs):
        """Wrap statsd timing.

        https://statsd.readthedocs.io/en/latest/timing.html#timing-chapter
        """
        return self.statsd.timing(*args, **kwargs)
