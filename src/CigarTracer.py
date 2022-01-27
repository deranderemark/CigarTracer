# Tkinter für GUI
import tkinter as tk
from tkinter import Entry, ttk
from tkinter import filedialog

# Matplotlib für Datenausgabe als Tabelle
import matplotlib.pyplot as plt


# Beinhaltet Algorithmus zur Ausgabe einer Tracetabelle
class CodeSmoker(object):
    # Erhält als Parameter Liste mit allen Variablenwerten 
    # und entsprechendem SD und erstellt daraus eine matplotlib-Tabelle.
    def create_tracetable(self, varlist):
        # plt.show()
        pass

    # Manipulation von py_file und anschließende Ausführung
    # mittels der exec(String)-Funktion.
    def smoke_code(self):
        exec_output = []

        # [...]

        return exec_output

    # Liste für gefunde Variablen in importiertem Pythoncode
    # War ursprünglich innerhalb von parse_code()-Funktion, 
    # jedoch Änderung wegen Implementierung von 
    # string_finder()-Funktion.
    found_variables = []
    found_whileloops = []
    found_forloops = []
    found_indentations = []

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

        # Testing
        print(self.found_variables)
        print(self.found_whileloops)
        print(self.found_forloops)
        print(self.found_indentations)

    def strings_finder(self, string_to_search, listname):
        found_list_names = {
            "found_variables": self.found_variables,
            "found_whileloops": self.found_whileloops,
            "found_forloops": self.found_forloops,
            "found_indentations": self.found_indentations
        }

        recent_val = None # Dient nur der Initialisierung

        # Es wird über alle char in py_file iteriert, sonst
        # wird 2. vorkommen von .find()-Funktion ignoriert/nicht gefunden.
        for i in range(0, len(py_file), 1):
            # Suchen eins Strings in py_file; i ist tail-pos
            strings_to_search = py_file.find(string_to_search, i)

            # Falls gewünscht wird die gefundene Position in die entsprechende
            # Liste ("siehe listname Param + dictionary") geschrieben
            no_dublicates_and_0 = (strings_to_search != recent_val) and (strings_to_search >= 0)
            if (string_to_search in py_file) and no_dublicates_and_0:
                pos = [strings_to_search, strings_to_search + len(string_to_search)]
                found_list_names[listname].append(pos)

                # Hilft beim Vermeiden doppelter Einträge von Variablenpositionen,
                # die sonst auftreten, da eben über jeden char als pos für den
                # tail iteriert wird
                recent_val = strings_to_search

# Hält das Programm am Leben
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

        # Dimensionen des Fensters
        root.geometry("600x200")
        # Verhindern von windowresizing durch Nutzer
        root.minsize(width=600, height=200)
        root.maxsize(width=600, height=200)

        # ----------------------------------------------------------------------------------
        # UI-Elemente BEGINN 
        # ----------------------------------------------------------------------------------

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

        # ----------------------------------------------------------------------------------
        # UI-Elemente ENDE 
        # ----------------------------------------------------------------------------------

        root.mainloop()


engine = Engine()
engine.gui()
