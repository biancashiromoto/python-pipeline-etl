import requests
import json
import os

url = "https://quotes15.p.rapidapi.com/quotes/random/"

headers = {
    "X-RapidAPI-Key": "b35b97ea92mshadaf81eda7870a7p16784ajsn91cbac3dd5c6",
    "X-RapidAPI-Host": "quotes15.p.rapidapi.com",
}


def format_text(quote):
    content = quote["content"]
    author = quote["originator"]["name"]
    formatted_quote = f"""
"{content}",

                                            {author}
    """
    return formatted_quote


def save_quote(quote):
    if not os.path.exists("quotes.txt"):
        with open("quotes.txt", "w") as file:
            file.write(quote)
    else:
        with open("quotes.txt", "a") as file:
            file.write(quote)
            file.close()


def get_quote():
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        quote_data = response.json()
        formatted_quote = format_text(quote_data)
        print(formatted_quote)
        save_quote(formatted_quote)
    else:
        print(None)


get_quote()
