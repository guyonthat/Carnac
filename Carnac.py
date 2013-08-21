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
from ttk import * #upgrades to ttk to allow dynamic modification of clm_select, some sytax changes in "borderwidth" and "padding" from the old tk
from tkMessageBox import*
import tkFileDialog
import csv


#----------
#call Make the Gui and buttons
#----------
class Carnac(Frame): #calls the main window
        def __init__(self, parent = None):
            Frame.__init__(self,parent) #makes main menu top level <--- this is a lie? see @learnwhat
            self.imported_csv = []
            self.working_file = []
            self.Clm_select_variable = []
            self.Clm_menu_values = []
            self.ColumnSelectDropdown = []
            self.pack(expand=YES, fill=BOTH)
            self.createWidgets()
            self.master.title("Carnac Role Guessing Tool")
            self.master.iconname("Carnac")
            

        def createWidgets(self): #loads widgets into Carnac
            self.makeMenuBar()
            self.makeColumnSelectBar()
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
        def makeMenuBar(self):
            self.menubar = Menu(self.master)
            self.master.config(menu=self.menubar) #master top level window @leanwhat top level means specifically #THIS IS THE TOPLEVEL WINDOW THAT GETS CLOSED
            self.fileMenu()

        def fileMenu(self):
            pulldown = Menu(self.menubar) # The (self.menubar) sets it in the menubar
            pulldown.add_command(label="Import File", command=self.import_csv)
            pulldown.add_command(label="Reset", command=self.RESET)
            pulldown.add_command(label="Edit Rules", command=self.modify_rules)
            pulldown.add_command(label="Save As", command=self.save_csv)
            pulldown.add_separator()
            pulldown.add_command(label="Close", command=self.program_quit)
            self.menubar.add_cascade(label='File', underline=0, menu=pulldown)
        

        def makeButtonBar(self): #aka button bar in the psuedo
            ButtonBar = Frame(self, cursor='hand2', padding="3 0 0 0", relief=SUNKEN, borderwidth=2)
            ButtonBar.pack(side=BOTTOM, fill=X)
            
           
            
            import_button = Button(ButtonBar, text = "Import", command=self.import_csv)
            import_button.pack(side = "left")

           # column_select_button = Button(ButtonBar, text = "Select Column", command=self.column_pop)
            #column_select_button.pack(side = "left")
            
            output_button = Button(ButtonBar, text = "List Contents", command=self.output)
            output_button.pack(side = "left")

            rules_button = Button(ButtonBar, text = "Run Rules", command=self.run_rules)
            rules_button.pack(side = "left")

            import_button = Button(ButtonBar, text = "Save", command=self.save_csv)
            import_button.pack(side = "left")

        def makeColumnSelectBar(self):#runs only if there isn't one already
            ColumnSelectBar = Frame(self, cursor='hand2', relief=SUNKEN, borderwidth=2)
            ColumnSelectBar.pack(side=BOTTOM, fill=X)
            
            #Clm_select_instruction = Label(ColumnSelectBar, text="Please select a column to run rules on:") #not needed now that selectdropdown is better filled
            #Clm_select_instruction.pack(side=LEFT)
            
            self.Clm_select_variable = StringVar(self)
            self.Clm_menu_values = ['File not loaded, please "Import"']
            self.Clm_select_variable.set(self.Clm_menu_values[0]) #default value, needed for the dropdown to work
            
            self.ColumnSelectDropdown = OptionMenu(ColumnSelectBar, self.Clm_select_variable, *self.Clm_menu_values) 
            self.ColumnSelectDropdown.pack(side=LEFT)
            #print ColumnSelectDropdown.get()
            close_button = Button(ColumnSelectBar, text = "Close", command=self.program_quit) #moved to from button bar for better looks
            close_button.pack(side = "right")
                
                    
#-------
#define button actions
#-------                      
        def program_quit(self):
            self.report(END, "Shutting Down")
            if askyesno('Verify Quit', 'Are you sure you want to quit?'):
                self.master.destroy()
            
                
           

        def import_csv(self):
            self.report(END, "Importing...")
            self.working_file = [] #resets the working file on import to allow for re-do in program
        
            filename = tkFileDialog.askopenfilename(filetypes=[('CSV (Comma Deliminated)', '.csv')], defaultextension=".csv", title="Import CSV")
            self.report(END,filename)
                   
        
            with open(filename, 'rb') as csvfile: #write in the CSV
                #global imported_csv #modifies global
                imported_file = csv.reader(csvfile, delimiter=',', quotechar='"')
                self.imported_csv = []
                row_count = -1 #"Take back one kadam to honor the Hebrew God, whose Ark this is"(remove one for the header)
                for row in imported_file:
                            print ', '.join(row)
                            self.imported_csv.append(row)
                            row_count = row_count + 1
                            #print row_count #for debugging
                print self.imported_csv
                self.report(END,"Successfully imported %s records" % row_count)
                
            self.Clm_select_variable.set('FILE IMPORTED') #default value, needed for the dropdown to work
            self.ColumnSelectDropdown.set_menu('Please select which column the rules will be applied to', *self.imported_csv[0]) #gives it information to populate the optionmenu with
            
            
                
#copy over the list, so the original is preserved
        def output(self):
            self.report(END,"You asked for it...")
            #print "Test that string!" #for debugging
            if self.working_file == []: #Show the working file if it has something, otherwise show what was imported
                for row in self.imported_csv: #dumps contents in rows
                        #print row #for debug, called in report function
                        self.report(END,row)
            else:
                for row in self.working_file:
                        self.report(END,row)
            
            #select = self.Clm_select_variable.get()  #must use .get() on variable not menu
            #self.report(END,"The selected Column is: %s" % select)
            
        def run_rules(self):     
            if self.Clm_select_variable.get() == "Please select which column the rules will be applied to": #if they didnt select a column, throw an error
                    showerror("Selection Not Made", "Please select a column to run rules on")#error popup using messagebox
            else:
                self.report(END,"Running the rules!")
            
                if self.working_file == []: #if transition empty, then fill with selected column
                        active_col = 0 #sets variable
                        self.report(END,self.imported_csv[0]) #prints first row for debug
                        active_col = self.imported_csv[0].index(self.Clm_select_variable.get())#gets the column number of the selection
                        self.report(END,active_col) #prints for debugging
                        self.report(END,self.Clm_select_variable.get())#reports the name which will be run
                        for row in self.imported_csv:
                                self.working_file.append(row[active_col])#takes the entry from each row in main list and makes sub list @todo currently broken                        
                
            #read that column into a transition file
            #clean transition file
            #run rules that are rule run yes on transition file
            #return box name and amount if amount greater than 0

        def modify_rules(self):
            self.report(END,"This will pop up a new window")
            #pop up new gui to have user add mod and del rules
            #has checkbox for rule run yes/no
            
        def RESET(self):
            #global working_csv
            if askyesno('Verify Reset', 'Are you sure you want to undo all rule work?'):
                self.working_file = []
                
                        
#save button, takes working file turns into output file, 
        def save_csv(self):
            #add contents of working_file into imported_csv (probably a function)
            self.report(END, "Saving...")
        
            print self.imported_csv
            exportname = tkFileDialog.asksaveasfilename(filetypes=[('CSV (Comma Deliminated)', '.csv')], defaultextension=".csv", title="Save As")
            print exportname
        # write contents of list into .csv 
            with open(exportname, 'wb') as csvfile:
                output_file = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                #output_file.writerow(['please', 'work', 'damnit'])
                output_file.writerows(self.imported_csv)
        
if __name__ == '__main__': Carnac().mainloop() #if I'm run as a script
    
