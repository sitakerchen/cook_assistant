import sqlite3
import dataDefine
from tkinter import *


def data_get():


    conn = sqlite3.connect('menuData.db')
    cursor = conn.execute('select ID, NAME, MATERIALS, STEPS,  WEB from menuData')
    data = cursor.fetchall()
    conn.commit()
    conn.close()
    return data


def data_deal(data):
    foods = []
    for a, b, c, d, e in data:
        foods.append(dataDefine.Food(b, c, d, e))
    return foods

# name, material, steps, web
def menu(Foods):
    def show_all():
        text = Text(root)
        text.tag_config('tag_1', backgroun='yellow', foreground='red')
        text.tag_config('tag_2', backgroun='blue', foreground='red')
        for item in Foods[0:20]:
            text.insert('insert', '菜名:', 'tag_1')
            text.insert('insert', item.name+str('\n'), 'tag_1')
            text.insert('insert', '材料准备:\n', 'tag_2')
            text.insert('insert', item.material+str('\n'))
            text.insert('insert', '步骤:\n', 'tag_2')
            text.insert('insert', item.steps+str('\n'))
            text.insert('insert', '来源网址:\n', 'tag_2')
            text.insert('insert', item.web+str('\n\n'))
        text.pack()


    def search_by_name():
        print('hello')


    root = Tk()
    root.geometry('1000x800')
    menubar = Menu(root)
    func_dict = {'01': show_all, '11': search_by_name}

    content = [['show all'], ['search by name']]
    main = ['Show', 'Search']
    for i in range(len(main)):
        filemenu = Menu(menubar, tearoff=0)
        for k in content[i]:
            filemenu.add_command(label=k, command=func_dict[str(i)+'1'])
        menubar.add_cascade(label=main[i], menu=filemenu)

    root['menu'] = menubar
    root.mainloop()














# def _backup():
#
#     # dic = dc.updateMenu()
#     # conn = sqlite3.connect('menuData.db')
#     # cursor = conn.execute('select ID, NAME, WEB from menuData')
#     # file = cursor.fetchall()
#     conn = sqlite3.connect('menuData.db')
#     cursor = conn.execute('select ID, WEB from menuData')
#     data = cursor.fetchall()
#     # print(data_s,'steps:'+str(n))
#     begin = 800
#     end = 1000
#     for id, web in data:
#         if id >= begin and id < end:
#         # cnt += 1
#             data_s, n = dc.updateSteps(web)
#             sql = 'update menuData set STEPS = "%s" where ID = %d' % (str(n)+'steps:'+str(data_s),id)
#             # print(sql)
#             conn.execute(sql)
#             print('successful update %d record' % (id))
#             # print(n)
#             # print(data_s)
#             # print('='*20)
#
#     dlist = []
#     dlist.append(DData())#头节点，设为空
#     begin = 801
#     cnt = 1
#     for id, name, web in file:
#         if id >= begin and id <= begin+200:
#             print(id,name,web)
#             dlist.append(DData())
#             dlist[cnt].name,dlist[cnt].web = name, web
#             dlist[cnt].rMaterial.update(dc.updateDetail(dlist[cnt].web))
#             cnt += 1
#             print('successful added'+str(id)+'pieces')
#         else:
#             pass
#     # for i in dlist:
#     #     print(i.name,str(i.rMaterial))
#     cnt = 1
#     for item in dlist[1:]:
#
#         sql = 'update menuData set MATERIALS = "%s" where ID = %d' % (str(item.rMaterial), begin+cnt-1)
#         cnt += 1
#         conn.execute(sql)
#         print('update successfully')
#     cnt = 1
#     for key,value in dic.items():
#         sql = 'insert into menuData (ID,NAME,WEB) values (%d, "%s", "%s")' % (cnt, key, value)
#         conn.execute(sql)
#         cnt += 1
#         print("insert successful!")
#
#     conn.commit()
#     conn.close()


