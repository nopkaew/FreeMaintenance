from tkinter import *
from tkinter import messagebox
from tkinter import ttk
#from songline import Sendline
import csv
from datetime import datetime
from db_maintenance import *

GUI = Tk()
GUI.title('โปแกรมซ่อมบำรุง โดย Nop')
GUI.geometry('1000x450+300+300')  #ขนาด 500 x 500 ตำแหน่งแสดงผล 300,300

###Font###
FONT1 = ('Tahoma',20)
FONT2 = ('Tahoma',15)
##########

###Tab###
Tab = ttk.Notebook(GUI)
T1 = Frame(Tab)
T2 = Frame(Tab)
Tab.add(T1,text='ใบแจ้งซ่อม')
Tab.add(T2,text='ดูใบแจ้งซ่อม')
Tab.pack(fill=BOTH,expand=1)

#token = 'C9AgUJb18pFtxKrDrnSYY1PBJ1522V0aNivWajqN9iw'
#messenger = Sendline(token)

#############Tab1##########################
L = Label(T1,text='โปรแกรมซ่อมบำรุง',font=FONT1)
L.pack()

L = Label(T1,text='ชื่อผู้แจ้ง',font=FONT2)
L.place(x=20,y=50) #ตำแหน่ง
v_name = StringVar()
E1 = Entry(T1,textvariable=v_name,font=FONT2)
E1.place(x=150,y=50)

L = Label(T1,text='แผนก',font=FONT2)
L.place(x=20,y=100) #ตำแหน่ง
v_department = StringVar()
E1 = Entry(T1,textvariable=v_department,font=FONT2)
E1.place(x=150,y=100)

L = Label(T1,text='อุปกรณ์/เครื่อง',font=FONT2)
L.place(x=20,y=150) #ตำแหน่ง
v_machine= StringVar()
E1 = Entry(T1,textvariable=v_machine,font=FONT2)
E1.place(x=150,y=150)

L = Label(T1,text='อาการเสีย',font=FONT2)
L.place(x=20,y=200) #ตำแหน่ง
v_problem = StringVar()
E1 = Entry(T1,textvariable=v_problem,font=FONT2)
E1.place(x=150,y=200)

L = Label(T1,text='หมายเลข',font=FONT2)
L.place(x=20,y=250) #ตำแหน่ง
v_no = StringVar()
E1 = Entry(T1,textvariable= v_no,font=FONT2)
E1.place(x=150,y=250)

L = Label(T1,text='เบอร์โทร',font=FONT2)
L.place(x=20,y=300) #ตำแหน่ง
v_tel = StringVar()
E1 = Entry(T1,textvariable=v_tel,font=FONT2)
E1.place(x=150,y=300)

def writecsv(record_list):    
    with open('data.csv','a',newline='',encoding='utf-8') as file:
        fw = csv.writer(file)
        fw.writerow(record_list)

def save():
    name = v_name.get()
    department = v_department.get()
    machine = v_machine.get()
    problem = v_problem.get()
    number = v_no.get()
    tel = v_tel.get()
    text = 'ชื่อผู้แจ้ง: ' + name +'\r\n'
    text = text + 'แผนก: ' + department + '\r\n'
    text = text + 'อุปกรณ์/เครื่อง: ' + machine + '\r\n'
    text = text + 'อาการเสีย: ' + problem + '\r\n'
    text = text + 'หมายเลข: ' + number + '\r\n'
    text = text + 'โทร: ' + tel + '\r\n'
    dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    tsid = str(int(datetime.now().strftime('%y%m%d%H%M%S')) + 114152147165)
    insert_mtworkorder(tsid,name,department,machine,problem,number,tel)
    datalist = [dt,name,department,machine,problem,number,tel]
    writecsv(datalist)
  #  messagebox.showinfo('กำลังบันทึกข้อมูล....',text)
    v_name.set('')
    v_department.set('')
    v_machine.set('')
    v_problem.set('')
    v_no.set('')
    v_tel.set('')
    update_table()
   # messenger.sendtext(text)

B = Button(T1,text='บันทึกการแจ้งซ่อม',font=FONT2,command=save)
B.place(x=150,y=350)   

#############Tab2##########################
header = ['TSID','ชื่อ','แผนก','อุปกรณ์','อาการเสีย','หมายเลข','เบอร์โทรผู้แจ้ง']
headerw = [50,100,100,150,300,100,100]

mtworkorderlist = ttk.Treeview(T2,columns=header,show='headings',height=10)
mtworkorderlist.pack()
for h,w in zip(header,headerw):
    mtworkorderlist.heading(h,text=h)
    mtworkorderlist.column(h,width=w)

mtworkorderlist.column('TSID', anchor='e')

#mtworkorderlist.insert('','end',values=['A','B','C','D','E','F','G'])

def update_table():
    datatuple= view_mtworkorder()  #ผลลัพธ์เป็น tuple ไม่ใช่ list
    mtworkorderlist.delete(*mtworkorderlist.get_children())
    for d in datatuple:
        d = list(d)  # แปลง tuple ให้เป็น list
        del d[0]     # ลบ id จาก database ออก
        mtworkorderlist.insert('','end',values=d)

########### Start Up #############
update_table()

GUI.mainloop()