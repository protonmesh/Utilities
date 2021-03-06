# URLsToShortcuts
# Conceived for batch subscribing to iTunes Podcasts (if multiple links are dragged into iTunes, it subscribes to them all)
# Input: filename - name of text file containing URLs (one per line)
# Output: for nth URL, the n.url Internet Shortcut file is added to the current working directory
#
# Usage: python URLsToShortcuts.py <filename>
# Ex: python URLsToShortcuts.py urls.txt

import sys

fin = open(sys.argv[1])
i = 1
for feedurl in fin:
    if feedurl.strip() != "":
        with open(str(i) + ".url", 'w') as shortcut:
            print("[InternetShortcut]", file=shortcut)
            print("URL=", feedurl.strip(), sep='', file=shortcut)
        i += 1
