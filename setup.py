from setuptools import find_packages
from setuptools import setup

setup(
    name='pre-commit-hooks',
    description='Some out-of-the-box hooks for pre-commit',
    url='https://github.com/mpratsch/pre-commit-hooks',
    version='1.0.0',

    author='Martina Rath',
    author_email='mpratscher@gmail.com',

    platforms='linux',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],

    packages=find_packages('.'),
    install_requires=[
        'fuzzywuzzy',
        'python-Levenshtein'
    ],
    entry_points={
        'console_scripts': [
            'check_rcloud_version = pre_commit_hooks.check_rcloud_version:main',
        ],
    },
)

