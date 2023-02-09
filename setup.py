# -*- coding: utf-8 -*-
from setuptools import find_packages, setup


setup(
    name='wagtail_clear_cache',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    description='With the click of a button you can clear all Django Template Cache',
    long_description='For installation instructions see https://github.com/KalobTaulien/wagtail_clear_cache',
    url='https://github.com/KalobTaulien/wagtail_clear_cache',
    author='Kalob Taulien',
    author_email='kalob@kalob.io',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        'Operating System :: OS Independent',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 3.2',
        'Framework :: Django :: 4.0',
        'Framework :: Django :: 4.1',
        'Framework :: Wagtail',
        "Framework :: Wagtail :: 4",
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP',
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    keywords='development',
    install_requires=[
        'wagtail>=4.1',
        'Django>=3.2'
    ]
)
