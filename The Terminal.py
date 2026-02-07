import os, keyboard, cursor, random, time

# ====== VARS ============================================================================================================================================================

colors = {
    "black" : 0, "red" : 1, "green" : 2, "yellow" : 3, "blue" : 4, "purple" : 5, "cyan" : 6, "white" : 7, "bright black" : 8, "bright red" : 9, "bright green" : 10, "bright yellow" : 11, "bright blue" : 12, "bright purple" : 13, "bright cyan" : 14, "bright white" : 15
}

# ====== DATA ============================================================================================================================================================

am_ac = [
    {"name" : "Alanine",        "3 letter code" : "Ala",    "letter" : "A",     "codons" : ["GCU", "GCC", "GCA", "GCG"],                    "polarity" : "Nonpolar"},
    {"name" : "Arginine",       "3 letter code" : "Arg",    "letter" : "R",     "codons" : ["CGU", "CGC", "CGA", "CGG", "AGA", "AGG"],      "polarity" : "Basic"},
    {"name" : "Asparagine",     "3 letter code" : "Asn",    "letter" : "N",     "codons" : ["AAU", "AAC"],                                  "polarity" : "Neutral"},
    {"name" : "Aspartic Acid",  "3 letter code" : "Asp",    "letter" : "D",     "codons" : ["GAU", "GAC"],                                  "polarity" : "Acidic"},
    {"name" : "Cysteine",       "3 letter code" : "Cys",    "letter" : "C",     "codons" : ["UGU", "UGC"],                                  "polarity" : "Neutral"},
    {"name" : "Glutamic Acid",  "3 letter code" : "Glu",    "letter" : "E",     "codons" : ["GAA", "GAG"],                                  "polarity" : "Acidic"},
    {"name" : "Glutamine",      "3 letter code" : "Gln",    "letter" : "Q",     "codons" : ["CAA", "CAG"],                                  "polarity" : "Neutral"},
    {"name" : "Glycine",        "3 letter code" : "Gly",    "letter" : "G",     "codons" : ["GGU", "GGC", "GGA", "GGG"],                    "polarity" : "Nonpolar"},
    {"name" : "Histidine",      "3 letter code" : "His",    "letter" : "H",     "codons" : ["CAU", "CAC"],                                  "polarity" : "Basic"},
    {"name" : "Isoleucine",     "3 letter code" : "Ile",    "letter" : "I",     "codons" : ["AUU", "AUC", "AUA"],                           "polarity" : "Nonpolar"},
    {"name" : "Leucine",        "3 letter code" : "Leu",    "letter" : "L",     "codons" : ["UUA", "UUG", "CUU", "CUC", "CUA", "CUG"],      "polarity" : "Nonpolar"},
    {"name" : "Lysine",         "3 letter code" : "Lys",    "letter" : "K",     "codons" : ["AAA", "AAG"],                                  "polarity" : "Basic"},
    {"name" : "Methionine",     "3 letter code" : "Met",    "letter" : "M",     "codons" : ["AUG"],                                         "polarity" : "Nonpolar"},
    {"name" : "Phenylalanine",  "3 letter code" : "Phe",    "letter" : "F",     "codons" : ["UUU", "UUC"],                                  "polarity" : "Nonpolar"},
    {"name" : "Proline",        "3 letter code" : "Pro",    "letter" : "P",     "codons" : ["CCU", "CCC", "CCA", "CCG"],                    "polarity" : "Nonpolar"},
    {"name" : "Pyrrolysine",    "3 letter code" : "Pyl",    "letter" : "O",     "codons" : ["UAG"],                                         "polarity" : "Special"},
    {"name" : "Selenocysteine", "3 letter code" : "Sec",    "letter" : "U",     "codons" : ["UGA"],                                         "polarity" : "Special"},
    {"name" : "Serine",         "3 letter code" : "Ser",    "letter" : "S",     "codons" : ["UCU", "UCC", "UCA", "UCG", "AGU", "AGC"],      "polarity" : "Neutral"},
    {"name" : "Threonine",      "3 letter code" : "Thr",    "letter" : "T",     "codons" : ["ACU", "ACC", "ACA", "ACG"],                    "polarity" : "Neutral"},
    {"name" : "Tryptophan",     "3 letter code" : "Trp",    "letter" : "W",     "codons" : ["UGG"],                                         "polarity" : "Nonpolar"},
    {"name" : "Tyrosine",       "3 letter code" : "Tyr",    "letter" : "Y",     "codons" : ["UAU", "UAC"],                                  "polarity" : "Neutral"},
    {"name" : "Valine",         "3 letter code" : "Val",    "letter" : "V",     "codons" : ["GUU", "GUC", "GUA", "GUG"],                    "polarity" : "Nonpolar"},
]

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
            time.sleep(0.2)
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
                    elif key == "backspace" and keyboard.is_pressed(key) and len(search) > 0: # deleting char
                        search = search[:-1]
                        write("\033[1D \033[1D", "black", color if color != "" else "white", True, False, False)
                    elif key == "enter" and keyboard.is_pressed(key): #searching
                        if x == 1: # search biology
                            found = []
                            results = []
                            for i in range(22): # search am_ac
                                for j in ["name", "3 letter code", "letter"]:
                                    found.append(i) if search.lower() == am_ac[i][j].lower() else None
                                found.append(i) if search.upper() in am_ac[i]["codons"] else None
                            results += ["Amino Acid", f"Name : {am_ac[found[len(found) - 1]]['name']}", f"3 Letter Code : {am_ac[found[len(found) - 1]]['3 letter code']}", f"Letter : {am_ac[found[len(found) - 1]]['letter']}", f"Codons : {', '.join(am_ac[found[len(found) - 1]]['codons'])}", f"Polarity : {am_ac[found[len(found) - 1]]['polarity']}"] if type(found) == list else None                        
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
        title("Biology - Quiz", "")
        quiz_biology(choice(["Amino Acids", "Back"], "", []))
    elif x == 1:
        title("Amino Acids - Quiz", "")
        list = ["Name", "3 letter code", "Letter", "Codons", "Structure"]
        write("Choose question :", "", "", False, True, True)
        spc()
        question = choice(list, "", []) - 1
        for i in range(3): # flickering green
            write(f"{'\033[30D'.ljust(31)}\033[22D", "black", "", True, False, False)
            time.sleep(0.15)
            write(f"\033[30D({question + 1}) {list[question]}".ljust(31), "green", "", True, False, False)
            time.sleep(0.15)
        list.remove("Structure")
        list.append("Polarity")
        print(f"\033[{len(list) - question}B")
        question = list[question].lower()
        list.remove(question.capitalize())
        write("Choose answer :", "", "", False, True, True)
        spc()
        answer = choice(list, "", []) - 1
        for i in range(3): # flickering green
            write(f"{'\033[30D'.ljust(31)}\033[22D", "black", "", True, False, False)
            time.sleep(0.15)
            write(f"\033[30D({answer + 1}) {list[answer]}".ljust(31), "green", "", True, False, False)
            time.sleep(0.15)
        print(f"\033[{len(list) - answer}B")
        answer = list[answer].lower()
        write("Ready ?", "", "", False, True, True)
        spc()
        y = choice(["Start quiz", "Back"], "", [])
        if y == 1:
            title("Amino Aciids - Quiz", "")
            write("Associate the correct ", "", "", False, False, True)
            write(answer, "cyan", "", True, False, True)
            write(" to the given ", "", "", False, False, True)
            write(question, "purple", "", True, False, True)
            write(".", "", "", False, True, True)
            spc()
            list = am_ac
            random.shuffle(list)
            mistakes = 0
            for i in range(22):
                write(f"({i + 1}) {list[i][question]} -> ", "" , "", False, False, True)
                u_answer = ""
                while True:
                    key = keyboard.read_key()
                    if ((key.isalpha() and len(key) == 1) or key.isdecimal() or key == "space") and keyboard.is_pressed(key) and len(u_answer) < 15: # writing answer
                        if keyboard.is_pressed("shift") or keyboard.is_pressed("maj"):
                            key = key.upper()
                        u_answer += key if key != "space" else " "
                        write(f"{key}" if key != "space" else " ", "", "", True, False, False)
                    elif key == "backspace" and keyboard.is_pressed(key) and len(u_answer) > 0: # deleting char
                        u_answer = u_answer[:-1]
                        write("\033[1D \033[1D", "", "", True, False, False)
                    elif key == "enter" and keyboard.is_pressed(key): # submitting answer
                        if u_answer == list[i][answer]:
                            c = "green"
                        else:
                            c = "red"
                            mistakes += 1
                        for i in range(3): # flickering
                                write(f"\033[{len(u_answer)}D{u_answer}", "black", "", True, False, False)
                                time.sleep(0.15)
                                write(f"\033[{len(u_answer)}D{u_answer}", c, "", True, False, False)
                                time.sleep(0.15)
                        spc()
                        break
            spc()
            comment = "Did you even try ??!"
            if mistakes == 0: comment = "Perfect score !!"
            elif mistakes <= 5: comment = "Well done !"
            elif mistakes <= 10: comment = "Good."
            elif mistakes <= 15: comment = "Meh."
            write(f"{comment} You did {mistakes} mistakes.")
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