from unittest import TestCase

from app.main import main


class TestMain(TestCase):
    def test_can_call(self):
        main()
