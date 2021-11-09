import dataCrawler as dc
import SearchInterface
import func_Lib as fl
import sqlite3
from dataDefine import *


if __name__ == '__main__':
    # app = Application()
    # app.master.title('hello world')
    #
    # app.mainloop()
    data = fl.data_get()
    Foods = fl.data_deal(data)
    # SearchInterface.M(Foods)
    fl.menu(Foods)



