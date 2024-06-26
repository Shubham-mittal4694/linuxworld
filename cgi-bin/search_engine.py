#!/usr/bin/env python3

import cgi
import cgitb
import webbrowser

# Enable CGI traceback for debugging
cgitb.enable()

# Print necessary headers including CORS headers
print("Content-Type: text/plain")
print("Access-Control-Allow-Origin: *")  # Allow requests from any origin (you can restrict it as needed)
print()  # Blank line required between headers and body

def search_google(search_query):
    webbrowser.open(f"https://www.google.com/search?q={search_query}")
    return f"Searched on Google: {search_query}"

def search_youtube(search_query):
    webbrowser.open(f"https://www.youtube.com/results?search_query={search_query}")
    return f"Searched on YouTube: {search_query}"

def main():
    form = cgi.FieldStorage()

    if "website" in form and "search" in form:
        website = form.getvalue("website")
        search_query = form.getvalue("search")

        if website == "google":
            result = search_google(search_query)
        elif website == "youtube":
            result = search_youtube(search_query)
        else:
            result = "Invalid website selection."
    else:
        result = "No website or search query provided."

    print(result)

if __name__ == "__main__":
    main()
