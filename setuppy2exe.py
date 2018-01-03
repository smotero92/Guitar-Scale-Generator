from distutils.core import setup
import py2exe  #, os, pymssql
# import decimal
import subprocess



setup(windows=['main.py'], zipfile="foo/bar.zip", options={"py2exe": {"skip_archive": True}})

# setup(windows=['Name of your file.py'], zipfile="foo/bar.zip", options=py2exe_options, data_files=data_files)
# win32 client does not work if zipped in the default py2exe fashion, we need to sjkip the archiving

# "type python (the name of this document) py2exe into the console"
