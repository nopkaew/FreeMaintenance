import sqlite3

#สร้าง connection ต่อฐานข้อมูล
conn = sqlite3.connect('maintenance.sqlite3')
#สร้าง cursor ตัวที่เอาไว้สร้างคำสั่ง sql
c = conn.cursor()

c.execute(""" CREATE TABLE IF NOT EXISTS mt_workorder (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                tsid TEXT,
                name TEXT,
                department TEXT,
                machine TEXT,
                problem TEXT,
                number TEXT,
                tel TEXT)""")

def insert_mtworkorder(tsid,name,department,machine,problem,number,tel):
    #creare
    with conn:
        command = 'INSERT INTO mt_workorder VALUES(?,?,?,?,?,?,?,?)'
        c.execute(command,(None,tsid,name,department,machine,problem,number,tel))
    conn.commit()
    #print('Data was save')

def view_mtworkorder():
    with conn:
        command = "SELECT * FROM mt_workorder"
        c.execute(command)
        result = c.fetchall()
    #print(result)
    return result

def update_mtworkorder(tsid,field,newvalus):
    with conn:
        command = 'UPDATE mt_workorder SET {} = (?) WHERE tsid =(?)' .format(field)  # {} คือจุดที่จะถูกแทนที่ด้วย .format(field)
        c.execute(command,(newvalus,tsid))
    conn.commit()
    #print('Data was save')

def delete_mtworkorder(tsid):
    with conn:
        command = 'DELETE FROM mt_workorder WHERE tsid =(?)'
        c.execute(command,([tsid]))    #ใส [] เนื่องจากต้องการตัวแปรประเภท list หากมีหลาย ตัวแปร ไม่จำเป็นต้องใส หากมีแค่ 1 ตัวแปรจำเป็นต้องใส่ให้ python รับรู้ว่าเป็น list