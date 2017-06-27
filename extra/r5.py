

import cmd

class SubInterpreter(cmd.Cmd):
    prompt = "(level2) "

    def do_subcommand_1(self, args):
        pass

    def do_subcommand_2(self, args):
        pass

    def do_quit(self, args):
        return True

    do_EOF = do_quit


class MyInterpreter(cmd.Cmd):
    def do_level1(self, args):
        pass

    def do_level2(self, args):
        sub_cmd = SubInterpreter()
        sub_cmd.cmdloop()

    def do_level3(self, args):
        pass

    def do_exit(self, *args):
        return True

my_cmd = MyInterpreter()
my_cmd.cmdloop()
