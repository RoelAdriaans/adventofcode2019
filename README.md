# Advent of Code 2019

Advent of Code 2019 with tests and utils etc

## Todo

- Add logging for debugging?
- Make modules out of the days that auto load. Include test and source in the dame module. (See Odoo modules?)
- Make module or day class responsible for specify files to load, but do not load and split files
- Generate sphinx documentation from docstrings? 
- Complete all puzzles (Doh)

## Cookiecutter

To create a new day with the CookieCutter version run the command from the
`advent2019` directory.

```shell script
cookiecutter template -f
```

Answer the questions:
* `advendofcode2019` : Accept default answer. This installs the result in the currect directory
* `day` : Answer with day you're working on, with leading zero. Eg: 07, 10, 31.
* `directory_name`, `file_name`, `class_name` : Accept default answer

This will create the correct files in the `src` and `tests` directories.
The `-f` option is required to make the files in the current subdirectory.
When the project supports modules this is probably no longer needed.

The new solution still have to be added to the `main.py` file.

### Cookiecutter Todo

* Nothing at the moment

## Install

Install the application with:

```
pip3 install -e .
```

### Run

Use `tox` to run the tests, run `adventofcode` to run the main application.
