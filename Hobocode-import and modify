# This is real python code! This will actually read in a file from disk
# and return to you its contents.
def read_file(file_path):
with open(file_path, 'r') as f:
data = f.read()
return data

# This is real python code! This will actually write data to a file on disk.
def write_file(file_path, content, mode="w"):
with open(file_path, mode) as stream:
stream.write(content)

# This will get populated by the load-in function
# which is triggered by the user
raw_csv_data = None

# This will be filled with the processed data from the
# spreadsheet. The structure of this object is faked below.
# The key here is the title of the user from the csv.
# The value are what rows from the raw data contain this type of user.
proc_csv_data = {
#   "grouping_bucket_from_csv": [1, 2, 3, 4],
}

# This object contains prettyfying labels for our "in memory" bucket names
pretty_names = {
    "ceo": "Chief Executive Officer",
    "grunt": "Valued Employee",
    "unknown": "UNKNOWN"
}

def load_csv_file(path):
    global raw_csv_data

    # @DEBUG
    # If this were for real you'd use something like:
    #    raw_csv_data = csv.parse(read_file(path)) 

    raw_csv_data = [
        ["Richie", "Bigshot", "CEO"],
        ["Joel", "Schmuckberg", "Grunt"]
    ]

# The arguments to this function correspond to which columns
# in the csv contain the salient data we want to extract.
# If you need more data to be extracted from the csv, simply add more args
# in the style of foo_col=index.
#
# The varname=value struct in python is how you define "default values" for args.
#
# This is saying unless you pass in something, use the second column for the title
# field, the first for the first name, and the second for the last name.
#
# You can in your little GUI render something to let the user specify what columns
# contain what data.
def process_csv_data(src_file, title_col=2, fname_col=0, lname_col=1):
    global proc_csv_data

    # Go get our CSV data
    load_csv_file(src_file)

    print "Starting data processing..."

    # set up an index counter to keep track of where we are in the list.
    index = 0

    for row in raw_csv_data:
        # This extract title function defined below is where all the magic happens
        title = extractTitle(row[title_col])

        # This little line of code checks to see if the title we returned is already
        # in our processed data. If it's not, we want to create an empty array to store
        # our data keys in.
        if title not in proc_csv_data:
            proc_csv_data[title] = []

        # Now we will definitely have proc_csv_data be a list (even if it's empty)
        # the first time, so we can now append our indicies to it!
        proc_csv_data[title].append(index)

        # Now we increment the index counter to keep everything working
        index += 1

    # At this point, all of our data is processed!
    print "Data processing complete!"

    # Create the headers for our CSV.
    # I always like to do this newline thing to indicate that it's a list of lists. Otherwise
    # I find having the two brackets next to each other [[ is hard to read at a glance.
    csv_output = [
        ["First Name", "Last Name", "Employee Bucket"]
    ]

    # This is a list we are going to use to prevent duplicate entries in the output CSV.
    # just incase something really crazy happens during processing, which it will.
    # Doing this is called "defensive programming". We are going to force the program
    # logic to guarantee that we never have duplicate data in the program output.
    has_already_displayed = []

    # Remember that our proc_csv_data only contains indices to the raw data array!
    for raw_title in proc_csv_data:
        # The raw title here is what type of user we think it is based on the
        # rules we applied in extractTitle. The way we've structured our data,
        # we group users by their title and then display them.

        # Because we're grouping by the type of user on it's title, we can get the display
        # name for all users of this type before we go through every user. This is just
        # more efficient than resetting this variable to the same value every time in the list.
        display_title = pretty_names[raw_title]

        # When you iterate through an object, you get it's keys. To get the values, you
        # need to request the value of the object at the key, which is what the 
        # proc_csv_data[raw_title] line does. The "for ... in ..." construct here will iterate
        # through the value at proc_csv_data, which is a list of the indices in raw data that
        # we want.
        for user_index in proc_csv_data[raw_title]:

            # Before we process the row, we need to ensure that we have not already
            # processed this user. Fundamentally, we can assume that the index of the
            # row in the raw data array is a unique identifier (there can only be one first row).
            
            # Knowing that, the first time we see a new array, we pop 
            # it into our `has_already_displayed' list. If the list doesn't contain the index,
            # then it's new data and should be processed.
            if user_index in has_already_displayed:
                # This is a keyword that tells the loop to stop here and go to the next item.
                continue

            # If we're here in the code, it means that we are processing a new item. First,
            # add that item index to the displayed list so we don't ever get a dupe.
            has_already_displayed.append(user_index)

            # Next, because this identifier is only the index of the data and not the data itself
            # we need to go grab the actual raw data.
            raw_data = raw_csv_data[user_index]
            first_name = raw_data[fname_col]
            last_name = raw_data[lname_col]

            # Finally, simply add this to the output list.
            csv_output.append(first_name, last_name, display_title)

    # We're almost done! All we need to do now is format the data.
    # Because we're saving to a CSV, we need to actually join our lists into strings
    # which are separated by commas. To do this is pretty simple. First, we create
    # one final list to contain the output:
    out = []

    # Then, for each row in our csv_output
    for row in csv_output:
        # We join the row data with a comma
        row = ",".join(row) # ["foo", "bar"] -becomes-> "foo,bar"

        # And then add this to the output list
        out.append(row)

    # Finally, we need to turn out list of strings into a string with line breaks so
    # we can write it into a file.
    # Right now we have this: ["foo,bar", "baz,gaz"]
    # And we need: "foo,bar\nbaz,gaz".

    # The "\n" is how you say "make a newline" in a string. When you hit enter, you are
    # inserting this special "escaped n" character, which renders as a linebreak. Neat, eh?
    out = "\n".join(out)

    # Our out variable is now in the "foo,bar\nbaz,gaz" format, so we can write it back to
    # disk!
    write_file(OUTPUT_FILE, out)

    print "Program completed!"
    print "File located at: {0}.format(OUTPUT_FILE)

# This is your rules engine. It needs to take in the title field from the CSV
# and output one of the expected "in progress" titles for a user. In this
# example, the acceptable values for inprogress titles are CEO and grunt.
# In the event no bucketing title can be computed, "unknown" is returned.
def extractTitle(csv_title_string):
    # This is the "do rules" (p)art of your program. You can do literally whatever
    # makes sense here, all that needs to happen is your output the string
    # identifier for the type of user.

    # Python lets you search strings for substrings using "in".
    # Example:
    #    "CEO" in "CEO, Dog, Person"; // True
    #    "CEO" in "C E O"; // False
    #    "CEO" in "CEORPHAN"; // True
    if "CEO" in user_title:
        return "ceo"

    # You can also do explicit string matching against a "set" of possible values:
    if user_title.lower() in ["grunt", "engineer", "manager", "accountant"]:
        return "grunt"

    # If we get to the last case, we don't know what the user is, so return our 
    # fallback value to keep everything happy.
    return "unknown"
