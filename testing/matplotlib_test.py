import matplotlib.pyplot as plt 

# Diagramm und Achsen definieren
fig, ax = plt.subplots()

# Werte für Tabelle erstellen
table_data=[
    ["1", 30, 34],
    ["2", 20, 223],
    ["3", 33, 2354],
    ["4", 25, 234],
    ["5", 12, 929]
]

#Tabelle erstellen
table = ax.table(cellText=table_data, loc='center', colLabels=['SD', 'ID', 'Score'])

# Tabelle ändern
table.set_fontsize(14)
table.scale(1,4)
ax.axis('off')

#Tabelle anzeigen
plt.show()
