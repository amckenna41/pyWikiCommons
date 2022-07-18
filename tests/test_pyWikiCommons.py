################################################################################
###############             pyWikiCommons Module Tests           ###############
################################################################################
import os
import requests
import unittest

from pyWikiCommons import pyWikiCommons

class PyWikiCommonsTests(unittest.TestCase):

    def setUp(self) -> None:
        return super().setUp()
    
    def test_endpoints(self):
        """ Test API endpoints. """
        api_url = "https://commons.wikimedia.org/w/api.php"
        response = requests.get(api_url)        

        self.assertEqual(response.status_code, 200, f'Status code should be 200, got {response.status_code}')
        
    def test_download(self):
        pass
    
    def test_props(self):
        pass
    
    def test_iiprops(self):
        pass

    def tearDown(self) -> None:
        return super().tearDown()
