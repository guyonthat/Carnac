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
#call Make the Gui and buttons
#----------
class Carnac(Frame): #calls the Carnac Parent Class
    def __init__(self):
        self.Carnac_Gui(Self)
        self.imported_csv = []
        self.working_file = []
        
#if __name__ == '__main__': Carnac().mainloop() #if I'm run as a script

class Carnac_Gui(Carnac):
        def __init__(self):
            Frame.__init__(self) #makes main menu top level <--- this is a lie? see @learnwhat
            self.pack(expand=YES, fill=BOTH)
            self.createWidgets()
            self.master.title("Carnac Role Guessing Tool")
            self.master.iconname("Carnac")

        def createWidgets(self): #loads widges into Carnac
            self.makeMenuBar()
            self.makeButtonBar()
            Side_scroll = Scrollbar(self)
            Bot_scroll = Scrollbar(self)
            Print_box = Text(self)
            Side_scroll.config(command=Print_box.yview)
            Side_scroll.pack(side=RIGHT, fill=Y)
            Bot_scroll.config(command=Print_box.xview, orient=HORIZONTAL)
            Bot_scroll.pack(side=BOTTOM, fill=X)
            Print_box.config(state=DISABLED, relief=SUNKEN, width=80, height=20, bg='white',yscrollcommand=Side_scroll.set, xscrollcommand=Bot_scroll.set)
            Print_box.config(wrap=NONE)
            Print_box.pack(side=LEFT, expand=YES, fill=BOTH)
            self.Print_box = Print_box
            
        def makeButtonBar(self): 
            ButtonBar = Frame(self, cursor='hand2', relief=SUNKEN, bd=2)
            ButtonBar.pack(side=BOTTOM, fill=X)
            
            close_button = Button(ButtonBar, text = "Close", command=self.program_quit)
            close_button.pack(side = "right")
            
            import_button = Button(ButtonBar, text = "Import", command=self.import_csv)
            import_button.pack(side = "left")
            
            output_button = Button(ButtonBar, text = "Output", command=self.output)
            output_button.pack(side = "left")

            import_button = Button(ButtonBar, text = "Run Rules", command=self.run_rules)
            import_button.pack(side = "left")

            import_button = Button(ButtonBar, text = "Save", command=self.save_csv)
            import_button.pack(side = "left")

            
        def makeMenuBar(self):
            self.menubar = Menu(self.master)
            self.master.config(menu=self.menubar) #master top level window @leanwhat top level means specifically #THIS IS THE TOPLEVEL WINDOW THAT GETS CLOSED
            self.fileMenu()

        def fileMenu(self):
            pulldown = Menu(self.menubar) # The (self.menubar) sets it in the menubar
            pulldown.add_command(label="Import File", command=self.import_csv)
            pulldown.add_command(label="Reset", command=self.RESET)
            pulldown.add_command(label="Save As", command=self.save_csv)
            pulldown.add_separator()
            pulldown.add_command(label="Close", command=self.program_quit)
            self.menubar.add_cascade(label='File', underline=0, menu=pulldown)                   
#-------
#Report function
#This function is to save time and code by enveloping the simon says with the text widget, into a print-like line
#'where' is not a string, 'what' and mod are
        def report(self,where,what): #to be used to print to the user and the shell
                    self.Print_box.configure(state=NORMAL) #allows additions to text widget
                    self.Print_box.insert(where,what) #try printing to text widget
                    self.Print_box.insert(END,"\n")
                    print what #for debugging
                    self.Print_box.configure(state=DISABLED) #stops additions to text widget
#------------                         
#-------
#define button actions
#-------                      
        def program_quit(self):
            self.report(END, "Shutting Down")
            if askyesno('Verify Quit', 'Are you sure you want to quit?'):
                self.master.destroy()
            
                
           

        def import_csv(self):
            self.report(END, "Importing...")
        
            filename = tkFileDialog.askopenfilename(filetypes=[('CSV (Comma Deliminated)', '.csv')], defaultextension=".csv", title="Import CSV")
            self.report(END,filename)
                   
            
            with open(filename, 'r') as csvfile: #write in the CSV
                global imported_csv #modifies global
                imported_file = csv.reader(csvfile, delimiter=' ', quotechar='|')
                imported_csv = []
                row_count = -1 #"Take back one kadam to honor the Hebrew God, whose Ark this is"(remove one for the header)
                for row in imported_file:
                            print ', '.join(row)
                            imported_csv.append(row)
                            row_count = row_count + 1
                            #print row_count #for debugging
                print imported_csv
                self.report(END,"Successfully imported %s records" % row_count)
                
        
        def output(self):
            #self.Print_box.configure(state=NORMAL) #allows additions to text widget @removed turned into report function
            #self.Print_box.insert(END,"output, test that string \n") #try printing to text widget
            self.report(END,"You asked for it...")
            #print "Test that string!" #for debugging
            #self.report(END, imported_csv) #dumps contents
            for row in imported_csv: #dumps contents in rows
                        #print row #for debug, called in report function
                        self.report(END,row)
            #self.Print_box.configure(state=DISABLED) #stops additions to text widget

        def run_rules(self):
            self.report(END,"Running the rules!")
            #if transition file has contents then skip getting column
            active_col = 0            
            #get which column will be run
                #pop up window with drop-box populated with the first row of imported_csv, and an accept and run rules button  and cancel button okay returns the active_col number
                #cancel escapes this code
            #read that column into a transition file
            #clean transition file
            #run rules that are rule run yes on transition file
            #return box name and amount if amount greater than 0

        #@todo def modify_rules(self):
            #pop up new gui to have user add mod and del rules
            #has checkbox for rule run yes/no
            
        def RESET(self):
            global working_csv
            if askyesno('Verify Reset', 'Are you sure you want to undo all rule work?'):
                working_csv = []
                
                        

        def save_csv(self): #save button, takes working file turns into output file, 
            #add contents of working_file into imported_csv (probably a function)
            self.report(END, "Saving...")
        
            print imported_csv
            exportname = tkFileDialog.asksaveasfilename(filetypes=[('CSV (Comma Deliminated)', '.csv')], defaultextension=".csv", title="Save As")
            print exportname
         
            with open(exportname, 'wb') as csvfile: # write contents of list into .csv
                output_file = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                #output_file.writerow(['please', 'work', 'damnit'])
                output_file.writerows(imported_csv)
        
if __name__ == '__main__': Carnac_Gui().mainloop() #if I'm run as a script
    
