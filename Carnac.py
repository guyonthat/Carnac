#!/usr/bin/env python2.7.5
#Carnac Gui using OOP
'''
Intent of program is to:
Pull in a csv
Process the title column
Run rules to modify the column contents based on "roles"
Make the rule able to be changed in app by user
Run rules multiple times
Export to file
'''
#----------
#Import your shit
#----------
from Tkinter import *
from tkMessageBox import*
import tkFileDialog
import csv
#----------
#global Variables, to be modified later
#----------
working_file = []
#----------
#call Make the Gui and buttons
#----------
class MainMenu(Frame): #calls the main window
        def __init__(self, parent=None):
            Frame.__init__(self,parent) #makes main menu top level <--- this is a lie? see @learnwhat
            self.pack(expand=YES, fill=BOTH)
            self.createWidgets()
            self.master.title("Carnac Role Guessing Tool")
            self.master.iconname("Carnac")

        def createWidgets(self): #loads widges into MainMenu
            self.makeMenuBar()
            self.makeButtonBar()
            Side_scroll = Scrollbar(self)
            Print_box = Text(self)
            Side_scroll.config(command=Print_box.yview)
            Side_scroll.pack(side=RIGHT, fill=Y)
            Print_box.config(state=DISABLED, relief=SUNKEN, width=40, height=20, bg='white',yscrollcommand=Side_scroll.set)
            Print_box.pack(side=LEFT, expand=YES, fill=BOTH)
            self.Print_box = Print_box
                        

        def makeButtonBar(self): #aka button bar in the psuedo
            ButtonBar = Frame(self, cursor='hand2', relief=SUNKEN, bd=2)
            ButtonBar.pack(side=BOTTOM, fill=X)
            
            close_button = Button(ButtonBar, text = "Close", command=self.program_quit)
            close_button.pack(side = "right")

            alright_button = Button(ButtonBar, text = "Alright", command=self.alright)
            alright_button.pack(side = "left")
            '''
            import_button = Button(ButtonBar, text = "Import", command=self.import_csv)
            import_button.pack(side = "left")

            #import_button = Button(ButtonBar, text = "Manage Rules", command=self.save_csv)
            #import_button.pack(side = "left")

            import_button = Button(ButtonBar, text = "Save", command=self.save_csv)
            import_button.pack(side = "left")

            '''
        def makeMenuBar(self):
            self.menubar = Menu(self.master)
            self.master.config(menu=self.menubar) #master top level window @leanwhat top level means specifically #THIS IS THE TOPLEVEL WINDOW THAT GETS CLOSED
            self.fileMenu()

        def fileMenu(self):
            pulldown = Menu(self.menubar) # The (self.menubar) sets it in the menubar
            pulldown.add_command(label="Import File", command=self.import_csv)
            pulldown.add_command(label="Save As", command=self.save_csv)
            pulldown.add_separator()
            pulldown.add_command(label="Close", command=self.program_quit)
            self.menubar.add_cascade(label='File', underline=0, menu=pulldown)
        '''
        def askopenfilename(self):
            filename = tkFileDialog.askopenfilename(filetypes=[('CSV (Comma Deliminated)', '.csv')], parent=MainMenu, title="import")

            return filename
        '''            
#-------
#define button actions
#-------                      
        def program_quit(self):
            print "Shut it down"
            self.master.destroy()
            '''if askyesno('Verify Quit', 'Are you sure you want to quit?'):
                Frame.quit(self)
                sys.exit()
            '''

        def import_csv(self):
            print "Importing..."
        '''
    filename = MainMenu.askopenfilename
    print filename
#write in the CSV
    
    with open(filename, 'r') as csvfile: 
        global working_file #modifies global
        imported_file = csv.reader(csvfile, delimiter=' ', quotechar='|')
        working_file = []
        for row in imported_file:
                    print ', '.join(row)
                    working_file.append(row)                 
        print working_file
        '''    
#copy over the list, so the original is preserved
        def alright(self):
            self.Print_box.configure(state=NORMAL) #allows additions to text widget
            self.Print_box.insert(END,"Alright, test that string \n") #try printing to text widget
            print "Alright, test that string" #for debugging
            print working_file
            self.Print_box.configure(state=DISABLED) #stops additions to text widget
#save button, takes working file turns into output file, 
        def save_csv(self):
    
            print "Saving..."
        '''
    print working_file
    exportname = tkFileDialog.asksaveasfilename(filetypes=[('CSV (Comma Deliminated)', '.csv')], defaultextension=".csv", parent=window, title="Save As")
    print exportname
# write contents of list into .csv 
    with open(exportname, 'wb') as csvfile:
        output_file = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        #output_file.writerow(['please', 'work', 'damnit'])
        output_file.writerows(working_file)
        '''
if __name__ == '__main__': MainMenu().mainloop() #if I'm run as a script
    
