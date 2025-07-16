import unittest
import json
import os
from helper_funcs import get_key_dict

class TestHelperFuncs(unittest.TestCase):
    def test_get_key_dict(self):
        # Create a temporary JSON file with the problematic key
        keys_data = {
            "0x0000": {
                "algid": "0xAA",
                "key": "0xc416c8c4c4"
            }
        }
        keys_file = "test_keys.json"
        with open(keys_file, "w") as f:
            json.dump(keys_data, f)

        # Call get_key_dict with the temporary file
        keys = get_key_dict(keys_file)

        # Assert that the key was parsed correctly
        self.assertIn(0, keys)
        self.assertEqual(keys[0]["algid"], 0xAA)
        self.assertEqual(keys[0]["key"], [0xc416c8c4c4])

        # Clean up the temporary file
        os.remove(keys_file)

if __name__ == "__main__":
    unittest.main()
