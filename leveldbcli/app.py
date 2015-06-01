'''
leveldb-cli

Usage:
  leveldb create -d <db_path>
  leveldb get <key> -d <db_path> [-x | --hex]
  leveldb put <key> <value> -d <db_path>
  leveldb delete <key> -d <db_path>
  leveldb -h | --help
  leveldb -v | --version

Options:
  -d --database  Database path
  -x --hex       Print binary data in lowercase hex (without 0x prefix)
  -h --help      Show this screen
  -v --version   Show version
'''

from __future__ import print_function
import os.path

from docopt import docopt
from leveldb import LevelDB


def main():
    args = docopt(__doc__, version='leveldb-cli 0.1.0')

    cmd_create = args['create']
    cmd_get = args['get']
    cmd_put = args['put']
    cmd_delete = args['delete']
    db_path = args['<db_path>']
    db_exists = os.path.exists(db_path)
    if db_exists and cmd_create:
        print('Error: file %s exists' % db_path)
        return 1
    if not db_exists and any([cmd_get, cmd_put, cmd_delete]):
        print('Error: database %s does not exist' % db_path)
        return 1

    db = LevelDB(db_path)  # create or open

    if cmd_get:
        k = args['<key>']
        try:
            v = db.Get(k)
        except KeyError:
            print('Error: key %s does not exist' % k)
            return 1
        else:
            if args['--hex']:
                print(v.encode('hex'))
            else:
                print(v)
    elif cmd_put:
        k, v = args['<key>'], args['<value>']
        db.Put(k, v)
    elif cmd_delete:
        k = args['<key>']
        db.Delete(k)
    return 0
