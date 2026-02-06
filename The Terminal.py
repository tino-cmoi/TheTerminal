import os, keyboard, cursor, random, time

# ====== VARS ============================================================================================================================================================

colors = {
    "black" : 0, "red" : 1, "green" : 2, "yellow" : 3, "blue" : 4, "purple" : 5, "cyan" : 6, "white" : 7, "bright black" : 8, "bright red" : 9, "bright green" : 10, "bright yellow" : 11, "bright blue" : 12, "bright purple" : 13, "bright cyan" : 14, "bright white" : 15
}

# ====== DATA ============================================================================================================================================================

am_ac = {
    "name" : ["Alanine", "Arginine", "Asparagine", "Aspartic Acid", "Cysteine", "Glutamic Acid", "Glutamine", "Glycine", "Histidine", "Isoleucine", "Leucine", "Lysine", "Methionine", "Phenylalanine", "Proline", "Pyrrolysine", "Selenocysteine", "Serine", "Threonine", "Tryptophan", "Tyrosine", "Valine"],
    "3 letter code" : ["Ala", "Arg", "Asn", "Asp", "Cys", "Glu", "Gln", "Gly", "His", "Ile", "Leu", "Lys", "Met", "Phe", "Pro", "Pyl", "Sec", "Ser", "Thr", "Trp", "Tyr", "Val"],
    "letter" : ["A", "R", "N", "D", "C", "E", "Q", "G", "H", "I", "L", "K", "M", "F", "P", "O", "U", "S", "T", "W", "Y", "V"],
    "codons" : [["GCU", "GCC", "GCA", "GCG"], ["CGU", "CGC", "CGA", "CGG", "AGA", "AGG"], ["AAU", "AAC"], ["GAU", "GAC"], ["UGU", "UGC"], ["GAA", "GAG"], ["CAA", "CAG"], ["GGU", "GGC", "GGA", "GGG"], ["CAU", "CAC"], ["AUU", "AUC", "AUA"], ["UUA", "UUG", "CUU", "CUC", "CUA", "CUG"], ["AAA", "AAG"], ["AUG"], ["UUU", "UUC"], ["CCU", "CCC", "CCA", "CCG"], ["UAG"], ["UGA"], ["UCU", "UCC", "UCA", "UCG", "AGU", "AGC"], ["ACU", "ACC", "ACA", "ACG"], ["UGG"], ["UAU", "UAC"], ["GUU", "GUC", "GUA", "GUG"]],
    "polarity" : ["Nonpolar", "Basic", "Neutral", "Acidic", "Neutral", "Acidic", "Neutral", "Nonpolar", "Basic", "Nonpolar", "Nonpolar", "Basic", "Nonpolar", "Nonpolar", "Nonpolar", "Special", "Special", "Neutral", "Neutral", "Nonpolar", "Neutral", "Nonpolar"],
    "structure" : []
}

# ====== FUNCTIONS =======================================================================================================================================================

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def spc():
    print()

def write(text, color, bcolor, bold : bool, x : bool, f: bool):
    color = f'\033[38:5:{colors[color]}m' if color != "" else ''
    bcolor = f'\033[48:5:{colors[bcolor]}m' if bcolor != "" else ''
    bold = '\033[1m' if bold else ''

    if f:
        for char in text:
            print(f"{color}{bcolor}{bold}{char}\033[0m", end = "", flush = True)
            time.sleep(0.02)
    else:
        print(f"{color}{bcolor}{bold}{text}\033[0m", end = "", flush = True)
    print() if x else None

def title(text, color):
    clear()
    write(f" {text} ".center(50, "="), color, "", True, True, False)
    spc()
def choice(text, color, box):
    for i in range(len(text)):
        write(f"({i + 1}) {text[i]}", color, "", False, True, True)
    time.sleep(0.1)
    write(f"\033[{len(text)}A(1) {text[0]}".ljust(30), "black", color if color != "" else "white", True, False, False)
    x = 1
    while True:
        if (keyboard.is_pressed("up") or keyboard.is_pressed("haut")) and x > 1:
            write(f"\033[30D({x}) {text[x - 1]}".ljust(31), color, "", False, True, False)
            x -= 1
            write(f"\033[30D\033[2A({x}) {text[x - 1]}".ljust(35), "black", color if color != "" else "white", True, False, False)
            time.sleep(0.2)
        elif (keyboard.is_pressed("down") or keyboard.is_pressed("bas")) and x < len(text):
            write(f"\033[30D({x}) {text[x - 1]}".ljust(31), color, "", False, True, False)
            x += 1
            write(f"({x}) {text[x - 1]}".ljust(26), "black", color if color != "" else "white", True, False, False)
            time.sleep(0.2)#sqdqs
        elif keyboard.is_pressed("enter"):
            if x in box:
                write(f"{'\033[30D>>> '.ljust(31)}\033[22D", "black", color if color != "" else "white", True, False, False)
                search = ""
                while True:
                    key = keyboard.read_key()
                    if key == "up" or key == "haut" or key == "down" or key == "bas" or key == "esc": # exit search mode
                        write(f"\033[30D({x}) {text[x - 1]}".ljust(31), "black", color if color != "" else "white", True, False, False)
                        break
                    elif ((key.isalpha() and len(key) == 1) or key.isdecimal() or key == "space") and keyboard.is_pressed(key) and len(search) < 22: # writing search
                        if keyboard.is_pressed("shift") or keyboard.is_pressed("maj"):
                            key = key.upper()
                        search += key if key != "space" else " "
                        write(f"{key}" if key != "space" else " ", "black", color if color != "" else "white", True, False, False)
                    elif key == "backspace" and keyboard.is_pressed(key) and len(search) > 0: # deleting search
                        search = search[:-1]
                        write("\033[1D \033[1D", "black", color if color != "" else "white", True, False, False)
                    elif key == "enter" and keyboard.is_pressed(key): #searching
                        if x == 1: # search biology
                            results = []
                            for i in ["name", "3 letter code", "letter"]: # search am_ac
                                for j in range(len(am_ac[i])):
                                    results.append(j) if search.lower() == am_ac[i][j].lower() else None
                            for i in am_ac["codons"]:
                                for j in i:
                                    results.append(am_ac["codons"].index(i)) if search.upper() == j else None
                            results = ["Amino Acid", f"Name : {am_ac['name'][results[0]]}", f"3 Letter Code : {am_ac['3 letter code'][results[0]]}", f"Letter : {am_ac['letter'][results[0]]}", f"Codons : {', '.join(am_ac['codons'][results[0]])}", f"Polarity : {am_ac['polarity'][results[0]]}"] if results != [] else None
                        elif x == 2: # search chemistry
                            results = None
                        if type(results) == list: # show results
                            title("Search Results", color)
                            for i in results:
                                write(i, "", "", False, True, True)
                            spc()
                            if choice(["Back"], color, []) == 1: # back
                                return 0
                        else: # not in database
                            for i in range(3):
                                write(f"{f'\033[30D>>> {search}'.ljust(31)}\033[22D", "red", "", True, False, False)
                                time.sleep(0.15)
                                write(f"{'\033[30D'.ljust(31)}\033[22D", "black", "", True, False, False)
                                time.sleep(0.15)
                            write(f"{'\033[30D>>> '.ljust(31)}\033[22D", "black", color if color != "" else "white", True, False, False)
                        search = ""
            else: break
    return x


# ====== MAIN ============================================================================================================================================================

def main_menu(x):
    if x == 0:
        title("The Terminal", "")
        main_menu(choice(["Database", "Quiz", "Emotional Support", "Exit"], "", []))
    elif x == 1: database(0)
    elif x == 2: quiz(0)
    elif x == 3: emotional_support(0)
    elif x == 4: exit()

def database(x):
    if x == 0:
        title("Database", "")
        database(choice(["Search Biology", "Search Chemistry", "Back"], "", [1, 2]))
    elif x == 3: main_menu(0)

def quiz(x):
    if x == 0:
        title("Quiz", "")
        quiz(choice(["Biology", "Chemistry", "Back"], "", []))
    elif x == 1: quiz_biology(0)
    elif x == 2: pass
    elif x == 3: main_menu(0)
def quiz_biology(x):
    if x == 0:
        title("Biology Quiz", "")
        quiz_biology(choice(["Amino Acids", "Back"], "", []))
    elif x == 1:
        title("Amino Acids", "")
        list = ["Name", "3 Letter Code", "Letter", "Codons"]
        write("Choose question :", "", "", False, True, True)
        spc()
        question = choice(list, "", []) - 1
        for i in range(3): # flickering green
            write(f"{'\033[30D'.ljust(31)}\033[22D", "black", "", True, False, False)
            time.sleep(0.15)
            write(f"\033[30D({question + 1}) {list[question]}".ljust(31), "green", "", True, False, False)
            time.sleep(0.15)
        list.remove(list[question])
        list.append("Polarity")
        print(f"\033[{len(list) - question}B")
        write("Choose answer :", "", "", False, True, True)
        spc()
        answer = choice(list, "", []) - 1
        for i in range(3): # flickering green
            write(f"{'\033[30D'.ljust(31)}\033[22D", "black", "", True, False, False)
            time.sleep(0.15)
            write(f"\033[30D({answer + 1}) {list[answer]}".ljust(31), "green", "", True, False, False)
            time.sleep(0.15)
        print(f"\033[{len(list) - answer}B")
        write("Ready ?", "", "", False, True, True)
        spc()
        y = choice(["Start quiz", "Back"], "", [])
        if y == 1: pass
        elif y == 2: quiz_biology(0)
    elif x == 2: quiz(0)

def emotional_support(x):
    if x == 0:
        title("Emotional Support", "")
        emotional_support(choice(["Nothing here yet...", "Back"], "", []))
    elif x == 1:
        write("yo", "", "", False, True, True)
    elif x == 2: main_menu(0)

# ====== START ===========================================================================================================================================================

cursor.hide()
main_menu(0)