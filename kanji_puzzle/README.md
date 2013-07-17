# Kanji Puzzle Solver

## Usage

* Run findpairs.py to download and make a dictionary of all the words containing only two kanji.
* Run puzzle.py with arguments as follows
* ./puzzle.py kanji1 kanji2 kanji3 kanji4 [start/end] [start/end] [start/end] [start/end] [start/end]
* [start/end] signifies where the kanji (1-4)  must start appear at the start or the end of the word. 

## Caveats

* This assumes that the OS character set is utf8 which probably only works on the map.
* The kanji pairs list currently contains duplicates which makes the performance very slightly slower. 
