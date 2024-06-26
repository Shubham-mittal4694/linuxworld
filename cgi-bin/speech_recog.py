#!/usr/bin/env python3

import cgi
import cgitb
import pyttsx3
import sys

# Enable CGI traceback for debugging
cgitb.enable()

# Redirect stderr to stdout for debugging purposes
sys.stderr = sys.stdout

# Print necessary headers including CORS headers
print("Content-Type: text/plain")
print("Access-Control-Allow-Origin: *")  # Allow requests from any origin
print()  # Blank line required between headers and body

def text_to_speech(message):
    engine = pyttsx3.init()
    engine.say(message)
    engine.runAndWait()

def main():
    form = cgi.FieldStorage()

    if "message" in form:
        message = form.getvalue("message")
        try:
            text_to_speech(message)
            print(f"Success: The message '{message}' was spoken.")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Error: No message provided.")

if __name__ == "__main__":
    main()
