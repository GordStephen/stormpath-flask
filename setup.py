"""
Flask-Stormpath
---------------

The simplest and most secure way to handle user authentication and
authorization with Flask, via Stormpath (https://stormpath.com).
"""


from setuptools import setup

from flask_stormpath import __version__ as version


setup(
    name = 'Flask-Stormpath',
    version = version,
    url = 'https://github.com/stormpath/stormpath-flask',
    license = 'Apache',
    author = 'Stormpath, Inc.',
    author_email = 'python@stormpath.com',
    description = 'Simple and secure user authentication for Flask via Stormpath.',
    long_description = __doc__,
    py_modules = ['flask_stormpath'],
    zip_safe = False,
    include_package_data = True,
    platforms = 'any',
    install_requires = [
        'Flask',
        'Flask-Login',
    ],
    classifiers = [
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: Session',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)