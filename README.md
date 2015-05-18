# leveldb-cli
A command-line interface for LevelDB, an on-disk key-value database.

## Installation
```bash
$ pip install leveldb-cli
```

## Example
```bash
$ leveldb create -d my.db
$ leveldb put 1 2 -d my.db
$ leveldb get 1 -d my.db
2
$ leveldb delete 1 -d my.db
$ leveldb get 1 -d my.db
Error: key 1 does not exist
```

## See also
* http://en.wikipedia.org/wiki/LevelDB
