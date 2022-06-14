# Snail Print

[![GitHub release](https://img.shields.io/github/v/release/Baelfire18/slow_print.svg)](../../releases/latest)
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>

This library includes a print funtion that slowly shows the output in console in real time.



Moreover, every console log in this video was made with the library and with [this file](https://github.com/Baelfire18/snail_print/master/presentation.py)

## Getting started

Install the library with:

```sh
pip install -U snail_print
```

### Usage

![Presentation Demo Video](https://raw.githubusercontent.com/Baelfire18/snail_print/master/assets/presentation.mp4)

*Video 1: Example of use of this real life print library*

## Documentation

### snail_print

```python
function snail_print(*objects, delay=0.1, sep=" ", end="\n", flush=False)
```

#### Parameters

+ `objects`: Can be any python object.
The object wicth will be printed slowly in real time.

+ `delay`: `float` or `int`, default `0.1`.
The time between the addition of the next character or the time between each print.


## Testing

Run the test suite with:

```sh
python -m unittest tests
```

## Install Local

To install it locally from the source code:

```sh
python setup.py develop
```
