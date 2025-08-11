import uuid
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_uuid():
    """Generate a UUID and log the action."""
    new_uuid = uuid.uuid4()
    logging.info(f"Generated UUID: {new_uuid}")
    return new_uuid

if __name__ == "__main__":
    print("UUID Generator")
    print("==============")
    print(f"Generated UUID: {generate_uuid()}")