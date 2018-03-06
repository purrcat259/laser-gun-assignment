# Laser Gun Assignment

Script to check which laser guns are within a specified range, with a default range of 112,000 metres.

## Requirements

* Python 3.x interpreter
* Input file (sample and test files provided)

## Usage

*Please note that you may have to run the following commands with python3 rather than python on most linux systems.*

Running `python distance_checker.py -h` will show the required and optional arguments that can be applied.

Required:
* File path to the input file

Optional:
* Minimum Gun Distance. If it is not provided, then the default will be used instead

Example usage:

`python distance_checker.py -file-path /data/test.in -minimum-distance 500`

### Tests

Pytest is required to be installed to run the tests. To run them:

`pytest tests.py`

## Licence

MIT
