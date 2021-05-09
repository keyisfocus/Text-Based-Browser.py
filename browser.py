import argparse
import os
import sys

nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('directory')
args = arg_parser.parse_args()

if not os.access(args.directory, os.F_OK):
    os.mkdir(args.directory)

while True:
    user_input = input().lower()
    if user_input == 'exit':
        break
    if '.' not in user_input:
        print('Error')
        continue
    file_name = user_input[:user_input.index('.')]
    file_path = os.path.join(os.getcwd(), args.directory, file_name)

    if file_name in os.listdir(os.getcwd()):
        with open(os.path.join(os.getcwd(), args.directory, file_name), 'r') as file_in:
            print(file_in.read())
    else:
        try:
            content = globals()[user_input.replace('.', '_')]
            print(content)
            with open(os.path.join(os.getcwd(), args.directory, file_name), 'w') as file_out:
                file_out.write(content)
        except KeyError:
            print('Error, Not found')

