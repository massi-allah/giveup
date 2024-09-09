from whatsapp_web import WhatsApp
import time

# Initialize WhatsApp
wp = WhatsApp()

# Open WhatsApp Web and display the QR code
wp.open_browser()

# Wait for 10 seconds to scan the QR code
time.sleep(10)

# Check if WhatsApp Web is logged in
if wp.is_logged_in():
    # Replace with your channel's phone number
    channel_phone_number = "+1234567890"

    # Replace with your message
    message = "Hello, this is a test message!"

    # Send the message
    wp.send_message(channel_phone_number, message)

    # Logout from WhatsApp Web
    wp.logout()
else:
    print("Failed to login to WhatsApp Web")