# This Python file uses the following encoding: utf-8
from HelperFunctions.TerminalColors import TerminalColors as tc

debuggingActive: bool = True

# Text that should always be written in front of each debug message
debugPreamble = f"{tc.BOLD}{tc.OKBLUE}[DEBUG]{tc.ENDC} "

def debugPrint(*args):
    if debuggingActive is True:
        messageToBePrinted = debugPreamble

        # Add each argument to the message to be printed
        for argument in args:
            messageToBePrinted += str(argument) + " "

        # Print the final string
        print(messageToBePrinted)
