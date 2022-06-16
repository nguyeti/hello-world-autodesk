from email import header
from src.logger import *
import unittest


class LoggerTestCase(unittest.TestCase):
    def test_index_get(self):
        """
            GIVEN a get_logger function
            WHEN get_logger is called with parameters
            THEN check that the logger object is created successfully
        """
        logger = get_logger("test_logger", "INFO")
        self.assertIsNotNone(logger)
        self.assertEqual(logger.getEffectiveLevel(), 20)


if __name__ == "__main__":
    unittest.main()
