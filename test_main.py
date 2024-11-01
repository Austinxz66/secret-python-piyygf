import unittest
from main import SystemInfo

class TestSystemInfo(unittest.TestCase):
    def test_get_info(self):
        info = SystemInfo.get_info()
        self.assertIsInstance(info, dict)
        self.assertIn('python_version', info)
        self.assertIn('platform', info)
        self.assertIn('timestamp', info)
        self.assertIn('implementation', info)

if __name__ == '__main__':
    unittest.main()