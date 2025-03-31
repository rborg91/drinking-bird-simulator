# Drinking Bird Simulator
Does your job involve pressing the same key on a keyboard all day?
Do you want this job to be automated for you, so you can pop out and say, watch a movie.
Well the drinking bird has your back. Simply follow the instructions below and automate
your work tasks.

## Requirements

- Python 3.12+
- [Python Poetry](https://python-poetry.org/docs/)

**Note:** Can only run in Powershell.

## Usage

Clone this repository to your local machine and change into the directory.

The repository is set-up to use [Poetry](https://python-poetry.org/) for dependency management.
If you've got poetry, use the following from within the project folder to install dependencies and run
in your Powershell terminal:

    poetry install

To run the drinking bird simulator, run the following command

    poetry run python drinking-bird-simulator.py

You can specify the key that the drinking bird presses with the `-k` or `--key` argument
and the number of times that it presses a key for you with the `-r` or `--rounds` argument.

For example, if you want to run the drinking bird to press the `e` key 10 times, simply run:

    poetry run python drinking-bird-simulator.py -k e -r 10

## Current Limitations

Can only press number/letter/symbol keyboard keys. Future versions will aim to be able to press other
keys such as `Enter`.
