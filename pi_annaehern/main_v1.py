# Aufgabe
# Die Strukturierte Programmierung eignet sich wunderbar um Probleme der Numerik zu bearbeiten. 
# Dabei gehen viele Algorithmen so vor, dass sie sich einem gewünschten Ergebnis immer weiter annähern. 
# Beendet werden diese Algorithmus sobald sich Zwischenergebnisse nicht mehr stark verändern und angenommen 
# werden kann beim korrekten Ergebnis angekommen zu sein.

# Der Mathematiker Gottfried Wilhelm Leibniz hat im Jahre 1682 eine Näherungsformel für die Kreiszahl PI entwickelt.

# Für Details schauen Sie hier nach: https://de.wikipedia.org/wiki/Leibniz-Reihe

# Schreiben Sie ein Programm zur Bestimmung der Zahl PI.

# Das Programm soll in einer ersten Version zunächst eine feste Zahl von 1000 Iterationen durchlaufen.
# In der zweiten Version soll die Zahl PI auf 6 Stellen hinter dem Komma genau ermittelt werden.
# Das Kriterium dafür ist, das sie die Zahl PI bei 5 Iterationsstufen hintereinander an der 6. Stelle nicht mehr ändern darf.
# Gemäß des Wikipaedia Artikels müsste dies bei ca 500.000 Iterationen der Fall sein.
# Visualisieren Sie den Näherungsalgorithmus auf die von Ihnen gewünschte Weise und geben Sie dies hier ab. Ein Foto ist dabei wie immer ausreichend.


pi = 0
sign = 1
iterations = 1000

for i in range(1, iterations+1):
    pi = pi + sign * 4 / (2 * i - 1)
    sign = -sign
    
print(pi)