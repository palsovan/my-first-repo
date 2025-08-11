import unittest
from uuid import UUID
from uuid_generator import generate_uuid
import logging

class TestUUIDGenerator(unittest.TestCase):
    def setUp(self):
        # Capture logs
        self.log_capture = logging.StringIO()
        self.handler = logging.StreamHandler(self.log_capture)
        logging.getLogger().addHandler(self.handler)

    def tearDown(self):
        # Remove log capture handler
        logging.getLogger().removeHandler(self.handler)

    def test_generate_uuid(self):
        # Test that a valid UUID is generated
        uuid = generate_uuid()
        self.assertIsInstance(uuid, UUID)

    def test_uuid_uniqueness(self):
        # Test that generated UUIDs are unique
        uuid1 = generate_uuid()
        uuid2 = generate_uuid()
        self.assertNotEqual(uuid1, uuid2)

    def test_logging(self):
        # Test that UUID generation is logged
        generate_uuid()
        log_output = self.log_capture.getvalue()
        self.assertIn("Generated UUID:", log_output)

if __name__ == '__main__':
    unittest.main()