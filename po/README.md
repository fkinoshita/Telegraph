## Update pot files from source files:

```bash
cd po  
intltool-update --maintain  
cd ..  
find src -iname "*.py" | xargs xgettext --from-code=UTF-8 --output=po/telegraph-python.pot
find data -iname "*.ui" | xargs xgettext --from-code=UTF-8 --output=po/telegraph-glade.pot -L Glade
find data -iname "*about*" | xargs xgettext --from-code=UTF-8 --output=po/telegraph-about.pot
find data -iname "*desktop*" | xargs xgettext --from-code=UTF-8 --output=po/telegraph-desktop.pot
msgcat --use-first po/telegraph-glade.pot po/telegraph-python.pot po/telegraph-about.pot po/telegraph-desktop.pot > po/telegraph.pot
rm po/telegraph-glade.pot po/telegraph-python.pot po/telegraph-about.pot po/telegraph-desktop.pot
```

## Generate po file for language

```bash
cd po  
msginit --locale=xx --input=telegraph.pot
```

