import os
import sys

DIR = os.getcwd()

bin = """\
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from argparse import ArgumentParser

try:
    from %s import run, __version__
    from %s.config import config
except ImportError:
    import sys, os
    sys.path.append(os.path.split(os.path.split(os.path.realpath(__file__))[0])[0])
    from %s import run, __version__
    from %s.config import config

# clean stop on KeyboardInterrupt
from signal import signal, SIGINT

def stop(signum, frame):
        exit(0)

signal(SIGINT, stop)

if __name__ == '__main__':
    parser = ArgumentParser('%s')
    parser.add_argument('-a', '--argument', help='an example argument')

    options = parser.parse_args()

    if options.argument:
        config.argument = options.argument

    run()
"""

config = """\
# -*- coding:Utf-8 -*-

from utils import Storage

class Config(Storage):

    def __init__(self, *args, **kwargs):
        Storage(self, *args, **kwargs)
        # default values
        self.argument = 'this is an example argument'

config = Config()
"""

utils = """\
# -*- coding:Utf-8 -*-

# The following class is part of the web.py project. So it is in the Public
# Domain. For more informations, please see the following URLs :
#
#   https://github.com/webpy/webpy/blob/master/LICENSE.txt
#   https://github.com/webpy/webpy/blob/master/web/utils.py
#
class Storage(dict):
    \"\"\"
    A Storage object is like a dictionary except `obj.foo` can be used
    in addition to `obj['foo']`.

        >>> o = storage(a=1)
        >>> o.a
        1
        >>> o['a']
        1
        >>> o.a = 2
        >>> o['a']
        2
        >>> del o.a
        >>> o.a
        Traceback (most recent call last):
        ...
        AttributeError: 'a'

    \"\"\"

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError, k:
            raise AttributeError, k


    def __setattr__(self, key, value):
        self[key] = value

    def __delattr__(self, key):
        try:
            del self[key]
        except KeyError, k:
            raise AttributeError, k

    def __repr__(self):
        return '<Storage ' + dict.__repr__(self) + '>'
"""

setup_py = """\
# -*- coding:Utf-8 -*-

from setuptools import setup

from %s import __version__

setup(name='%s',
      version=__version__,
      description='FIXME',
      author='FIXME',
      long_description='FIXME',
      # or you can also do something like this
      # long_description=open("README").read(),
      author_email='FIXME',
      url='FIXME',
      # install_requires=['lib_with_a_certain_version>=0.9.9.1', 'another_lib'],
      # list of packages you want you application/lib install
      packages=['%s'],
      license= 'FIXME',
      # list of scripts supplied by your application
      scripts=['bin/%s'],
      keywords='FIXME',
     )

# vim:set shiftwidth=4 tabstop=4 expandtab:
"""

main_file = """\
# -*- coding:Utf-8 -*-

from config import config

def run():
    print 'Time to write your code!'
    print config.argument
"""

def conditionnaly_create_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)

def create_template(name):
    print "creating " + name
    conditionnaly_create_dir(DIR + '/' + name)
    print "creating " + name + "/bin"
    conditionnaly_create_dir(DIR + '/' + name + "/bin")
    print "creating " + name + "/bin/" + name
    open(DIR + '/' + name + "/bin/" + name, "w").write(bin % (name, name, name, name, name))
    os.system("chmod 755 " + DIR + '/' + name + "/bin/" + name)
    print "creating " + name + "/" + name
    conditionnaly_create_dir(DIR + '/' + name + "/" + name)
    print "creating " + name + "/" + name + "/" + name + ".py"
    open(DIR + '/' + name + "/" + name + "/" + name + ".py", "w").write(main_file)
    print "creating " + name + "/" + name + "/utils.py"
    open(DIR + '/' + name + "/" + name + "/utils.py", "w").write(utils)
    print "creating " + name + "/" + name + "/config.py"
    open(DIR + '/' + name + "/" + name + "/config.py", "w").write(config)
    print "creating " + name + "/" + name + "/__init__.py"
    open(DIR + '/' + name + "/" + name + "/__init__.py", "w").write("from %s import run\n\n__version__ = '0.1'" % name)
    print "creating " + name + "/setup.py"
    open(DIR + '/' + name + "/setup.py", "w").write(setup_py % (name, name, name, name))

if __name__ == "__main__":
    if not sys.argv[1:]:
        print "I will create a set of files for creating a python cli tool"
        print "Error: need a application name"
        sys.exit(1)

    create_template(sys.argv[1])
