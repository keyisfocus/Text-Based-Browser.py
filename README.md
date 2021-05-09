# Text-Based Browser https://hyperskill.org/projects/79

## Stage 1
1. You should write a program that takes a string from the user (URL) and outputs a "hard-coded" website with news (just a header and some text below).
The websites are presented as two variables in source code; you can see them in the template. These are mock versions of the sites `bloomberg.com` and `nytimes.com`. You just need to output them as a response to the corresponding input URL.
2. Also, you should add the option to quit the browser by typing `exit`. Real browsers don’t finish their work when they output a single web page, they are ready to accept a new URL at any moment. You should implement this behavior, too. An endless loop can help you with that part.

## Stage 2
In this stage, your program should:

* Accept a command-line argument which is a directory for saved tabs. For example, if the argument is `dir`, then you need to create a folder with the name `dir` and save all the web pages that the user downloads in this folder.
* Check if the user has entered a valid URL. It must contain at least one dot, for example, `bloomberg.com`. If the URL is incorrect, the browser should output an error message (it should contain the word error) and wait for another URL.
* In this task, your program can only access two web pages: `bloomberg.com` and `nytimes.com`. If the URL isn't either of these two, your program should output an error message.
* If the URL is valid, print the content of the web page and save it to a file in the aforementioned directory. You have two predefined variables with the content of the web pages that you should save: `bloomberg_com` and `nytimes_com`. The name of the file should correspond to the name of the web page. To get the name of the file, remove the last dot and everything that comes after it. This way, the file for the page `bloomberg.com` will be named `bloomberg`.
* Read the next input. If this input is the string `exit`, the program should stop running. If not, check if the string corresponds to the name of any file with a web page you saved before. If it does, print the content of this file. If it doesn't, check if the string is a new valid URL. If it is, repeat step 4. If it isn't, output an error message.

## Stage 3