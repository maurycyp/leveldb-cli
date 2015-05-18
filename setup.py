try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='leveldb-cli',
    version='0.1.0',
    description='A command-line interface for LevelDB databases.',
    long_description=open('README.txt').read(),
    author='Maurycy Pietrzak',
    author_email=['github.com@wayheavy.com'],
    url='https://github.com/maurycyp/leveldb-cli',
    packages=['leveldbcli'],
    license='Unlicense',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Topic :: Database',
    ],
    install_requires=[
        'docopt==0.6.2',
        'leveldb==0.193',
    ],
    entry_points={'console_scripts': [
        'leveldb = leveldbcli.app:main',
    ]},
    # TODO zip_safe, package_data
)
