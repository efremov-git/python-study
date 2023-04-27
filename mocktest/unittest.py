import unittest
from unittest.mock import patch, Mock

import worker


class TestWorker(unittest.TestCase):
    def test_can_repeat(self):
        sleep_time = 7 * 60 * 60
        expected_result = False

        new_worker = worker.Worker('Tony')

        result = new_worker.can_repeat(sleep_time)

        self.assertEqual(expected_result, result)
