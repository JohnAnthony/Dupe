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
~/.emacs.d/lisp >> dupe -r .
Added directory: .
Scanning directory ./
Scanning directory ./themes/
Scanning directory ./scripts/
Scanning directory ./contrib/
Scanning directory ./color-theme-6.6.0/
Scanning directory ./examples/
Processing 54 files.

Duplicate found: (Size 459.0B)
  1 :: ./color-theme-autoloads.el~
  2 :: ./color-theme-autoloads.in
Would you like to delete (1) / (2) / (b)oth / (n)either? n

Duplicate found: (Size 1.25KB)
  1 :: ./mandelbrot.el
  2 :: ./DELETEME
Would you like to delete (1) / (2) / (b)oth / (n)either? 2

Duplicate found: (Size 0.0B)
  1 :: ./configure-stamp
  2 :: ./build-stamp
Would you like to delete (1) / (2) / (b)oth / (n)either? n
All duplicates handled.
~/.emacs.d/lisp >> 
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

## Charity
If you find this software useful, please consider donating do Meningitis U.K. or your local meningitis charity.

http://www.meningitisuk.org
