import datetime 
import unittest
from unittest.mock import Mock


def is_weekday():
    today = datetime.datetime.today()
    return (0 <= today.weekday() < 5)




class TestCalendar(unittest.TestCase):
    def test_is_weekday(self):

        # Mock datetime to control today's date
        datetime = Mock()

        tuesday = datetime.datetime(year=2019, month=1, day=1)
        datetime.datetime.today.return_value = tuesday
        # Test Tuesday is a weekday
        self.assertEqual(is_weekday(), True)


        saturday = datetime.datetime(year=2019, month=1, day=5)
        datetime.datetime.today.return_value = saturday
        # Test Saturday is not a weekday
        self.assertEqual(is_weekday(), False)


if __name__ == '__main__':
    unittest.main()
