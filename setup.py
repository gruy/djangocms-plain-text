#!/usr/bin/env python

from os import path, sep
from distutils.core import setup


version = '0.1'

classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: BSD License",
    "Programming Language :: Python :: 2.6",
    "Programming Language :: Python :: 2.7",
    "Operating System :: OS Independent",
    "Topic :: Software Development :: Libraries",
    "Topic :: Utilities",
    "Environment :: Web Environment",
    "Framework :: Django",
    "Topic :: Internet :: WWW/HTTP",
    "Topic :: Software Development :: Libraries :: Python Modules",
]

root_dir = path.dirname(path.abspath(__file__))
long_desc = open(sep.join([root_dir, 'README'])).read()


setup(
    name='djangocms_plain_text',
    version=version,
    url='https://bitbucket.org/gruy/djangocms-plain-text',
    author='Cyrill Popov',
    author_email='gruy@feodosia.net',
    license='LICENSE',
    packages=['djangocms_plain_text', 'djangocms_plain_text.migrations'],
    description=('Django CMS plugin for plain text.'),
    keywords=['editor', 'django-cms', 'django', ],
    classifiers=classifiers,
    long_description=long_desc,
    install_requires=['django-cms>=3', ],
    include_package_data=True,
)
