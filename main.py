#!/usr/bin/python3
"""AirBnB Console - project entry point """

import cmd

class HBNBCommand(cmd.Cmd):
    """Class definition for HBNBCommand """

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, arg):
        """ Signal to exit the program """
        print('')
        return True

    def emptyline(self):
        """ Method to pass when emptyline entered """
        pass

    def do_create(self, arg):
    	print("args:", arg, len(arg))



if __name__ == '__main__':
    HBNBCommand().cmdloop()