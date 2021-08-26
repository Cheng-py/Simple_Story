import unittest

def sayhelo(to=None):
    if to:
        return "Hello %s!" %to
    return "Hello!"

class SayHelloTestCase(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_sayhello(self):
        rv = sayhelo()
        self.assertEqual(rv,'Hello!')

    def test_sayhello_to_somebody(self):
        rv = sayhelo(to="LaLaLa")
        self.assertEqual(rv,"Hello LaLaLa")

if __name__ == '__main__':
    unittest.main()