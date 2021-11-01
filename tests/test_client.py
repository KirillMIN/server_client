from client import create_presence, process_ans
from common.variables import RESPONSE, ERROR, USER, ACCOUNT_NAME, TIME, ACTION, PRESENCE
import unittest


class TestClient(unittest.TestCase):
    def test_create_presence(self):
        test = create_presence()
        test[TIME] = 1.1
        self.assertEqual(test, {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}})

    def test_ans_200(self):
        self.assertEqual(process_ans({RESPONSE: 200}), '200 : OK')

    def test_ans_400(self):
        self.assertEqual(process_ans({RESPONSE: 400, ERROR: 'Bad Request'}), '400 : Bad Request')

    def test_response(self):
        self.assertRaises(ValueError, process_ans, {ERROR: 'Bad Request'})