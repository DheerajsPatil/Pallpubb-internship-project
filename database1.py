import sqlite3
def create_db():
    con=sqlite3.connect(database=r'pallpubb.db')
    cur=con.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS data(name TEXT, age INT, contact INT, address TEXT, occupation TEXT, insta TEXT, facebook TEXT, other TEXT)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS clients(cid INT, name TEXT, contact INT, email TEXT, address TEXT, language TEXT)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS issue(cid INT, month TEXT, year INT)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS pkgclient(cid INT, name TEXT, contact INT, email TEXT, address TEXT, insta TEXT, facebook TEXT)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS books(cname TEXT, bname TEXT, language TEXT, online TEXT, paperback TEXT, ppress TEXT, quantity INT, packages TEXT)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS students(stuname TEXT, schname TEXT, contact INT, address TEXT)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS schools(sname TEXT, pname TEXT, address TEXT, doj TEXT, seid TEXT, cpid TEXT, cpname TEXT, instaid TEXT, facebookid TEXT)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS student(stuname TEXT, schname TEXT, contact INT, address TEXT)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS school(sname TEXT, pname TEXT, address TEXT, doj TEXT, seid TEXT, cpid TEXT, cpname TEXT, instaid TEXT, facebookid TEXT)")
    con.commit()

    


create_db()