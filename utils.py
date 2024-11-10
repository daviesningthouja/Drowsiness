from Adafruit_IO import Client
import cv2

# Adafruit IO credentials
ADAFRUIT_IO_USERNAME = 'davies66'
ADAFRUIT_IO_KEY = 'aio_OUCn18b3bovy3fSSYxZZmNL0e1CB'

# Initialize Adafruit IO client
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

def update_eye_status(status):
    """Publish the eye status to Adafruit IO."""
    aio.send('eye-status', status)
    print(f"Eye status sent to Adafruit IO: {status}")
