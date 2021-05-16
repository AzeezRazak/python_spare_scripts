import os
from datetime import datetime
import collections


def clearScreen():
    print("Invalid entry!")
    os.system('cls')
    main() 

class gba:
    def __init__(self):
        #self.plants = {}
        #self.plant_toModify = str()
        #self.plant_toDelete = str()
        pass

    def read_file(self):
        
        with open("myplants.txt") as f:
            lines = f.readlines()
        plants = {}
        current_key = None
        for line in lines:
            line = line.strip()
            if not line:
                current_key = None
            elif not current_key:
                current_key = line
                plants[current_key] = []
            else:
                plants[current_key].append(line)

        self.plants = plants
        self.main_menu()
        
    def main_menu(self):
        
        print("Welcome to the plants repository.")
        print("You can either (A)dd, (M)odify the details for plants, (S)earch for plant name or (D)isplay the houseplants")
        varChoice = str(input("Whats your choice for now? (A,M,S,D) ").upper())  
        
        self.Choice = varChoice

        if self.Choice == 'A':
            self.add_plant()
        elif self.Choice == 'M':
            self.modify_plant()
        elif self.Choice == 'S':
            self.search_plant()
        elif self.Choice == 'D':
            self.display_plant()
        elif (RuntimeError, TypeError, NameError):
            clearScreen()
            self.main_menu()
        
        
    def add_plant(self):
        print("Adding plants")
        print("\n")
        print("The plants currently in the database are :")
        for (key) in self.plants.items(): print(key)
        
        add_plants = str(input("Please enter new plant name: "))
        self.plants[add_plants] = [datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
        for (key,val) in self.plants.items(): print(key)
        self.plant_toModify = add_plants
        self.print_plant()
        

        nextStep = str(input("Would you like to add any information to your new plant? (Y)es or (N)o").upper())
        if nextStep == 'Y':
            self.modify_plant()
        elif (RuntimeError, TypeError, NameError):
            self.footer_menu()
        
        
    def modify_plant(self):
        print("Here you can modify the database, add entry to your plants, delete entries and delete plants")
        print("Here is the database for the plants")
        for (key) in self.plants.items(): print(key)
        
        print("\n"," Choose 1 to add entry to a plant, 2 to delete entry to a existing plant and 3 to delete a plant including its entries")
        modifyMenuChoice = int(input("Your option : "))
        if modifyMenuChoice == 1:
            plantInput = str(input("Which plant would you like to add information to? "))
            if plantInput in self.plants.keys(): 
                self.plant_toModify = plantInput
                self.entry()
            elif (RuntimeError, TypeError, NameError):
                self.modify_plant()
        elif modifyMenuChoice == 2:
            self.delete_entry()
            
        elif modifyMenuChoice == 3:
            self.delete_plant()
        elif (RuntimeError, TypeError, NameError):
            self.modify_plant()

    def entry(self):
        entryInput = input("What information would you like to add to your plant? ")
        self.plants[self.plant_toModify].append(entryInput)
        self.print_plant()
        
        choiceToEnd = str(input("Would you like to add on? (Y)es or (N)o ").upper())
        if (choiceToEnd == 'Y'):
            self.entry()
        elif (choiceToEnd == 'N'):
            self.footer_menu()
        elif (RuntimeError, TypeError, NameError):
            self.footer_menu()

    def delete_plant(self):
        
        deleteInput = input("Kindly enter your selection for deletion. ")
        
            
        del self.plants[deleteInput]
        self.print_plant()
            

        self.footer_menu()

    def delete_entry(self):

        plantInput = str(input("Which plant would you like to delete information of? "))
        if plantInput in self.plants.keys(): 
            
            print("\n The details of the plant ", plantInput, " is follows")
            print("# \t Detail")
            i=0
            for (val) in self.plants[plantInput]: 
                print(i,"\t",val)
                i=i+1
            
            deletionInput = int(input("Line Number # "))
            self.plants[plantInput].pop(deletionInput)
            self.print_plant()
            
        
        elif (RuntimeError, TypeError, NameError):
                self.delete_entry()

        self.footer_menu()
        
    def search_plant(self):
        print("Search for plants and display")

        argPlants = str(input("Which plant would you like to search? "))
        if argPlants in self.plants.keys():
            
            print("Plant is present in the database")
            print('Plant is : ', argPlants, self.plants[argPlants])
        else:
            print("Not present")

        self.footer_menu()
        
    def footer_menu(self):
        varChoiceA = str(input("Are you done? Y or N (N to go back to first menu)").upper())  
        if (varChoiceA == 'Y'):
            self.print_plant()
        elif (varChoiceA == 'N'):
            clearScreen()
            self.main_menu
        elif (RuntimeError, TypeError, NameError):
            clearScreen()
            self.footer_menu()

    def display_plant(self):
        print("Display the plants")

        sorted_dict_abc = {k: self.plants[k] for k in sorted(self.plants)}
        sorted_dict_time = sorted(self.plants.items(), key=lambda p: p[1], reverse=True)
        sorted_dict_time_d = collections.OrderedDict(sorted_dict_time)
        
        print("Choose 1 if you want to display according to letters, 2 accordingly to time and 3 to display all")
        display_menuChoice = int(input("Your option : "))
        if display_menuChoice == 1:
            for (key,val) in sorted_dict_abc.items(): print(key, "->", val)
        elif display_menuChoice == 2:
            for (key,val) in sorted_dict_time_d.items(): print(key, "->", val)
        elif display_menuChoice == 3:
            for (key,val) in sorted_dict_abc.items(): print(key, "->", val)
            print("-------------------------------------------------")
            for (key,val) in sorted_dict_time_d.items(): print(key, "->", val)
        elif (RuntimeError, TypeError, NameError):
            self.display_plant()

        
        self.footer_menu()
        

    def print_plant(self):

        f = open("myplants.txt", "a")
        
        for (key,val) in self.plants.items():
            
            f.writelines([str(key),"\n"])
            #print(str(val), "\n")
            for t in range(len(val)):
                f.writelines([str(val[t]),"\n"])
            f.writelines("\n")

        f.close()
        



def main():

    file_exists = os.path.isfile("myplants.txt")
    callON = gba()
    if file_exists:
        callON.read_file()
    else:
        print("Kindly check if myplants.txt is in the same folder")

        
if __name__ == "__main__":
    main()
