# `pyglatin`
Python command line tool to translate to and from pig latin.
For BUGS Spring 2019 git workshop.
Pig Latin rules can be found
[here](https://web.ics.purdue.edu/~morelanj/RAO/prepare2.html).

## To use this tool
Use the command

	`pyglatin <file>`
	`pylatin` reads from standard input

```shell
python pyglatin.py [OPTIONS] [file]
```

to use this tool.

#### Options
* `--help` - Get help on how to use the command
* `--english`/`--piglatin` - Explicitly state language to translate from

#### Arguments
* `file` *optional* - File name to read from; if blank, program reads from `stdin`
