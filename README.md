This is a simple python script that organizes files and directories into a YYYY/MM structure.
You can run it as many times as you'd like; already-organized files won't be touched again.

The script will only process files in the top-level of the "base" directory. See "Todo" for more info on this.

In case it's not clear:

* YYYY = four-digit year (2015)
* MM = two-digit month (06)

# Requirements

* Python (at least version 2.7)

# Demonstration
<code>
agileadam:~/transfer $ ls
2013  2014  2015  testdir  testfile

If testfile was last modified in January 2015, and testdir was last modified in June 2014...

agileadam:~/transfer $ python2.7 ../bin/pyorgdir.py
testfile --> /home/agileadam/transfer/2015/01/testfile
testdir --> /home/agileadam/transfer/2014/06/testdir
</code>

# Todo

* Currently if you place a file in a YYYY directory, but not within one of its MM directories, the file won't be automatically moved. It probably should be automatically moved into the appropriate MM subdirectory.
