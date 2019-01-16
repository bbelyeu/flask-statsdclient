"""Flask StatsDClient Extension module."""
from functools import wraps

try:
    from datadog import initialize, statsd
    DATADOG_IMPORTED = True
except ImportError:
    DATADOG_IMPORTED = False
    from statsd import StatsClient


def datadog_prefix(method):
    """Add prefix if using Datadog.

    http://datadogpy.readthedocs.io/en/latest/#datadog-dogstatsd-module
    """

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Inner decorator wrapper."""
        if DATADOG_IMPORTED and self.config['STATSD_PREFIX']:
            # Datadog statsd doesn't handle prefix
            args_0 = '.'.join([self.config['STATSD_PREFIX'], args[0]])
            args = (args_0,) + args[1:]
        return method(self, *args, **kwargs)

    return wrapper


class StatsDClient():
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

        if DATADOG_IMPORTED:
            self.statsd = statsd
            initialize(statsd_host=self.config['STATSD_HOST'],
                       statsd_port=self.config['STATSD_PORT'])
        else:
            self.statsd = StatsClient(
                host=self.config['STATSD_HOST'],
                port=self.config['STATSD_PORT'],
                prefix=self.config['STATSD_PREFIX']
            )

    @datadog_prefix
    def decr(self, *args, **kwargs):
        """Wrap statsd decr.

        https://statsd.readthedocs.io/en/latest/types.html#counters
        If using datadog, transform method name.
        http://datadogpy.readthedocs.io/en/latest/#datadog-dogstatsd-module
        """
        if DATADOG_IMPORTED:
            self.statsd.decrement(*args, **kwargs)
        else:
            self.statsd.decr(*args, **kwargs)

    @datadog_prefix
    def gauge(self, *args, **kwargs):
        """Wrap statsd gauge.

        https://statsd.readthedocs.io/en/latest/types.html#gauges
        """
        self.statsd.gauge(*args, **kwargs)

    @datadog_prefix
    def incr(self, *args, **kwargs):
        """Wrap statsd incr.

        https://statsd.readthedocs.io/en/latest/types.html#counters
        If using datadog, transform method name.
        http://datadogpy.readthedocs.io/en/latest/#datadog-dogstatsd-module
        """
        if DATADOG_IMPORTED:
            self.statsd.increment(*args, **kwargs)
        else:
            self.statsd.incr(*args, **kwargs)

    @datadog_prefix
    def set(self, *args, **kwargs):
        """Wrap statsd set.

        https://statsd.readthedocs.io/en/latest/types.html#sets
        """
        self.statsd.set(*args, **kwargs)

    @datadog_prefix
    def timer(self, *args, **kwargs):
        """Wrap statsd timer.

        https://statsd.readthedocs.io/en/latest/timing.html#timing-chapter
        """
        self.statsd.timer(*args, **kwargs)

    @datadog_prefix
    def timing(self, *args, **kwargs):
        """Wrap statsd timing.

        https://statsd.readthedocs.io/en/latest/timing.html#timing-chapter
        """
        self.statsd.timing(*args, **kwargs)
