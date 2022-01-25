import tkinter as tk
from tkinter import Entry, ttk
from tkinter import filedialog

import matplotlib.pyplot as plt


class CodeSmoker(object):
    # Konvertiert manipulierten String zu matplotlib-Tabelle
    def output_tracetable(self):
        # # Daten in Tabelle verfrachten
        # plt.show()
        pass

    # Manipulation von py_file
    def create_execString(self):
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        pass


    # String aus import_python_file()-Funktion return-value manipulieren,
    # um Variablen zu tracen.
    def parse_code(self, userinput):
        # Zu tracende Variablen aus Userinput
        trace_vars = userinput.get().split(" ")
        # Liste für gefunde Variablen in importiertem Pythoncode
        found_variables = []
        found_whileloops = []
        found_indentations = []

        # Jede Variable aus UserInput wird lokalisiert
        for var in trace_vars:
            found_variables.append(var) # Am Anfang der "Vorkommen" in Liste steht der Variablenbezeichner
            # Da für jeden Buchstaben Iteriert wird, muss abgeglichen werden,
            # ob man nicht schon wieder den selben Variablenbezeichner gefunden hat.
            recent_val = None
            for i in range(0, len(py_file), 1):
                letter = py_file.find(var, i)

                if (var in py_file) and self.no_duplicates_and_0(letter, recent_val):
                    pos = [letter, letter + len(var)]
                    found_variables.append(pos)
                
                    recent_val = letter
        
        # Alle while-Loops werden lokalisiert
        recent_val = None
        for i in range(0, len(py_file), 1):
            loops = py_file.find("while", i)

            if ("while" in py_file) and self.no_duplicates_and_0(loops, recent_val):
                pos = [loops, loops + len("while")]
                found_whileloops.append(pos)
                
                recent_val = loops
        
        # Alle Einrückungen werden lokalisiert
        for i in range(0, len(py_file), 1):
            indent = "    "
            indents = py_file.find(indent, i)

            if (indent in py_file) and indents >=0:
                pos = [indents, indents + len(indent)]
                found_indentations.append(pos)

        # # Test
        # print(found_variables)
        # print(found_whileloops)
        # print(found_indentations)

    def no_duplicates_and_0(self, variable, recent_val):
        return (variable != recent_val) and (variable >= 0)

class Engine(object):
    def __init__(self):
        get_trace_vars = None

    # Import von Python-Dateien und speichern in String
    def import_python_file(self):
        try:
            # Datei wird als String in CigarTracer importiert
            global py_file; py_file = filedialog.askopenfile(parent=root, title="Pythondatei für den Trace auswählen...").read()
        except:
            self.error_handler()

    def start_smoking(self):
        code_smoker = CodeSmoker()

        # try:
        code_smoker.parse_code(self.get_trace_vars)
        code_smoker.create_execString()
        code_smoker.output_tracetable()
        # except:
        #     self.error_handler()

    # Sendet Fehlermeldungen (müssen in Funktion geschlossen werden!)
    def error_handler(self):
        error_handler = tk.Tk()

        error_handler.title("ERROR")
        error_handler.iconbitmap('MonteCristo_Cigar.ico')

        skipped_filedialog = tk.Message(error_handler, text="Es ist ein Fehler aufgetreten!", fg= "red")
        skipped_filedialog.pack()
        
        confirm_message = ttk.Button(error_handler, text="Ok", command=root.quit)
        confirm_message.pack()

    # tkinter Fenster dient als Backbone
    def gui(self):
        global root; root = tk.Tk()
        
        # Titel und Icon oben links
        root.title("CigarTracer")
        root.iconbitmap('MonteCristo_Cigar.ico')

        # Dimensionen des Fensters, sowie Verhinderung dessen Manipulation
        root.geometry("600x200")
        root.minsize(width=600, height=200)
        root.maxsize(width=600, height=200)

        # UI-Elemente BEGINN
        welcome_txt = tk.Label(root, text="Willkommen beim CigarTracer", )
        welcome_txt.pack()

        by_ms = tk.Label(root, text="by Mark Steffes")
        by_ms.pack()

        # Filedialog
        choose_file_to_trace = ttk.Button(root, text="Pythondatei für Trace auswählen...", padding=10, command=self.import_python_file)
        choose_file_to_trace.pack()

        # Zu tracende Variablen übergeben
        get_trace_vars_label = ttk.Label(root, text="Variablenbezeichner durch LEERZEICHEN getrennt auflisten: \"variable1 variable2 variable3 [...]\".")
        get_trace_vars_label.pack()
        self.get_trace_vars =  Entry(root)
        self.get_trace_vars.pack()

        trace_button = ttk.Button(root, text="Trace the code motherfucker!", command=self.start_smoking)
        trace_button.pack()

        exit_button = ttk.Button(root, text="Verlassen", command=root.quit)
        exit_button.pack()
        # UI-Elemente ENDE

        root.mainloop()


engine = Engine()
engine.gui()