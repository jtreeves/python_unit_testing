import unittest
import consent

class TestConsent(unittest.TestCase):
    
    def test_proceed(self):
        self.assertEqual(consent.proceed(True), 'You may proceed.')
        self.assertEqual(consent.proceed(False), 'You may not proceed.')

    def test_extreme(self):
        self.assertEqual(consent.extreme('excited'), 'YAY!')
        self.assertEqual(consent.extreme('okay'), 'OK...')
        self.assertEqual(consent.extreme('angry'), 'BACK OFF!')

if __name__ == '__main__':
    unittest.main()