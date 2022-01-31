# Tkinter für GUI
import tkinter as tk
from tkinter import Entry, ttk
from tkinter import filedialog

# Matplotlib für Datenausgabe als Tabelle
import matplotlib.pyplot as plt


# Beinhaltet Algorithmus zur Ausgabe einer Tracetabelle
class CodeSmoker(object):
    def __init__(self):
        self.found_variables = []
        self.found_whileloops = []
        self.found_forloops = []
        self.found_indentations = []

    # Erhält als Parameter Liste mit allen Variablenwerten 
    # und entsprechendem SD und erstellt daraus eine matplotlib-Tabelle.
    def create_tracetable(self, varlist):
        # Diesen Teil schreibe ich erst, wenn ich:
        #   a) weiß in welcher Form ich die Variablenwerte aus
        #      smoke_code erhalte
        #   b) den Algorithmus für smoke_code fertiggestellt habe.
        #
        # Als Inspiration dient mir dabei: https://statologie.de/tabelle-matplotlib/
        
        # plt.show()
        pass

    # Manipulation von py_file und anschließende Ausführung
    # mittels der exec(String)-Funktion.
    def smoke_code(self):
        exec_output = []

        # Aktuelle Baustelle, ich bin gerade noch in der Konzeption
        # des passenden Algorithmus. 
        # 
        # Also hier gerne Vorschläge her,
        # ich schaue mir alle pull-requests an!

        return exec_output

    # String aus import_python_file()-Funktion return-value manipulieren,
    # um Variablen zu tracen.
    def parse_code(self, userinput):
        # Zu tracende Variablen aus Userinput
        trace_vars = userinput.get().split(" ")

        # Lokalisieren aller Variablen
        for var in trace_vars:
             # Alle Variablen werden in die selbe Liste gespeichert, daher
             # Trennung der Einträge durch die Variable selbst zu Beginn
            self.found_variables.append(var)
            self.strings_finder(var, "found_variables") # Variablen
        
        # Lokalisieren von Schleifenkeywords, etc.
        self.strings_finder("while", "found_whileloops") # while
        self.strings_finder("for", "found_forloops") # for
        self.strings_finder("    ", "found_indentations") # "Einrückungen"

        # # Testing
        # print(self.found_variables)
        # print(self.found_whileloops)
        # print(self.found_forloops)
        # print(self.found_indentations)

    def strings_finder(self, searched_string, listname):
        # Damit man auf die Listen, die in der __init__()-Funktion
        # initialisiert werden zugreifen kann.
        found_list_names = {
            "found_variables": self.found_variables,
            "found_whileloops": self.found_whileloops,
            "found_forloops": self.found_forloops,
            "found_indentations": self.found_indentations
        }

        # Es wird über Objekte aus Liste von Zeilen
        line_number = 1 # Für Zeilen angabe in found_listen
        for line in engine.py_file:
            searched_strings = line.find(searched_string)

            # Zeilennummer und Position (Tail, Head) wird in die entsprechende
            # Liste ("siehe listname Param + dictionary") geschrieben
            if (searched_string in line) and (searched_strings >= 0):
                pos = [line_number, searched_strings, searched_strings + len(searched_string)]
                found_list_names[listname].append(pos)
                
            line_number += 1

class Engine(object):
    def __init__(self):
        self.py_file = None
        self.window = None
        self.get_trace_vars = None

    # Import von Python-Dateien und speichern in String
    def import_python_file(self):
        try:
            # Datei wird als String in CigarTracer importiert
            self.py_file = filedialog.askopenfile(parent=self.window, title="Pythondatei für den Trace auswählen...").readlines()
        except:
            self.error_handler()

    def start_smoking(self):
        code_smoker = CodeSmoker()

        # # Errormanegmentsystem (während Debugging AUSKOMMENTIEREN, sonst Syntaxfehler nicht klar!)
        # try:
        code_smoker.parse_code(self.get_trace_vars)
        code_smoker.create_tracetable(code_smoker.smoke_code())
        # except:
        #     self.error_handler()

    # Sendet Fehlermeldungen (müssen in Funktion geschlossen werden!)
    def error_handler(self):
        error_handler = tk.Tk()

        error_handler.title("ERROR")

        skipped_filedialog = tk.Message(error_handler, text="Es ist ein Fehler aufgetreten!", fg= "red")
        skipped_filedialog.pack()
        
        confirm_message = ttk.Button(error_handler, text="Ok", command=self.window.quit)
        confirm_message.pack()

    # tkinter Fenster dient als Backbone
    #
    # An dieser Stelle die herzliche Einladung an alle, die mehr Erfahrung mit GUIs haben,
    # das hier ist, wie man wahrscheinlich unschwer erkennen kann meine 
    # Erste... :-)
    def gui(self):
        self.window = tk.Tk()
        
        # Titel und Icon oben links
        self.window.title("CigarTracer")

        # Dimensionen des Fensters
        self.window.geometry("600x200")
        # Verhindern von windowresizing durch Nutzer
        self.window.minsize(width=600, height=200)
        self.window.maxsize(width=600, height=200)

        # ----------------------------------------------------------------------------------
        # UI-Elemente BEGINN 
        # ----------------------------------------------------------------------------------

        welcome_txt = tk.Label(self.window, text="Willkommen beim CigarTracer", )
        welcome_txt.pack()

        by_ms = tk.Label(self.window, text="by Mark Steffes")
        by_ms.pack()

        # Filedialog
        choose_file_to_trace = ttk.Button(self.window, text="Pythondatei für Trace auswählen...", padding=10, command=self.import_python_file)
        choose_file_to_trace.pack()

        # Zu tracende Variablen übergeben
        get_trace_vars_label = ttk.Label(self.window, text="Variablenbezeichner durch LEERZEICHEN getrennt auflisten: \"variable1 variable2 variable3 [...]\".")
        get_trace_vars_label.pack()
        self.get_trace_vars =  Entry(self.window)
        self.get_trace_vars.pack()

        trace_button = ttk.Button(self.window, text="Trace the code motherfucker!", command=self.start_smoking)
        trace_button.pack()

        exit_button = ttk.Button(self.window, text="Verlassen", command=self.window.quit)
        exit_button.pack()

        # ----------------------------------------------------------------------------------
        # UI-Elemente ENDE 
        # ----------------------------------------------------------------------------------

        self.window.mainloop()


engine = Engine()
engine.gui()
