import cmd

class HelloWorld(cmd.Cmd):
    prompt = '>>> '

    def do_greet(self, line):
        print("hello")

    def do_say_hi(self, line):
        print("Hey there user")

    def do_EOF(self, line):
        return True

if __name__ == "__main__":
    HelloWorld().cmdloop()
