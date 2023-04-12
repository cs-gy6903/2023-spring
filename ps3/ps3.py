## -*- coding: utf-8 -*-
import typing


def problem1(data: bytes) -> bytes:
    """
    Compute an MD5 hash.

    Paremeters:
    |data|          is the message to compute a hash of

    >>> problem1(b'hello').hex()
    '5d41402abc4b2a76b9719d911017c592'
    """


def problem2(data: bytes) -> bytes:
    """
    Compute a SHA256 hash.

    Paremeters:
    |data|          the message to compute a hash of

    >>> problem2(b'hello').hex()
    '2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824'
    """


def problem3(digest_state: bytes, msg_len: int, data: bytes) -> bool:
    """
    Given the internal state of a MD5 digest, return True if it corresponds to an
    MD5 state after having processed a given message (and only that given message).

    Paremeters:
    |digest_state|  the internal state component representing the current hash value
    |msg_len|       the internal state component representing the length of the message
                    processed so far
    |data|          the message to test against the provided internal state

    >>> problem3(bytes.fromhex("00")*20, 3, b"foo")
    False
    >>> problem3(bytes.fromhex("acbd18db4cc2f85cedef654fccc4a4d8"), 3, b"foo")
    True
    """


def problem4(digest_state: bytes, msg_len: int, data: bytes) -> bool:
    """
    Given the internal state of a SHA256 digest, return True if it corresponds to a
    SHA256 state after having processed a given message (and only that given message).

    Paremeters:
    |digest_state|  the internal state component representing the current hash value
    |msg_len|       the internal state component representing the length of the message
                    processed so far
    |data|          the message to test against the provided internal state

    >>> problem4(bytes.fromhex("00")*32, 3, b"foo")
    False
    >>> problem4(bytes.fromhex("2c26b46b68ffc68ff99b453c1d30413413422d706483bfa0f98a5e886266e7ae"), 3, b"foo")
    True
    """


def problem5(key: bytes, data: bytes) -> bytes:
    """
    HMAC given data with the provided key using SHA256

    Parameters:
    |key|           secret key to use for computing the HMAC
    |data|          message to compute the MAC over

    >>> problem5(b'secret', b'data').hex()
    '1b2c16b75bd2a870c114153ccda5bcfca63314bc722fa160d690de133ccbb9db'
    """


def problem6(c1: bytes, c2: bytes, length: int, salt: bytes) -> (bytes, bytes):
    """
    Given 2 MD5-colliding messages, compute 2 new and distinct colliding messages of a
    required length, containing a required salt value.

    For directly relevant tips on how to solve this problem, refer to lecture material
    from April 5, and check out the sample colliding python scripts [included in this
    repo](../md5).

    Paramters:
    |c1|        a 128-byte message
    |c2|        a second, distinct, 128-byte message that MD5-hashes to the same value
                as |c1| (see included `assert` statement below the docstring)
    |length|    the required length of your output messages
    |salt|      a 32-byte message that you must include in your colliding output
                messages

    Return:     a 2-tuple with distinct bytes objects of length |length| each containing
                |salt| and with the same MD5 hash value. in other words if you're
                returning a tuple called ret, the following assert statement should
                pass: `assert ret[0] != ret[1] and problem1(ret[0]) == problem1(ret[1])`

    NOTE: there's no doctest included here because you're free to "fill" the file with
    whatever contents you like as long as the aforementioned constraints are satisfied.
    """
    assert problem1(c1) == problem1(c2) and c1 != c2
