# Graph theory project

## Introduction
Program in Python _to execute regular expressions on strings using an algorithm known as Thompson’s construction. Thompsons' construction is used to convert a regular expression to a NFA. This NFA is then used to match a String against the original regular expression. The main goal of this project is to accept a regular expression with the special characters to match it against an input string from the user.

## Setup
Developed and tested in python
https://github.com/JinaKim77/project.git

## how to install Python
Check this link.
https://realpython.com/installing-python/
1.	Open a browser window and navigate to the Download page for Windows at python.org.
2.	Underneath the heading at the top that says Python Releases for Windows, click on the link for the Latest Python 3 Release - Python 3.x.x. (As of this writing, the latest is Python 3.6.5.)
3.	Scroll to the bottom and select either Windows x86-64 executable installer for 64-bit or Windows x86 executable installer for 32-bit. 


## Test
This program  accept command line arguments.

### --help or -h : guides users how to run the program
<img src="images/help.PNG" width="800" >

### --version or -V : displays program version
<img src="images/version.PNG" width="800" >

### --description or -D : display program descriptions 
<img src="images/description.PNG" width="800" >

### --howtorun or -H : display how to run this program
<img src="images/howtorun.PNG" width="800" >

### --regex or -R : explain what the regular expression is
<img src="images/regex.PNG" width="1000" >

## How to run 
1. Firstly, when running the program, the user get a list of menu options.
   To select a menu option, enter the corresponding number for the user preference.
   As the main purpose of the program (project) is to match text string to infix regular expression,
   the user will enter infix regular expression that they want to check if it matches a string of        text. The expression should include any of the following special characters.
   
   #### ⬤ . : Concatenation operator. ( e.g. a.b : a followed by b )
   #### ⬤ | : Or operator. ( e.g. a|b : an a or a b
   #### ⬤ * : zero or more ( e.g. a* : any number of a's, including zero )
   #### ⬤ ? : zero or one
   #### ⬤ + : one or more
   
 2. Then the program will ask the user to enter string that they want to check.
 3. The program will output a True or False as to whether the string was matched against the             expression.

## Infix to postfix algorithm
The regex is read in infix notations that needs to be converted to postfix notation.
#
##### while there are more symbols to be read
  ##### if
#####    operand  -> output it.
#####      ')'    -> push it on the stack
#####      '('    -> pop operatiors from the stack to the output until a ')' is popped.
#####                you should make sure you do not output either of the parentheses.
#####    operator -> pop highter or equal precedence operators from the stack to the output.
#####                stop before popping a lower precedence operator or a ')'.
#####                push the operator on the stack.
#####   end if
##### end while
##### pop the remaining operators from the stack to the output

#
#
## References
#### ⬤ https://www.w3schools.com/python/python_regex.asp (To learn about regular expression)
#### ⬤ https://realpython.com/ (To learn about python)
#### ⬤ https://www.geeksforgeeks.org/infix-to-postfix-using-different-precedence-values-for-in-stack-and-out-stack/?ref=rp
#### ⬤ https://www.geeksforgeeks.org/stack-set-2-infix-to-postfix/
#### ⬤ https://www.includehelp.com/c/infix-to-postfix-conversion-using-stack-with-c-program.aspx //converting infix expression to postfix
#### ⬤ https://www.codeproject.com/Articles/405361/Converting-Postfix-Expressions-to-Infix //converting postfix expression to infix
#### ⬤ https://deniskyashif.com/2019/02/17/implementing-a-regular-expression-engine/
#### ⬤ https://docs.python.org/3/library/sys.html (System-specific parameters and functions)
#### ⬤ https://docs.python.org/3/library/getopt.html (C-style parser for command line options)
#### ⬤ https://docs.python.org/3/library/argparse.html (Parser for command-line options, arguments and sub-commands)
#### ⬤ https://docs.python.org/3/howto/argparse.html (Argparse Tutorial)
#### ⬤ https://stackabuse.com/command-line-arguments-in-python/ (Command Line Arguments)

