# Dupe

A UNIX-like (but not *NIX contstrained) tool for finding and removing duplicate files

## Usage

Unless you do something to make the situation otherwise, Dupe will require user confirmation before it will delete anything.

``` bash
$ dupe -r .
$ dupe ~/Pictures ~/Downloads
$ dupe myfile.jpg maybesame.jpg
```

Local installation:
``` bash
$ git clone https://github.com/JohnAnthony/Dupe.git
$ cd Dupe
$ sudo make install
```

Example usage:
``` bash
~/quicklisp >> touch BLANK1 BLANK2
~/quicklisp >> dupe -r .
Added directory: .
Scanning directory ./
Scanning directory ./tmp/
Scanning directory ./quicklisp/
Scanning directory ./local-projects/
Scanning directory ./dists/
Scanning directory ./dists/quicklisp/
Scanning directory ./cache/
Scanning directory ./cache/asdf-fasls/
Scanning directory ./cache/asdf-fasls/1fk411/
Processing 31 files.
Duplicate found: 
  1 :: ./dists/quicklisp/enabled.txt
  2 :: ./BLANK2
(Size 0.0B)
Would you like to delete (1) / (2) / (b)oth / (n)either ?
2
Duplicate found: 
  1 :: ./BLANK2
  2 :: ./BLANK1
(Size 0.0B)
Would you like to delete (1) / (2) / (b)oth / (n)either ?
2
~/quicklisp >> ls
asdf.lisp  cache/  dists/  local-projects/  quicklisp/  setup.lisp  tmp/
~/quicklisp >> 
```

## License
(Copied from LICENSE file)

Copyright (C) 2012 John Anthony

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
