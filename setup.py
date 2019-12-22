# import mysql.connector
import os

# Class for setting up files, databases, tables, etc.
class Setup:
    def __init__(self):
        self.securityFolder = "KeyVault/"

    def KeyVaultCheck(self):
        if not os.path.isdir(self.securityFolder):
            try:
                os.mkdir(self.securityFolder)
            except OSError:
                print("Creation of KeyVault has failed")
            else:
                print("Created KeyVault")
        else:
            print("KeyVault Exists")
            


 

if __name__ == '__main__':
    Setup().KeyVaultCheck()
    print("done-done-done")

