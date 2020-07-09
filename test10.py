import sqlite3
c=sqlite3.connect("base0.db")
show=c.execute('select * from base7')
for i in show:
    print(i)
    
