import unittest
from unittest.mock import patch, Mock
import requests
import sys 
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from geocode_function import geocode_ip, batch_ips_processing

class TestGeocodeFunctions(unittest.TestCase):

    @patch('geocode_function.requests.get')
    def test_geocode_ip_success(self, mock_get):
        # Mock a successful API response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"ip": "8.8.8.8", "country_name": "United States"}
        mock_get.return_value = mock_response

        result = geocode_ip("8.8.8.8")
        self.assertIsNotNone(result)
        self.assertEqual(result["ip"], "8.8.8.8")
        self.assertEqual(result["country_name"], "United States")

    @patch('geocode_function.requests.get')
    def test_geocode_ip_http_error(self, mock_get):
        # Mock an HTTP error response
        mock_get.side_effect = requests.exceptions.HTTPError("HTTP Error")
        
        result = geocode_ip("8.8.8.8")
        self.assertIsNone(result)

    def test_batch_ips_processing(self):
        with patch('geocode_function.geocode_ip') as mock_geocode_ip:
            mock_geocode_ip.side_effect = lambda ip: {"ip": ip, "country_name": "Testland"} if ip != "invalid" else None
            ip_addresses = ["8.8.8.8", "8.8.4.4", "invalid"]

            results = batch_ips_processing(ip_addresses, batch_size=2, delay=0)

            self.assertEqual(len(results), 2)
            self.assertEqual(results[0]['ip'], "8.8.8.8")
            self.assertEqual(results[1]['ip'], "8.8.4.4")
            self.assertNotIn({"ip": "invalid"}, results)

if __name__ == "__main__":
    unittest.main()
