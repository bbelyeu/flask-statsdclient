"""A simple, configurable statsd client for Flask apps with optional Datadog support.

It also provides optional support for Dogstatsd with the [Datadog] optional install.
"""
import sys

from setuptools import setup

if sys.version_info < (3, 5):
    sys.exit('Sorry, Python < 3.5 is not supported')

__version__ = '2.1.0'

setup(
    name='Flask-StatsDClient',
    version=__version__,
    url='https://github.com/bbelyeu/flask-statsdclient',
    download_url='https://github.com/bbelyeu/flask-statsdclient/archive/{}.zip'.format(
        __version__),
    license='MIT',
    author='Brad Belyeu',
    author_email='bradleylamar@gmail.com',
    description=__doc__,
    long_description=open("README.md", "r").read(),
    packages=['flask_statsdclient'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    python_requires='>=3.5',
    install_requires=[
        'Flask',
        'statsd>=3.2.2'
    ],
    extras_require={
        'Datadog': ['datadog']
    },
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    keywords=['flask', 'statsd', 'metrics', 'instrumentation'],
    test_suite='flask_statsdclient.tests',
)
