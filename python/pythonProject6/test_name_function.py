import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
    """测试name_function.py"""

    def test_first_last_name(self):
        """能够正确的处理像 Wu Yutian 这样的姓名么？"""
        formatted_name = get_formatted_name('wu', 'yutian')
        self.assertEqual(formatted_name, 'Wu Yutian')

    def test_first_last_middle_name(self):
        """能够正确处理像 Wolfang Amadeus Mozart 这样的姓名么？"""
        formatted_name = get_formatted_name('wolfang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfang Amadeus Mozart')

unittest.main()