import socket
import threading
import time
import logging

# Logging config.
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# Creating Notifications Client
notifications_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Attempt to connect to the server
try:
    notifications_client.connect(('localhost', 8500))
    logging.info("Connected to the server successfully.")
except ConnectionRefusedError:
    logging.error("Failed to connect to the server. Ensure the server is running.")
    exit(1)

# List of notification_messages.
notification_messages = [
    'Welcome to this amazing app!',
    'Your account was successfully created!',
    'You can explore about many options acordingly to your desires and necesities.',
    'Do you need some help? we can guide you through this app.',
    'You made up your first report, congratulations.',
    'Working in a teamwork environment could be better, we invite you to explore these few tips to start with.',
]


def send_notification_messages(notifications_list:list=notification_messages) -> None:
    """
    Sends notification messages to the server every 6 seconds.

    Args:
        notifications_list (list): List of notification messages to send.
    """

    try:
        # Send a notification message to the server every 6 seconds.
        for notification in notifications_list:
            notifications_client.send(f'{notification}'.encode('utf-8'))
            time.sleep(6)
        
        logging.warning(msg='Every notification was sent to the server.')
    except (ConnectionError, BrokenPipeError) as e:
        logging.error(f'Connection error ocurred: {e}')
    finally:
        for s in range(3):
            logging.warning(msg=f'Closing notifications client connection in {s} seconds.')
            time.sleep(1)

        notifications_client.close()
        logging.info("Notifications client connection closed.")

threading.Thread(target=send_notification_messages, daemon=True).start()