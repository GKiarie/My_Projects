link: http://pymotw.com/2/cmd/#processing-commands
The cmd module contains one public class, Cmd, designed to be used as a base class for command processors such as interactive shells and other command interpreters.

By default it uses readline for interactive prompt handling, command line editing, and command completion.

Processing Commands
The interpreter uses a loop to read all lines from its input, parse them, and then dispatch the command to an appropriate command handler.
Input lines are parsed into two parts:
1. Command
2. Any other text on the line

e.g. If the user enters a command foo bar, and your class includes a method named do_foo(), it is called with "bar" as the only argument.

The end-of-file marker is dispatched to do_EOF(). If a command handler returns a true value, the program will exit cleanly. So to give a clean way to exit your interpreter, make sure to implement do_EOF() and have it return True.

$ python cmd_simple.py
(Cmd) -> This is the command prompt.

The prompt can be configured through the attribute prompt.
e.g. prompt = '(>>>) '

The prompt will show as:
$ python cmd_cimple.py
(>>>) -> This is the new prompt

The help command is built into Cmd. With no arguments, it shows the list of commands available. If you include a command you want help on, the output is more verbose and restricted to details of that command, when available.

If your class does not include a specific command processor for a command, the method default() is called with the entire input line as an argument. The built-in implementation of default() reports an error.

(Cmd) foo *** Unknown syntax: foo

Command Arguments

