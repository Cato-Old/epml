import string
import sys

from contextlib import contextmanager, redirect_stdout
from io import StringIO
from random import choice
from unittest import TestCase

from app.main import main


class TestCaseAssertionMixIn:
    @contextmanager
    def assertPrint(self) -> None:
        with redirect_stdout(tmp_stdout := StringIO()):
            yield (printed := [])
        printed.extend(tmp_stdout.getvalue().strip().split('\n'))


class TestMain(TestCase, TestCaseAssertionMixIn):
    def setUp(self) -> None:
        self.arg = ''.join(choice(string.ascii_letters) for _ in range(8))

    def test_prints_argument_on_standard_output(self) -> None:
        sys.argv.append(self.arg)
        with self.assertPrint() as printed:
            main()
        self.assertIn(self.arg, printed)

    def test_prints_warning_when_no_argument(self) -> None:
        warning = 'No required argument!'
        with self.assertPrint() as printed:
            main()
        self.assertIn(warning, printed)

    def tearDown(self) -> None:
        sys.argv = sys.argv[:1]
