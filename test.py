import unittest
import spotbot

class TestSpotBot(unittest.TestCase):

    def test_create_content_pota(self):
        req_body = {"callsign":"KI7HSG", "source": "pota", "frequency": "14.074", "mode": "FT8", "wwffRef":"US-0052"}
        content = spotbot.create_content(req_body)
        expected = {'content': 'KI7HSG | [pota](https://api.pota.app/spot/comments/KI7HSG/US-0052) | freq: 14.074 | mode: FT8 | loc: US-0052', 'flags': 4}
        self.assertDictEqual(content, expected)

    def test_create_content_sota(self):
        req_body = {"callsign":"KI7HSG", "source": "sotawatch", "frequency": "14.074", "mode": "FT8", "summitRef": "ABCD"}
        content = spotbot.create_content(req_body)
        expected = {'content': 'KI7HSG | [sotawatch](https://sotl.as/activators/KI7HSG) | freq: 14.074 | mode: FT8 | loc: ABCD', 'flags': 4}
        self.assertDictEqual(content, expected)
        
    def test_create_spot_deeplink(self):
        self.assertTrue(False)
        
    def test_is_entity_recent(self):
        self.assertTrue(False)
        
    def test_call_target(self):
        self.assertTrue(False)
        
    def test_extract_message_id(self):
        self.assertTrue(False)

if __name__ == '__main__':
    unittest.main()
