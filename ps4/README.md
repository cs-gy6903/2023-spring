# Problem Set 4

This assignment will cover the basics of EC point arithmetic, then
put those primitives together to see how they can be used to implement
Elliptic Curve Diffie-Hellman (ECDH). All the math bits you need to
know are described pretty well on wikipedia's
[EC point multiplication][1] and [ECDH][2] pages.

See GradeScope for exact due-date of this assignment.

**NOTE**: For local testing in this pset, you'll need to install the
[`simple_bson` module][3]. You can do that with the following command:

```
$ pip3 install simple_bson
```

## Cheating

All the code you submit must be written by you. Submitting code written
by anyone else is cheating in the official sense. Please don't do that.

It's ok (and encouraged!) for students to work together by discussing
problems without sharing code. It's also ok to have someone look at your
code to help you debug a specific issue. But it's not ok to look at
someone else's code to copy it or to have anyone write code for you.
Please don't explore the gray area between these things.

For common operations like "open a file", "parse a JSON string", or
"call a library function", it's ok to copy two or three lines of code
from documentation, Stack Overflow, etc. But copying more than two or
three lines of code is probably not ok. If you do, you must clearly cite
your source in an inline comment that begins with COPIED. Citing your
source doesn't automatically make copying ok, but failing to cite your
source turns one violation into two violations. Please don't explore the
gray area of what counts as a "line of code".

## Problems

This assignment consists of 6 problems:

1. computing multiplicative inverse
1. negating EC point
1. adding EC points
1. doubling EC point (adding itself)
1. multiplying EC point
1. ECDH shared secret agreement

A couple of generic hints:

- there is no division. If you see division in the formula, instead
  multiply by multiplicative inverse
- don't forget to work in `mod p` -- always make sure your return values
  are mod `p`.
- for the `ecdh_agreement` problem , refer to ps2 and relevant lectures.
  ECDH is the same funamental problem as finite-field DH from ps2, just
  using a different multiplicative group (points on a prime curve
  instead of positive integers).

## Submission

Same methods apply as for the rest of the semester. You can submit in
Python or any language of your choice by using bson for stdout and bson
for stdout.

See [./ps4.py](./ps4.py) for all the function stubs.

[1]: https://en.wikipedia.org/wiki/Elliptic_curve_point_multiplication
[2]: https://en.wikipedia.org/wiki/Elliptic-curve_Diffie%E2%80%93Hellman#Key_establishment_protocol
[3]: https://pypi.org/project/simple-bson/
