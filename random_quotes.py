import requests
import json
import os

url = "https://quotes15.p.rapidapi.com/quotes/random/"

headers = {
    "X-RapidAPI-Key": "b35b97ea92mshadaf81eda7870a7p16784ajsn91cbac3dd5c6",
    "X-RapidAPI-Host": "quotes15.p.rapidapi.com",
}

def is_txt_file(file_name):
    return file_name.endswith(".txt")


def is_valid_file_name(file_name):
    return re.match(r"^[a-zA-Z0-9_.-]+$", file_name) is not None


def get_file_name():
    file_name = input("Type the name of the .txt file you want to save your quotes: ")
    return file_name


def format_text(quote):
    content = quote["content"]
    author = quote["originator"]["name"]
    formatted_quote = f"""
"{content}",

                                            {author}
    """
    return formatted_quote


def save_quote(quote):
    file_name = get_file_name()
    print(quote)
    if not os.path.exists(file_name):
        with open(file_name, "w") as file:
            file.write(quote)
    else:
        with open(file_name, "a") as file:
            file.write(quote)
            file.close()


def get_quote():
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        quote_data = response.json()
        formatted_quote = format_text(quote_data)
        save_quote(formatted_quote)
    else:
        print(None)


get_quote()
