from tkinter import *
import tkinter.messagebox as messagebox

#
# class Application(Frame):
#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         self.pack()
#         self.createWidgets()
#
#     def createWidgets(self):
#         self.nameInput = Entry(self)
#         self.nameInput.pack()
#         self.alertButton = Button(self, text='Hello', command=self.hello)
#         self.alertButton.pack()
#
#     def hello(self):
#         name = self.nameInput.get() or 'world'
#         messagebox.showinfo('Message', 'Hello, %s' % name)
#


class DData(object):

    def __init__(self):
        self.name = None
        self.steps = []
        self.rMaterial = {}
        self.web = str


class Food():
    name, material, steps, web = None, None, None, None

    def __init__(self, n=None, m=None, s=None, w=None):
        self.name = n
        self.material = m
        self.steps = s
        self.web = w
