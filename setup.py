"""A simple, configurable statsd client for Flask apps with optional Datadog support.

It also provides optional support for Dogstatsd with the [Datadog] optional install.
"""
from setuptools import setup

setup(
    name='Flask-StatsDClient',
    version='2.0.2',
    url='https://github.com/bbelyeu/flask-statsdclient',
    download_url='https://github.com/bbelyeu/flask-statsdclient/archive/2.0.2.zip',
    license='MIT',
    author='Brad Belyeu',
    author_email='bradleylamar@gmail.com',
    description='A simple statsd client extension for Flask apps with optional Datadog support',
    long_description=__doc__,
    packages=['flask_statsdclient'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
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
