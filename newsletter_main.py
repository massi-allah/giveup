from SocialsBot.Telegram.main import Telegram
import json
import time

def load_quote_and_format_for_telegram_post(json_file_path):
    # Read JSON data from a file
    with open(json_file_path, 'r', encoding='utf-8') as file:
        quotes = json.load(file)

    # Convert JSON data to a list of formatted strings (quotes) for Telegram
    quotes_list = [
        f"Quote of the Day:\n\n\"{item['quote']}\"\n\n— {item['author']}"
        for item in quotes
    ]

    # Return the list of formatted quotes for Telegram
    return quotes_list

# Example usage
formatted_quotes = load_quote_and_format_for_telegram_post('./quotes.json')


if __name__ == "__main__":
    # Instantiate the Telegram class
    t = Telegram()
    # Send each formatted quote with a 4-hour delay in between
    for quote in formatted_quotes:
        t.sendMessage(quote)
        print("\n")  # Adds spacing between posts in the output

        # Delay for 4 hours (4 * 60 * 60 seconds)
        time.sleep(4 * 60 * 60)

