# Problem Set 3

Hashing!

**You are encouraged to use libraries wherever needed in this assignment.**

In particular, the following (standard) libraries may be of use:

- [hashlib](https://docs.python.org/3/library/hashlib.html)
- [hmac](https://docs.python.org/3/library/hmac.html)

As with other assignments, python 3.10 is recommended.

## Cheating

All the code you submit must be written by you. Submitting code written by
anyone else is cheating in the official sense. Please don't do that.

It's ok (and encouraged!) for students to work together by discussing problems
without sharing code. It's also ok to have someone look at your code to help
you debug a specific issue. But it's not ok to look at someone else's code to
copy it or to have anyone write code for you. Please don't explore the gray
area between these things.

For common operations like "open a file", "parse a JSON string", or "call
a library function", it's ok to copy two or three lines of code from
documentation, Stack Overflow, etc. But copying more than two or three lines
of code is probably not ok. If you do, you must clearly cite your source
in an inline comment that begins with COPIED. Citing your source doesn't
automatically make copying ok, but failing to cite your source turns one
violation into two violations. Please don't explore the gray area of what
counts as a "line of code".

## Problems

This assignment consists of 5 problems:

1. Generate MD5 hash
1. Generate SHA256 hash
1. Determine if internal MD5 state matches a message
1. Determine if internal SHA256 state matches a message
1. Generating HMAC with SHA256
1. Given 2 MD5-colliding byte sequences, return 2 additional collisions

## Submission

You may submit this assignment in multiple ways described below.

Note that you can submit partial assignment without solving all of
the problems first. We actually encourage you to submit early and often as
GradeScope will help you testing your solutions.

### Gradescope

GradeScope uses [`pytest`](https://docs.pytest.org/en/7.1.x/contents.html)
for the test runner. It usually shows pretty good error messages.
You can see some examples [here](https://docs.pytest.org/en/7.1.x/how-to/output.html).
If youll need any help with gradescope output, please ask in slack.

Note that we reserve the right to update GradeScope test suite as we come
across issues/bugs or find submissions which abuse things.

### Python Submission

This is the simplest approach and we recommend that most students take this option.
You simply need to submit a file named `ps3.py`. Note filename is important.
Its not `problems.py` or anything else. Its literally `filename == 'ps3.py'`.
This file should have these 6 functions defined:

- `problem1`
- `problem2`
- `problem3`
- `problem4`
- `problem5`
- `problem6`

Yes we know this is very creative naming but it keeps things simple :D

Below you will find type-annotated stubs of the functions you need to implement.
You can copy-paste these stubs into `ps2.py` to get you started.
Note that parameter names are important. GradeScope will call these
functions with the same parameter names as defined in the stubs.
Also some of the functions have [doctests](https://github.com/cs-gy6903/resources#doctests)
defined which provide example output functions should produce.

GradeScope will run this code on Python3.10 so we recommend you use the same
Python version locally for development.
[pyenv](https://github.com/pyenv/pyenv) might be of use here if you need to
manage multiple Python versions.

### Binary Submission

If you feel adventurous, you can submit this assignment as an executable file
therefore allowing you to solve it in any other language.
Rust, C, C++, Java, JavaScript, even bash, etc can be used.
Note that GradeScope runs Ubuntu22.04 so the executable needs
to be POSIX-compatible and therefore no Windows executables.

To do that, you will need to submit either:

- script file with valid shebang. For example `ps3`, `ps3.sh`, `ps3.js`, etc.
  By script file we mean here the file is plain text file (not binary).
- compile an actual binary executable named `ps3` from submitted source code
  via `setup.sh` (see below).
  Note that you CANNOT submit binary file directly as its source-code
  will not be accessible. The binary needs to be compiled in GradeScope
  from submitted source code.

In either case the executable will have to do the following:

- accept `bson` input via `stdin`
- produce `bson` output to `stdout`

[`BSON`](https://www.mongodb.com/basics/bson) is used to explicitly allow binary
data in both input and output without any additional steps like hex encoding.

`BSON` input will be of the following structure:

- keys are the same as python function names described above
- for each key, value is a dictionary with parameters for the function
  as defined above.

For example for a single function defined as:

```python
def foo(a: int, b: str): pass
```

then the BSON input will be something like (represented as json here for clarity):

```json
{
  "foo": {
    "a": 1,
    "b": "test"
  }
}
```

`BSON` output will be of the following structure:

- keys are the same as python function names described above
- for each key, value is the return value of the function as described above

In other words, for each function described above bson input via stdin will
provide the function parameters and bson output to stdout should provide
function return values.

This way the data-structures between Python submission and binary submission
are interchangeable. As a matter of fact you can even generate bson input/output
in python via [`simple_bson`](https://pypi.org/project/simple-bson/):

```python
import sys
import simple_bson

# problem functions defined here

if __name__ == "__main__":
    inputs = simple_bson.loads(sys.stdin.buffer.read())
    solutions = {k: globals()[k](**v) for k, v in inputs.items()}
    sys.stdout.buffer.write(simple_bson.dumps(solutions))
```

Also see provided example bson files:

- `bson.in`
- `bson.out`

### `setup.sh`

If you submit `setup.sh` along with your submission, this is a hook script
which should allow you to:

- install additional dependencies if you need to although this assignment
  should not require any external libraries and standard library should be
  sufficient.
- install necessary system dependencies in order to compile binary
  solution from submitted source code

This should just be a simple bash script:

```bash
#!/usr/bin/env bash
# do things here
```
