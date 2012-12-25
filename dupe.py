#!/usr/bin/python2

'''
Finds duplicate files based on filesize and md5 hash
Created by John Anthony and licensed under the GPLv3
'''

import sys
import getopt
import os
import hashlib
import signal

## Classes

class Config():
    '''
    Contains a complete set of configuration flags and directories
    '''
    def __init__(self):
        ''' Set our defaults '''
        self.recursive = False
        self.directories = []
        self.files = []
    def get_file_list(self):
        '''
        Returns a list of all files in self.directories and follows
        rules as appropriate for flags (i.e. recursively etc.)
        '''
        dirfiles = []
        for dirs in self.directories:
            dirfiles = dirfiles + files_in_dir(dirs, self.recursive)
        return nub(self.files + dirfiles)

class File():
    '''
    Contains a set of file attributes; path and size by default and
    md5 when needed
    '''
    def __init__(self, inpath):
        self.path = inpath
        self.size = os.path.getsize(inpath)
        self.md5 = ""
    def get_md5(self):
        '''
        Returns an MD5 hash for the file, populating the field if it
        is currently unpopulated
        '''
        if self.md5 != "":
            return self.md5

        file_ = open(self.path)
        md5block = hashlib.new("md5")
        for data in file_.read(2**20):
            md5block.update(data)

        self.md5 = md5block.digest()
        return self.md5
    def matches(self, file_):
        ''' Takes a file and returns true if these files match '''
        if self.size != file_.size:
            return False
        if self.get_md5() != file_.get_md5():
            return False
        return True

## Top-level functions

def dupecheck(lst):
    ''' Recursively steps over a list looking for duplicates '''
    if len(lst) < 2:
        return
    head = lst[0]
    tail = lst[1:]
    dupes = duplicates(head, tail)
    
    for dupe in dupes:
        show_duplicates(head, dupe)
        choice = get_choice()
        if choice == 'n':
            continue
        if choice in ('2', 'b'):
            os.remove(dupe.path)
            dupes.remove(dupe)
            tail.remove(dupe)
        if choice in ('1', 'b'):
            os.remove(head.path)
            break

    return tail

def duplicates(file_, lst):
    '''
    The main lifting function. Does all the crunchwork of actually
    checking for duplicates and returns a list of duplicate files
    '''
    matches = []
    for file2 in lst:
        if file_.matches(file2):
            matches.append(file2)
    return matches

def elem_after(elem, lst):
    '''
    Finds an element "elem" in a list and returns everything after
    that element
    '''
    index = lst.index(elem) + 1
    return lst[index:]

def exit_with_usage_info():
    ''' Exit cleanly with a list of flags and flag information '''

    usage_txt = """
Please see the readme file or manpage for proper usage inctructions.
  :: man dupe
  :: cat README
"""

    print(usage_txt)
    exit(1)

def files_in_dir(dir_, recurse=False):
    '''
    Takes a directory path as an argument and returns a list of file
    path strings in that directory. Takes an additional option
    argument allowing this file gathering to become recursive
    '''

    # Sanitise input
    if dir_[-1] != "/":
        dir_san = dir_ + "/"
    else:
        dir_san = dir_

    print("Scanning directory " + dir_san)
    files = []
    for file_ in os.listdir(dir_san):
        fullpath = dir_san + file_
        if os.path.isdir(fullpath):
            if recurse:
                files = files + files_in_dir(fullpath, True)
        else:
            files.append(fullpath)
    return files

def get_choice():
    ''' Simple dialogue to ask which file to delete of a pair '''

    ask = "Would you like to delete (1) / (2) / (b)oth / (n)either? "
    valid_options = ["1", "2", "b", "both", "n", "neither"]

    choice = ""
    while not choice in valid_options:
        choice = raw_input(ask)
        choice = choice.lower()

    if choice == "both":
        return "b"
    if choice == "neither":
        return "n"
    return choice

def handle_args():
    '''
    Uses getopt to parse arguments and return an instance of Config
    '''
    shorto = "hr"
    longo = ["help", "recursive"]

    conf = Config()

    # Get a list of options
    try:
        opts, args = getopt.gnu_getopt(sys.argv[1:], shorto, longo)
    except getopt.GetoptError, err:
        print(err)
        exit(0)

    # Handle flags
    for opt, _ in opts:
        if opt in ("-h", "--help"):
            exit_with_usage_info()
        elif opt in ("-r", "--recursive"):
            conf.recursive = True

    # Get a list of directories and files All args left in args MUST
    # be paths. Pop out anything that's used
    paths = args
    
    # Check and handle directory arguments
    for path in paths:
        if os.path.isdir(path):
            conf.directories.append(path)
            print("Added directory: " + path)
        elif os.path.isfile(path):
            conf.files.append(path)
            print("Added file: " + path)
        else:
            print("Not a valid directory: " + path)
            exit(1)

    return conf

def nub(lst):
    ''' Removes duplicates from a list '''
    # This works because converting a list to a set removes all
    # duplicates. List -> Set -> List will therefore remove all
    # duplicates and leave us with a duplicate-free list
    return list(set(lst))

def paths_to_files(paths):
    '''
    Takes a list of paths and returns a list of corresponding File
    objects
    '''
    files = []
    for path in paths:
        files.append(File(path))
    return files

def pretty_size(size):
    '''
    Takes a long and returns a pretty string representation in bytes
    (B), kibibytes (KiB), mebibytes (MiB), gibibytes (GiB) or
    tebibytes (TB) as appropriate
    '''
    suffixes = [("B", 2**10), ("KB", 2**20), ("MB", 2**30),
                ("GB", 2**40), ("TB", 2**50)]
    for suf, lim in suffixes:
        if size > lim:
            continue
        else:
            return str(round(size / float(lim / 2**10), 2)) + suf

def show_duplicates(dup1, dup2):
    '''
    Display a pair of duplicate files via stdout for the user to make
    a decision based upon
    '''
    print("")
    print("Duplicate found: (Size " + pretty_size(dup1.size) + ")")
    print("  1 :: " + dup1.path)
    print("  2 :: " + dup2.path)

def sigint_handler(sig, _):
    ''' For handling SIGINT messages gracefully '''
    print(sig)
    print("\n\nSIGINT received. Exiting cleanly...")
    sys.exit(0)

## Main    

def main():
    ''' Main function '''
    # Attach a signal handler for clean exits
    signal.signal(signal.SIGINT, sigint_handler)

    conf = handle_args()
    paths = conf.get_file_list()

    # A little error checking and declaration of intent
    if len(paths) == 0:
        print("No files to check.")
    elif len(paths) == 1:
        print("Only one file given as input. Nothing to compare.")
    else:
        print("Processing " + str(len(paths)) + " files.")

    files = paths_to_files(paths)
    while len(files) > 1:
        files = dupecheck(files)
    print("All duplicates handled.")

if __name__ == "__main__":
    main()
