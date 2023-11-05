# ChatConnect Pro: Seamless WhatsApp-ChatGPT Integration
# Auther: Muhammad Aitzaz
# Base Version: v1
"""Make some requests to OpenAI's chatbot"""

import time
import asyncio
import os 
import flask
import sys

from flask import g

from playwright.sync_api import Page
from playwright.sync_api import sync_playwright
from playwright.sync_api import Error

PROFILE_DIR = "/tmp/playwright" if '--profile' not in sys.argv else sys.argv[sys.argv.index('--profile') + 1]
PORT = 5001 if '--port' not in sys.argv else int(sys.argv[sys.argv.index('--port') + 1])
APP = flask.Flask(__name__)
PLAY = sync_playwright().start()
BROWSER = PLAY.firefox.launch_persistent_context(
    user_data_dir=PROFILE_DIR,
    headless=False,
)
PAGE = BROWSER.new_page()

def get_input_box():
    """Find the input box by searching for the largest visible one."""
    textareas = PAGE.query_selector_all("textarea")
    candidate = None
    for textarea in textareas:
        if textarea.is_visible():
            if candidate is None:
                candidate = textarea
            elif textarea.bounding_box().width > candidate.bounding_box().width:
                candidate = textarea
    return candidate

def is_logged_in():
    try:
        return get_input_box() is not None
    except AttributeError:
        return False

def send_message(message):
    # Send the message
    box = get_input_box()
    box.click()
    box.fill(message)
    box.press("Enter")
    while PAGE.query_selector(".result-streaming") is not None:
        time.sleep(0.1)

def get_last_message():
    """Get the latest message"""

    # Initialize last message and current message
    last_message = None
    current_message = None

    # Wait for the latest message to appear on the page
    while True:
        time.sleep(1)

        # Obtain the chatgpt_messages
        chatgpt_messages = PAGE.query_selector_all(".flex.flex-grow.flex-col.gap-3.max-w-full > div")

        # Iterate through the messages and find the last non-empty message
        for message in reversed(chatgpt_messages):
            if message.inner_text().strip():
                current_message = message.inner_text()
                break

        # If the current message is not equal to the last message, update the last message and continue waiting
        if current_message != last_message:
            last_message = current_message
            time.sleep(0.2)  # Add a small delay to reduce CPU usage
        else:
            break  # If the current message is equal to the last message, break the loop

    return last_message

@APP.route("/chat", methods=["GET"])
def chat():
    message = flask.request.args.get("q")
    print("Sending message: ", message)
    send_message(message)
    response = get_last_message()
    print("Response: ", response)
    return response

def start_browser():
    PAGE.goto("https://chat.openai.com/")
    APP.run(port=PORT, threaded=False)
    if not is_logged_in():
        print("Please log in to OpenAI Chat")
        print("Press enter when you're done")
        input()
    else:
        print("Logged in")
        
if __name__ == "__main__":
    start_browser()
