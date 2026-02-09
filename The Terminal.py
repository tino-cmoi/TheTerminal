import os, keyboard, cursor, random, time

# ====== VARS ============================================================================================================================================================

colors = {
    "black" : 0, "red" : 1, "green" : 2, "yellow" : 3, "blue" : 4, "purple" : 5, "cyan" : 6, "white" : 7, "bright black" : 8, "bright red" : 9, "bright green" : 10, "bright yellow" : 11, "bright blue" : 12, "bright purple" : 13, "bright cyan" : 14, "bright white" : 15
}

# ====== DATA ============================================================================================================================================================

nucleotids = []
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
aldoses = [
    {"name" : "Glyceraldehyde",    "type" : "Triose",     "structure" : "\n    CHO\n    |\n H——+——\033[38:5:3mOH\033[0m\n    |\n    CH₂OH\n"},
    {"name" : "Erythrose",         "type" : "Tetrose",    "structure" : "\n    CHO\n    |\n H——+——\033[38:5:3mOH\033[0m\n    |\n H——+——\033[38:5:3mOH\033[0m\n    |\n    CH₂OH\n"},
    {"name" : "Threose",           "type" : "Tetrose",    "structure" : "\n    CHO\n    |\n\033[38:5:3mHO\033[0m——+——H\n    |\n H——+——\033[38:5:3mOH\033[0m\n    |\n    CH₂OH\n"},
    {"name" : "Ribose",            "type" : "Pentose",    "structure" : "\n    CHO\n    |\n H——+——\033[38:5:3mOH\033[0m\n    |\n H——+——\033[38:5:3mOH\033[0m\n    |\n H——+——\033[38:5:3mOH\033[0m\n    |\n    CH₂OH\n"},
    {"name" : "Arabinose",         "type" : "Pentose",    "structure" : "\n    CHO\n    |\n\033[38:5:3mHO\033[0m——+——H\n    |\n  H——+——\033[38:5:3mOH\033[0m\n    |\n H——+——\033[38:5:3mOH\033[0m\n    |\n    CH₂OH\n"},
    {"name" : "Xylose",            "type" : "Pentose",    "structure" : "\n    CHO\n    |\n H——+——\033[38:5:3mOH\033[0m\n    |\n\033[38:5:3mHO\033[0m——+——H\n    |\n H——+——\033[38:5:3mOH\033[0m\n    |\n    CH₂OH\n"},
    {"name" : "Lyxose",            "type" : "Pentose",    "structure" : "\n    CHO\n    |\n\033[38:5:3mHO\033[0m——+——H\n    |\n\033[38:5:3mHO\033[0m——+——H\n    |\n H——+——\033[38:5:3mOH\033[0m\n    |\n    CH₂OH\n"},
    {"name" : "Allose",            "type" : "Hexose",     "structure" : "\n    CHO\n    |\n H——+——\033[38:5:3mOH\033[0m\n    |\n H——+——\033[38:5:3mOH\033[0m\n    |\n H——+——\033[38:5:3mOH\033[0m\n    |\n H——+——\033[38:5:3mOH\033[0m\n    |\n    CH₂OH\n"},
    {"name" : "Altrose",           "type" : "Hexose",     "structure" : "\n    CHO\n    |\n\033[38:5:3mHO\033[0m——+——H\n    |\n H——+——\033[38:5:3mOH\033[0m\n    |\n H——+——\033[38:5:3mOH\033[0m\n    |\n H——+——\033[38:5:3mOH\033[0m\n    |\n    CH₂OH\n"},
    {"name" : "Glucose",           "type" : "Hexose",     "structure" : "\n    CHO\n    |\n H——+——\033[38:5:3mOH\033[0m\n    |\n\033[38:5:3mHO\033[0m——+——H\n    |\n H——+——\033[38:5:3mOH\033[0m\n    |\n H——+——\033[38:5:3mOH\033[0m\n    |\n    CH₂OH\n"},
    {"name" : "Mannose",           "type" : "Hexose",     "structure" : "\n    CHO\n    |\n\033[38:5:3mHO\033[0m——+——H\n    |\n\033[38:5:3mHO\033[0m——+——H\n    |\n H——+——\033[38:5:3mOH\033[0m\n    |\n H——+——\033[38:5:3mOH\033[0m\n    |\n    CH₂OH\n"},
    {"name" : "Gulose",            "type" : "Hexose",     "structure" : "\n    CHO\n    |\n H——+——\033[38:5:3mOH\033[0m\n    |\n H——+——\033[38:5:3mOH\033[0m\n    |\n\033[38:5:3mHO\033[0m——+——H\n    |\n H——+——\033[38:5:3mOH\033[0m\n    |\n    CH₂OH\n"},
    {"name" : "Idose",             "type" : "Hexose",     "structure" : "\n    CHO\n    |\n\033[38:5:3mHO\033[0m——+——H\n    |\n H——+——\033[38:5:3mOH\033[0m\n    |\n\033[38:5:3mHO\033[0m——+——H\n    |\n H——+——\033[38:5:3mOH\033[0m\n    |\n    CH₂OH\n"},
    {"name" : "Galactose",         "type" : "Hexose",     "structure" : "\n    CHO\n    |\n H——+——\033[38:5:3mOH\033[0m\n    |\n\033[38:5:3mHO\033[0m——+——H\n    |\n\033[38:5:3mHO\033[0m——+——H\n    |\n H——+——\033[38:5:3mOH\033[0m\n    |\n    CH₂OH\n"},
    {"name" : "Talose",            "type" : "Hexose",     "structure" : "\n    CHO\n    |\n\033[38:5:3mHO\033[0m——+——H\n    |\n\033[38:5:3mHO\033[0m——+——H\n    |\n\033[38:5:3mHO\033[0m——+——H\n    |\n H——+——\033[38:5:3mOH\033[0m\n    |\n    CH₂OH\n"}
]
cetoses = [ 
    {"name" : "Dihydroxyacetone",  "type" : "Triose",     "structure" : "\n    CH₂OH\n    |\n    |==O\n    |\n    CH₂OH\n"},
    {"name" : "Erythrulose",       "type" : "Tetrose",    "structure" : "\n    CH₂OH\n    |\n    |==O\n    |\n H——+——\033[38:5:3mOH\033[0m\n    |\n    CH₂OH\n"},
    {"name" : "Ribulose",          "type" : "Pentose",    "structure" : "\n    CH₂OH\n    |\n    |==O\n    |\n H——+——\033[38:5:3mOH\033[0m\n    |\n H——+——\033[38:5:3mOH\033[0m\n    |\n    CH₂OH\n"},
    {"name" : "Xylulose",          "type" : "Pentose",    "structure" : "\n    CH₂OH\n    |\n    |==O\n    |\n\033[38:5:3mHO\033[0m——+——H\n    |\n H——+——\033[38:5:3mOH\033[0m\n    |\n    CH₂OH\n"},
    {"name" : "Psicose",           "type" : "Hexose",     "structure" : "\n    CH₂OH\n    |\n    |==O\n    |\n H——+——\033[38:5:3mOH\033[0m\n    |\n H——+——\033[38:5:3mOH\033[0m\n    |\n H——+——\033[38:5:3mOH\033[0m\n    |\n    CH₂OH\n"},
    {"name" : "Fructose",          "type" : "Hexose",     "structure" : "\n    CH₂OH\n    |\n    |==O\n    |\n\033[38:5:3mHO\033[0m——+——H\n    |\n H——+——\033[38:5:3mOH\033[0m\n    |\n H——+——\033[38:5:3mOH\033[0m\n    |\n    CH₂OH\n"},
    {"name" : "Sorbose",           "type" : "Hexose",     "structure" : "\n    CH₂OH\n    |\n    |==O\n    |\n H——+——\033[38:5:3mOH\033[0m\n    |\n\033[38:5:3mHO\033[0m——+——H\n    |\n H——+——\033[38:5:3mOH\033[0m\n    |\n    CH₂OH\n"},
    {"name" : "Tagatose",          "type" : "Hexose",     "structure" : "\n    CH₂OH\n    |\n    |==O\n    |\n\033[38:5:3mHO\033[0m——+——H\n    |\n\033[38:5:3mHO\033[0m——+——H\n    |\nH——+——\033[38:5:3mOH\033[0m\n    |\n    CH₂OH\n"} 
]

p_table = [
    {"name" : "Hydrogen",    "atom" : "H",     "ion" : "H⁺",       "mass": 1.0078,    "Valence" : [1]},
    {"name" : "Helium",      "atom" : "He",    "ion" : "He²⁺",     "mass": 4.0026,    "Valence" : [2]},
    {"name" : "Lithium",     "atom" : "Li",    "ion" : "Li⁺",      "mass": 6.9410,    "Valence" : [1]},
    {"name" : "Berylium",    "atom" : "Be",    "ion" : "Be²⁺",     "mass": 9.0122,    "Valence" : [2]},
    {"name" : "Bore",        "atom" : "B",     "ion" : "B",        "mass": 10.811,    "Valence" : [3]},
    {"name" : "Carbon",      "atom" : "C",     "ion" : "C",        "mass": 12.011,    "Valence" : [4]},
    {"name" : "Nitrogen",    "atom" : "N",     "ion" : "N³⁻",      "mass": 14.007,    "Valence" : [5]},
    {"name" : "Oxygen",      "atom" : "O",     "ion" : "O²⁻",      "mass": 15.999,    "Valence" : [6]},
    {"name" : "Fluor",       "atom" : "F",     "ion" : "F⁻",       "mass": 18.998,    "Valence" : [7]},
    {"name" : "Neon",        "atom" : "Ne",    "ion" : "Ne",       "mass": 20.180,    "Valence" : [8]},
    {"name" : "Sodium",      "atom" : "Na",    "ion" : "Na⁺",      "mass": 22.990,    "Valence" : [1]},
    {"name" : "Magnesium",   "atom" : "Mg",    "ion" : "Mg²⁺",     "mass": 24.305,    "Valence" : [2]},
    {"name" : "Aluminium",   "atom" : "Al",    "ion" : "Al³⁺",     "mass": 26.982,    "Valence" : [3]},
    {"name" : "Silicium",    "atom" : "Si",    "ion" : "Si",       "mass": 28.086,    "Valence" : [4]},
    {"name" : "Phophorus",   "atom" : "P",     "ion" : "P³⁻",      "mass": 30.974,    "Valence" : [5]},
    {"name" : "Sulfur",      "atom" : "S",     "ion" : "S²⁻",      "mass": 32.065,    "Valence" : [6]},
    {"name" : "Chlore",      "atom" : "Cl",    "ion" : "Cl⁻",      "mass": 35.453,    "Valence" : [7]},
    {"name" : "Argon",       "atom" : "Ar",    "ion" : "Ar",       "mass": 39.948,    "Valence" : [8]},
    {"name" : "Potassium",   "atom" : "K",     "ion" : "K⁺",       "mass": 39.098,    "Valence" : [1]},
    {"name" : "Calcium",     "atom" : "Ca",    "ion" : "Ca²⁺",     "mass": 40.078,    "Valence" : [2]},
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
                            found = None
                            results = []
                            for i in range(22): # search am_ac
                                for j in ["name", "3 letter code", "letter"]:
                                    if search.lower() == am_ac[i][j].lower(): found = i 
                                if search.upper() in am_ac[i]["codons"]: found = i
                                if type(found) == int : results += ["Amino Acid", f"Name : {am_ac[found]['name']}", f"3 Letter Code : {am_ac[found]['3 letter code']}", f"Letter : {am_ac[found]['letter']}", f"Codons : {', '.join(am_ac[found]['codons'])}", f"Polarity : {am_ac[found]['polarity']}", ""]                      
                                found = None
                            for i in range(15): #search aldoses
                                for j in ["name", "type"]:
                                    if search.lower() == aldoses[i][j].lower(): found = i
                                if type(found) == int : results += ["Aldose", f"Name : {aldoses[found]['name']}", f"Type : {aldoses[found]['type']}", "Structure :", f" {aldoses[found]['structure']}"]
                                found = None
                            for i in range(8): #search cetoses
                                for j in ["name", "type"]:
                                    if search.lower() == cetoses[i][j].lower(): found = i
                                if type(found) == int : results += ["Cetose", f"Name : {cetoses[found]['name']}", f"Type : {cetoses[found]['type']}", "Structure :", f" {cetoses[found]['structure']}"]
                                found = None
                        elif x == 2: # search chemistry
                            results = []
                        if results != []: # show results
                            title("Search Results", color)
                            for i in results:
                                write(i, "", "", False, True, False if i[slice(0, 1)] == " " else True)
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
        main_menu(choice(["Database", "Quiz", "Calculator", "Exit"], "", []))
    elif x == 1: database(0)
    elif x == 2: quiz(0)
    elif x == 3: calculator(0)
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
    elif x == 2: quiz(0)
    elif x == 3: main_menu(0)
def quiz_biology(x):
    if x == 0:
        title("Biology - Quiz", "")
        quiz_biology(choice(["Amino Acids", "Glucids", "Back"], "", []))
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
            write(answer, "bright cyan", "", True, False, True)
            write(" to the given ", "", "", False, False, True)
            write(question, "bright purple", "", True, False, True)
            write(".", "", "", False, True, True)
            spc()
            list = am_ac
            random.shuffle(list)
            mistakes = 0
            for i in range(22):
                write(f"({i + 1}) {list[i][question]} >> ", "" , "", False, True if question == "structure" else False, False if question == "structure" else True)
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
                        if u_answer.lower() == list[i][answer].lower():
                            c = "green"
                        else:
                            c = "red"
                            mistakes += 1
                        for j in range(3): # flickering
                                write(f"\033[{len(u_answer) + 3}D{">> " + list[i][answer] if c == "green" else ">> " + u_answer}", "black", "", True, False, False)
                                time.sleep(0.15)
                                write(f"\033[{len(u_answer) + 3}D{">> " + list[i][answer] if c == "green" else ">> " + u_answer}", c, "", True, False, False)
                                time.sleep(0.15)
                        spc()
                        break
            spc()
            comment = "Did you even try ??!"
            if mistakes == 0: comment = "Perfect score !!"
            elif mistakes <= 5: comment = "Well done !"
            elif mistakes <= 10: comment = "Good."
            elif mistakes <= 15: comment = "Meh."
            write(f"{comment} You did {mistakes} mistake." if mistakes == 1 else f"{comment} You did {mistakes} mistakes.", "", "", False, True, True)
            spc()
            quiz_biology(1) if choice(["Again", "Back"], "", []) == 1 else quiz_biology(0)
        elif y == 2: quiz_biology(0)
    elif x == 2:
        title("Glucids - Quiz", "")
        write("Which family of glucids would you like to study ?", "", "", False, True, True)
        spc()
        theme = choice(["Aldoses", "Cetoses", "Both"], "", [])
        for i in range(3): # flickering green
            write(f"{'\033[30D'.ljust(31)}\033[22D", "black", "", True, False, False)
            time.sleep(0.15)
            write(f"\033[30D({theme}) {"Aldoses" if theme == 1 else "Cetoses" if theme == 2 else "Both"}", "green", "", True, False, False)
            time.sleep(0.15)
        print(f"\033[{4 - theme}B")
        write("Ready ?", "", "", False, True, True)
        spc()
        y = choice(["Start quiz", "Back"], "", [])
        if y == 1:
            title("Glucids - Quiz", "")
            write("Put a ", "", "", False, False, True)
            write("name", "bright cyan", "", True, False, True)
            write(" to the given ", "", "", False, False, True)
            write("structure", "bright purple", "", True, False, True)
            write(".", "", "", False, True, True)
            spc()
            list = [] # preparing q/a
            if theme in [1, 3]: list += aldoses
            if theme in [2, 3]: list += cetoses
            random.shuffle(list)
            mistakes = 0
            for i in list:
                write(f"{i["structure"]}\n>> ", "", "", False, False, False)
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
                        if u_answer.lower() == i["name"].lower():
                            c = "green"
                        else:
                            c = "red"
                            mistakes += 1
                        for j in range(3): # flickering
                                write(f"\033[{len(u_answer) + 3}D{">> " + i["name"] if c == "green" else ">> " + u_answer}", "black", "", True, False, False)
                                time.sleep(0.15)
                                write(f"\033[{len(u_answer) + 3}D{">> " + i["name"] if c == "green" else ">> " + u_answer}", c, "", True, False, False)
                                time.sleep(0.15)
                        spc()
                        break
            spc()
            comment = "Did you even try ??!"
            if mistakes == 0: comment = "Perfect score !!"
            elif mistakes <= 1: comment = "Well done !"
            elif mistakes <= 3: comment = "Good."
            elif mistakes <= 6: comment = "Meh."
            write(f"{comment} You did {mistakes} mistake." if mistakes == 1 else f"{comment} You did {mistakes} mistakes.", "", "", False, True, True)
            spc()
            quiz_biology(2) if choice(["Again", "Back"], "", []) == 1 else quiz_biology(0)
        elif y == 2: quiz_biology(0)
    elif x == 3: quiz(0)

def calculator(x):
    if x == 0:
        title("Calculator", "")
        calculator(choice(["Calculate M", "Back"], "", []))
    if x == 1: m_calc(0)
    if x == 2: main_menu(0)
def m_calc(x):
    if x == 0:
        title("calculate M", "")
        write("Please enter the components in format Xa Yb etc...\n\n>> ", "", "", False, False, True)
        search = ""
        while True:
            key = keyboard.read_key()
            if ((key.isalpha() and len(key) == 1) or key.isdecimal() or key == "space") and keyboard.is_pressed(key): # writing comp
                if keyboard.is_pressed("shift") or keyboard.is_pressed("maj"):
                    key = key.upper()
                search += key if key != "space" else " "
                write(f"{key}" if key != "space" else " ", "black","", True, False, False)
            elif key == "backspace" and keyboard.is_pressed(key) and len(search) > 0: # deleting char
                search = search[:-1]
                write("\033[1D \033[1D", "black", "", True, False, False)
            elif key == "enter" and keyboard.is_pressed(key): # calculating
                components = search.split()
                result = 0
                detail = []
                for i in components:
                    if len(i) > 1 and i[-2].isalpha(): # if element has 2 letters
                        atom = i[-2:]
                        n = i[:-2]
                    else:
                        atom = i[-1]
                        n = i[:-1]
                    for j in p_table:
                        if j["atom"] == atom:
                            result += j["mass"] * (int(n) if n != "" and n.isdecimal() else 1)
                            detail.append(f"{n if n != '' else '1'} x {j['mass']}")
                            break
                write(f"\n\nM = {' + '.join(detail)}", "", "", False, True, True)
                write(f"  = {result} g/mol", "", "", False, True, True)
                spc()
                y = choice(["Again", "Back"], "", [])
                if y == 1: m_calc(0)
                elif y == 2 : calculator(0)
# ====== START ===========================================================================================================================================================

cursor.hide()
main_menu(0)