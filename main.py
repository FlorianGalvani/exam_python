# check if the file is __main__ and run the main function
import sys
from start_message import StartMessage as SM
from part_one.main import PartOne as PO
from part_two.main import PartTwo as PT
from part_three.main import FlaskApp 

sm = SM()
po = PO()
pt = PT()

def startMessage():
    print(sm.getMessage())

def errorMessage(error):
    print(f"{error}")
    print("python main.py 1 | Exercice 1 : Traduction Thelassien -> Français")
    print("python main.py 2 | Exercice 2 : Dictionnaire vers JSON")
    print("python main.py 3 | Exercice 3 : FLASK APP - Informations système")

def main():
    startMessage()

    if len(sys.argv) > 1:
        if (sys.argv[1] == "1"):
            print(po.get_random_sentence())
        elif (sys.argv[1] == "2"):
            print(pt.get_person_json())
        elif (sys.argv[1] == "3"):
            FlaskApp.app.run()
        else :
            errorMessage("Invalid argument(s)")
    else:
        errorMessage("No argument(s) provided")
       

if __name__ == "__main__":
    main()

