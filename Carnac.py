#!/usr/bin/env python2.7.5
#Carnac 1.3 Gui test this is with the headfirst guide

#Call Tkinter
from Tkinter import *
import tkFileDialog
import csv


#-------------------
#Application Window
#-------------------
#make app window
app = Tk()
app.title("Test GUI for Carnac")
app.geometry("400x400")

#------------------------
#Defs and Button functions
#------------------------
#define some commands
#import button, gets and reads in file, defines list
def import_csv():
    print "Importing..."
    filename = tkFileDialog.askopenfilename(filetypes=[('CSV (Comma Deliminated)', '.csv')], parent=app, title="import")
    print filename
#write in the CSV
    
    with open(filename, 'r') as csvfile: 
        imported_file = csv.reader(csvfile, delimiter=' ', quotechar='|')
        working_file = []
        for row in imported_file:
                    print ', '.join(row)
                    working_file.append(row)                 
        print working_file
        global working_file
#copy over the list, so the original is preserved
    
    
def alright():
    print "Alright, test that string"
    print working_file
#save button, takes working file turns into output file, 
def save_csv():
    print "Saving..."
    print working_file
    exportname = tkFileDialog.asksaveasfilename(filetypes=[('CSV (Comma Deliminated)', '.csv')], defaultextension=".csv", parent=app, title="Save As")
    print exportname
# write contents of list into .csv 
  
    with open(exportname, 'wb') as csvfile:
        output_file = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        #output_file.writerow(['please', 'work', 'damnit'])
        output_file.writerows(working_file)

#-----------------
#Menu
#-----------------
#creates menu
menu_bar = Menu(app)

#creates sub menu
file_sub_menu = Menu(menu_bar, tearoff=0)
file_sub_menu.add_command(label="Import File", command=import_csv)
file_sub_menu.add_command(label="Save As", command=save_csv)
file_sub_menu.add_separator()
file_sub_menu.add_command(label="Close", command=app.quit)

menu_bar.add_cascade(label="File", menu=file_sub_menu)
#makes menu_bar App's menu
app.config(menu=menu_bar)

#-----------------
#Display
#-----------------
#-----------------
#Button Bar
#-----------------
#button_bar = Frame()
#Label(button_bar, text="").pack(side = "bottom")
close_button = Button(app, text = "Close", command=app.quit)
close_button.pack(side = "right")

alright_button = Button(app, text = "Alright", command=alright)
alright_button.pack(side = "left")
'''
import_button = Button(app, text = "Import", command=import_csv)
import_button.pack(side = "left")

#import_button = Button(app, text = "Manage Rules", command=save_csv)
#import_button.pack(side = "left")

import_button = Button(app, text = "Save", command=save_csv)
import_button.pack(side = "left")

'''


app.mainloop()
app.destroy()


