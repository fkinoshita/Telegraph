## Update pot files from source files:

```bash
cd po  
intltool-update --maintain  
cd ..  
find telegraph -iname "*.py" | xargs xgettext --from-code=UTF-8 --output=po/telegraph-python.pot  
find data -iname "*.ui" | xargs xgettext --from-code=UTF-8 --output=po/telegraph-glade.pot -L Glade  
msgcat --use-first po/telegraph-glade.pot po/telegraph-python.pot > po/telegraph.pot  
rm po/telegraph-glade.pot po/telegraph-python.pot  
```

## Generate po file for language

```bash
cd po  
msginit --locale=xx --input=telegraph.pot
```

