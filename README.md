graphicore Bitmap Font Building, graphicoreBMFB
===============================================

This program builds fonts from a custom format "Bitmap Font" (BMF) into
ready to use OpenType format, or anything the used generator is capable of.
By using different parameters varying fonts are generated. Attached to
the program is the source data of graphicore Bitmap Font in the BMF format
licensed under the SIL Open Font License (OFL).

There is a [blog post](http://graphicore.de/en/archive/2010-09-09_A-Brute-Font-Attack) 
telling more. There's a [german version](http://graphicore.de/de/archive/2010-09-09_A-Brute-Font-Attack)
too.


Additional Disclaimer
---------------------
English is not my mother tongue, it's German. I'm sorry for inconveniences caused by that.


What You'll Need
----------------

* **Linux**. I use Linux and didn't try anything else with the code. Help for other systems 
  will find a place here if you provide it.

* **Python 2.6.5**. I import from the Python Standard Library:

    from __future__ import with_statement # backward compatibility
    import sys, os, re, codecs, math, json, random
    from optparse import OptionParser #in ./bmfb.py

* **FontForge** with Python bindings. 

  * On Debian and Ubuntu you can get it by running `sudo apt-get install python-fontforge`.
  * Run a Python shell and type `import fontforge`. If there's no error message (like 
    `ImportError: No module named fontforge`), you should be fine.
  * Any recent version of FontForge should work without problems.
  
  
Quickstart (on Linux)
---------------------

Extract the archive and go to the resulting directory.

    $ cd /the/dir/where/this/README/is/located

Try building one font.

    $ ./bmfb.py ./BMFonts/graphicoreBitmapFont/BitmapFont0Medium.jsn

Now, you should find the following files in the `./generated` dir:

  * `graphicoreBitmapFont0-Medium.sfd` (FontForge font format)
  * `graphicoreBitmapFont0-Medium.otf` (OpenType font format)

If that works, you can build all fonts from all `.jsn` files in `./BMFonts/graphicoreBitmapFont/`.
That will take a while.

    $ ./start.sh


Commandline Options
-------------------

All actions create files in the `./generated` folder. The source file should not be affected, as long
as it's not in the `./generated` folder and named like the output of the action.

You can get some help for using the script with this command:

    $ ./bmfb.py -h

The `bmfb.py` script always takes as its last argument the path to the JSON file that defines the font.

    $ ./bmfb.py ./BMFonts/graphicoreBitmapFont/BitmapFont0Medium.jsn

All other arguments should come before that.

    $ ./bmfb.py -a classes -l 1 -r 1 -v 3 ./BMFonts/graphicoreBitmapFont/BitmapFont0Medium.jsn

If the `dist` action is specified, there is an argument for the name of the kerning class, which should
be placed second to last.

    $ ./bmfb.py -a dist -v 1 @_1R_1_2Y2N3Y5N -R 1 ./BMFonts/graphicoreBitmapFont/BitmapFont0Medium.jsn


Hacking
-------

If you haven't played with Python, the [Python beginner's guide](http://wiki.python.org/moin/BeginnersGuide) 
is probably a good start.

Jump into the code at `./bmfb.py` -- that's how I use the `graphicoreBMFB` module.

The code contains docstrings and comments that can help you understand the inner workings of the script.
Docstrings are really useful and you can easily access them through the Python console.

    $ python
    >>> import graphicoreBMFB
    >>> help(graphicoreBMFB)

All the classes are still in the ./graphicoreBMFB/__init__.py file. That fact will change one day i think.

The [Fontforge Python documentation](http://fontforge.sourceforge.net/python.html) should also be useful.
The FontForge people do a great job at [documenting the application](http://fontforge.sourceforge.net). 
If you feel lost in the Python docs, try reading these and using FontForge itself.

The documentation for all other imported modules is available [here](http://docs.python.org/modindex.html).


Folder and File Structure
-------------------------

  * `./BMFonts/` -- some ready-to-use fonts, not necessary for running the program
  * `./BMFonts/graphicoreBitmapFont/#` -- the graphicore Bitmap Font (BMF)
  * `./generated/` -- the output goes there, files in this folder are NOT saved. Initially empty
  * `./graphicoreBMFB/` -- the module files. One at the moment, more as soon as needed
  * `./graphicoreBMFB/__init__.py` -- all the important stuff
  * `./bmfb.py` -- the command line script
  * `./LICENSE` -- the GNU Affero General Public License
  * `./README.md` -- this file
  * `./start.sh` -- build all the fonts from all `.jsn` files in `./BMFonts/graphicoreBitmapFont/` (takes a while)


The Bitmap Font (BMF) Format
----------------------------

A font is contained in a folder with the typeface name. Inside there's two types of things: options and glyphs.

Glyphs are in a folder called `glyphs`. That name can be changed in the options, but that's not recommended.
Inside the folder, glyphs are stored in simple files. For example, the capital A looks like this:

```
$ more ./BMFonts/graphicoreBitmapFont/glyphs/aCap.txt
...........
........###
.......###.
......####.
.....##.##.
....##..##.
.. #######.
..##....##.
.##.....###
##.........
...........
...........
```

A glyph contains no side bearing values. That information is stored inside the `features.distances` table 
that you can find in options.

Everything that isn't a glyph and ends with `.jsn` is an options file. These are stored in the 
[JSON format](http://www.json.org/).

Options can inherit from one another, and the last defined JSON file takes priority. They must specify their 
ancestors in their root object like this:

```
{
    "inherit": ["glyphs.jsn", "kerning.jsn", "ligatures.jsn"]
}
```

This will load `ligatures.json` first and all its ancestors, then `kerning.jsn` and all its ancestors, and finally
the glyphs.

If an option is already set, it will not be overwritten by the ancestors. Options are only set in the root element 
and in its direct children if these are dicts, there is no deeper copying.

The graphicoreBitmapFont shows how to use BMF options. The defaults dict in `./graphicoreBMFB/__init__.py` has 
some comments and the default values.

Enjoy! Lasse


License
-------

graphicore Bitmap Font Building, this program builds bitmap fonts
Copyright (c) 2010, Lasse Fister lasse@graphicore.de, http://graphicore.de

graphicore Bitmap Font Building is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

