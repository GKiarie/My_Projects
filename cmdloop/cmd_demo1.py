import cmd
import os

class HelloWorld(cmd.Cmd):
    """Simple command processor example"""

    def do_greet(self, person):
        """greet[person]
        Greet named person"""
        if person:
            print(f"Hi, {person}")
        else:
            print("Hi")

    def do_EOF(self, line):
        return True

    def postloop(self):
        print("")

if __name__ == "__main__":
    HelloWorld().cmdloop()
