Carnac
======

Staff Role selector tool csv(excel) in csv(excel) out

Using Python 2.7.5

Carnac MUST be able to do 3 things:
Import a csv

Make changes to that csv based on rules

Export that csv

If it can do the above, then it is "working" If it completes all of the stretch goals it will be "finished."

Stretch goals include: making the tool's rules to be edited in the tool, and then run on the un-edited code.

Allow the user to select which rules will be applied

Allow the user to undo an action

Allow the user to select which column they would like to perform rules on

Allow the user to import a group of rules for a different project

#resources
http://docs.python.org/2/library/csv.html

effbot

#@todo
@todo add functionality of load and save apply to import_file_contents and output_file_contents

@todo test functionality of http://www.python-excel.org/

@todo better define _init_

@todo get better understanding of OOPS and (self) command

@todo learn how to make and call modules and how to defined arguments with homebrew module

#Program Pseudo code
Open window Have file menu and appropriate buttons

When import file selected, imports contents of csv(or excel) into import_file_contents and output_file_contents

Save as button outputs contents of output_file_contents

When run rules button is selected, process working_file_contents and replace as directed by rules 

After run rules finishes, it Prints list of rules with radio button and number of entries modified


When Rules Manage button selected bring up current rules loaded screen

Rules loaded screen contains method of creating new rule and positioning in list

Screen also has checklist for which rules to run and at bottom run rules



When radio button selected, prints rows of records for review, undo rule, undo changes made by rule

Revert button replaces output_file_contents with Import_file_contents prints: "File reverted to original"


