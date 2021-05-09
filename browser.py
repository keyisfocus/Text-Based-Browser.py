import argparse
import collections
import os
import requests


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
            content = requests.get(url).text
            with open(file_path, 'w', encoding='utf-8') as file_out:
                file_out.write(content)
            return content
        except KeyError:
            return 'Error, Not found'


while True:
    user_input = input().lower()
    if user_input == 'exit':
        break
    if user_input == 'back':
        if stack:
            current_page = stack.pop()
            print(get_content(current_page))
        continue
    if '.' not in user_input:
        print('Error')
        continue

    if current_page:
        stack.append(current_page)
    current_page = user_input if 'https://' in user_input else 'https://' + user_input
    print(get_content(current_page))

