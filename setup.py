
import os
import pickle
import sqlite3

# Class for setting up files, databases, tables, etc.
class Setup:
    def __init__(self):
        self.securityFolder = "KeyVault/"
        self.dataFolder = "Data/"
        self.configFile = "config.p"
        self.databaseFile = "collection.db"

    def DirCheck_KeyVault(self):
        if not os.path.isdir(self.securityFolder):
            try:
                os.mkdir(self.securityFolder)
            except OSError:
                print("Creation of KeyVault has failed")
            else:
                print("Created KeyVault")
        else:
            print("KeyVault Exists")
            

    def DirCheck_Data(self):
        if not os.path.isdir(self.dataFolder):
            try:
                os.mkdir(self.dataFolder)
            except OSError:
                print("Creation of Data has failed")
            else:
                print("Created Data")
        else:
            print("Data Exists")


    def FileCheck_config(self, initConfig):
        if not os.path.isfile(self.configFile):
            try:
                pickle.dump(initConfig, open(self.configFile, "wb"))
            except OSError:
                print("Creation config.p has failed")
            else:
                print("Created config.p")
        else:
            print("config.p Exists")


    def FileCheck_database(self):
        if not os.path.isfile(self.databaseFile):
            try:
                connection = sqlite3.connect(self.databaseFile)
            except OSError:
                print("Creation of collection.db has failed")
            else:
                print("Created collection.db")
        else:
            print("collection.db Exists")

    
    def TableCheck(self, tableList):
        # Takes a list of duples; (tableName, tableSchema)

        connection = sqlite3.connect(self.databaseFile)
        print(f"connection to {self.databaseFile} openned")

        for t in tableList:
            query = f"create table if not exists {t[0]} ({t[1]})"
            connection.execute(query)
            print(f"{t[0]} created")

        connection.close()
        print(f"connection to {self.databaseFile} closed")



if __name__ == '__main__':
    config = {
        "publicKey": "9DA90D6C-1467-4FDD-AA76-AE6EEA9155FF",
        "privateKey": "6E42ADC9-C683-44AA-B3D8-5B01D0300EB7",
        "accessToken": "",
        "accessTokenExperation": ""
    }
    
    testList = [
        ("TableOne", "Id INT"),
        ("TableTwo", "Address CHAR(50)")
    ]

    Setup().TableCheck(testList)
    
    print("done-done-done")

