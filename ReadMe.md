# Snail Print

[![GitHub release][release-image]][release-url]
[![codeclimate][codeclimate-image]][codeclimate-url]
![Tests & Linter][ci-url]
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>

This library includes a print funtion that slows down the showing of output in console, character by character, as though typed by a typewriter.


## Getting started

Install the library with:

```sh
pip install -U snail_print
```

### Usage

![Presentation Demo Video](https://raw.githubusercontent.com/Baelfire18/snail_print/master/assets/presentacion_color.gif)

*Gif 1: Example of use of this real time print library*

Moreover, every console log in this video was made with the library and with [this file](https://github.com/Baelfire18/snail_print/master/presentation.py)

## Documentation

### snail_print

```python
function snail_print(*objects, delay=0.1, sep=" ", end="\n")
```

#### Parameters

+ `objects`: Can be any or even multiple python objects.

The objects whose string representation will be "snail printed".

+ `delay`: `float` or `int`, default `0.1`.

The delay, measured in seconds, between the printing of each character in `object`.

+ `sep`: `str`, default `" "`.

In case of having multiple arguments, one sep will be placed between each and the next.

+ `end`: `str`, default `"\n"`.

The final character of the print. By default creates a new line.


## Testing

Run the test suite with:

```sh
python -m unittest tests
```

## Install local

To install it locally from the source code:

```sh
python setup.py develop
```

[release-image]: https://img.shields.io/github/v/release/Baelfire18/snail_print.svg
[release-url]: https://github.com/Baelfire18/snail_print/releases/latest
[codeclimate-image]: https://codeclimate.com/github/Baelfire18/snail_print/badges/gpa.svg
[codeclimate-url]: https://codeclimate.com/github/Baelfire18/snail_print
[ci-url]: https://github.com/Baelfire18/snail_print/actions/workflows/tests-and-linter.yml/badge.svg
