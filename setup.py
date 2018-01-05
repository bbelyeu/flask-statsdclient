"""A simple, configurable statsd client for Flask apps.  """
from setuptools import setup


setup(
    name='Flask-StatsDClient',
    version='1.0',
    url='https://github.com/youversion/flask-statsdclient',
    license='MIT',
    author='Brad Belyeu',
    author_email='developers@youversion.com',
    description='A simple statsd client extension for Flask apps',
    long_description=__doc__,
    packages=['flask_statsdclient'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'statsd>=3.2.2'
    ],
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
