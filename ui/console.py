class Ui:
    def __init__(self,controller):
        self._controller = controller

    def Read_Command(self):
        '''
        Read and parse user commands
        output:(command,args) tuple,where:
        command is user command
        args are arguments
        '''
        command = input("command:")
        pos = command.find(" ")
        if (pos == -1):
            # no parameteres
            return (command, "")
        # we have parameters
        cmd = command[:pos]
        args = command[pos:]
        args = args.split()
        args = [e.strip() for e in args]

        return (cmd, args)

    def start(self):
        # Entry point into the program
        # The list of commands
        cmds = {}
        while True:
            # User input consists of command and arguments
            (cmd, args) = self.Read_Command()
            if cmd == 'exit':
                break
            if cmd == 'ship':
                x = input ("Please enter placement:")
                x = list(x)
                self._controller.add_ship(str(x[0]),str(x[1]),str(x[2]),str(x[3]),str(x[4]),str(x[5]))
                self._controller.player_board(str(x[0]),str(x[1]),str(x[2]),str(x[3]),str(x[4]),str(x[5]))
            if cmd == 'start':
                string = "Player board:\n"
                string += "ABCDEF\n"
                string += "0"
                r0 = self._controller.getR0()
                for x in r0:
                    string += x
                string +='\n'
                string += "1"
                r1 = self._controller.getR1()
                for x in r1:
                    string += x
                string += '\n'
                string += "2"
                r2 = self._controller.getR2()
                for x in r2:
                    string += x
                string += '\n'
                string += "3"
                r3 = self._controller.getR3()
                for x in r3:
                    string += x
                string += '\n'
                string += "4"
                r4 = self._controller.getR4()
                for x in r4:
                    string += x
                string += '\n'
                string += "5"
                r5 = self._controller.getR5()
                for x in r5:
                    string += x
                string += '\n'
                print(string)

