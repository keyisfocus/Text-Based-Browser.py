import argparse
import collections
import os

import requests
from bs4 import BeautifulSoup, element
from colorama import Fore

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('directory')
args = arg_parser.parse_args()

if not os.access(args.directory, os.F_OK):
    os.mkdir(args.directory)

stack = collections.deque()
current_page = None


def get_content(url) -> str:
    file_name = url[8:url.rindex('.')]
    file_path = os.path.join(os.getcwd(), args.directory, file_name)
    if file_name in os.listdir(os.getcwd()):
        with open(file_path, 'r', encoding='utf-8') as file_in:
            return file_in.read()
    else:
        try:
            response = requests.get(url)
            if response:
                soup = BeautifulSoup(response.content, 'html.parser')
                content = []

                for tag in soup.find_all([f'h{i}' for i in range(1, 7)] + ['ul', 'ol', 'p', 'a']):
                    t = tag.text.strip()
                    if tag.name == 'a':
                        t = Fore.BLUE + t + Fore.RESET
                    content.append(t)

                content = os.linesep.join(content)
                with open(file_path, 'w', encoding='utf-8') as file_out:
                    file_out.write(content)
                return content
            else:
                return response.status_code
        except requests.exceptions.ConnectionError:
            return 'Incorrect URL'


while True:
    user_input = input().lower()
    if '.' in user_input:
        if current_page:
            stack.append(current_page)
        current_page = user_input if 'https://' in user_input else 'https://' + user_input
        print(get_content(current_page))

    elif user_input == 'exit':
        break
    elif user_input == 'back':
        if stack:
            current_page = stack.pop()
            print(get_content(current_page))
    else:
        print('Incorrect URL')
