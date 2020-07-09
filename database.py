def regdat(fn,ln,un,mob,pwd):
    import sqlite3
    c=sqlite3.connect("pizza.db")
    print('created')
##c.execute('''create table signup
##          (firstname text,
##          lastname text,
##          username text,
##          mobileno int,
##          password varchar );''')


    c.execute("insert into signup values(?,?,?,?,?)",(fn,ln,un,mob,pwd))
    c.commit()

    sel = c.execute("select * from signup;")

    for i in sel:
        print(i)
        
    c.close()

import sqlite3
c=sqlite3.connect("pizza.db")
c.execute("delete from signup where firstname = '';")
c.commit()

sel = c.execute("select * from signup;")

for i in sel:
    print(i)

c.close()


##for r in sel:
##    print(r[0])
##    print(r[1])
##    print(r[2])
##    print(r[3])
##    print(r[4])
##    print(r[5])
##c.execute('''drop table signup;''')



