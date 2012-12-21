from contextlib import contextmanager
import tempfile
import os


@contextmanager
def tmpfile():
    lolwut, fd = tempfile.mkstemp()
    try:
        yield fd
    finally:
        os.unlink(fd)
