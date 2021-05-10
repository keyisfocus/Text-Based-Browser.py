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
The result of this task is the same as in the previous one, but now the program has a new feature:

1. The program should show the previous web page saved to a file if the user types `back`. Note that the last page you saved to a file is actually the current page; when the user types `back`, you should output the page that was before the current one. You can implement a stack to do this, but note that the current page should not be in that stack. For example, if the user inputs `bloomberg.com`, then `nytimes.com`, and then `back`, the user should see the content of `bloomberg.com`.
2. If there are no more pages in the browser history, don’t output anything. For example, if the first input of the user is the string `back`, your program shouldn't output anything.

## Stage 4
Keep the functionality from the previous stages and follow the same guidelines for file names. You don't need to keep the predefined variables with the content of web pages. Instead, add new features to the browser:

Your program should read the URL from the input as before, but now it should output the content of a real web page. Output the page with all the tags and text inside them. We'll get rid of tags in the next stage.
Since the user can input the URL without `https://` in the beginning, your browser should append this string if it is not there.

## Stage 5
In this stage, you need to extract and output the content between these tags. No more `<div>`, `<script>`, `<p>` and so on, just a clear readable text! Your browser should display only the content of a limited list of tags (`<p>`, headers, `<a>` and `<ul>`, `<ol>`, `<li>`) without showing the tags themselves.

Use the library `beautifulsoup4` to make these changes. This library is already installed in your project.

To pass the tests, it's enough to simply find the function allowing us to extract the human-readable text from a web page. If you’re curious, feel free to browse through some more information about parsing!

When an invalid URL is entered (URL without a dot and a top-level domain name), the program should output `Incorrect URL`.