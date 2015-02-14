# Move top-level directories and files into a YYYY/MM/ directory structure
# based on the directory and file creation dates
import os
import re
import shutil
from time import strftime, localtime

# Use a full path (starts with '/') to directory
# or a function that returns a full path e.g., os.getcwd()
# I STRONGLY suggest using a hardcoded path to avoid running the script
# within another already-established structure.
base_dir = os.getcwd()

re_year_dir = re.compile("/[0-9]{4}(/[0-9]{2})?")

# Processing during the os.walk caused all sorts of problems,
# so instead we'll just build a list of the dirs/files to move, and process
# them after
to_move = []
for root, subdirs, files in os.walk(base_dir):
    # Process directories except YYYY and YYYY/MM
    if re_year_dir.search(root) is None:
        if root is not base_dir:
            to_move.append(root)
            # We only want to move top-level directories (leave their files within them)
            del subdirs[:]
        else:
            # These are top-level files, so move them
            for fname in files:
                to_move.append(os.path.join(root, fname))

# Process each of the paths
for old_path in to_move:
    # Using getmtime to avoid issues with files that have movied getting a new ctime value
    year_month = strftime("%Y/%m/", localtime(os.path.getmtime(old_path)))
    year_month_dir = os.path.join(base_dir, year_month)
    if not os.path.exists(year_month_dir):
        os.makedirs(year_month_dir)

    new_path = os.path.join(year_month_dir +
               os.path.basename(os.path.normpath(old_path)))

    shutil.move(old_path, new_path)

    print("{0} --> {1}".format(old_path.replace(base_dir, '').lstrip('./'), new_path))
