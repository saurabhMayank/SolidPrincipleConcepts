# srp video from Design patterns
# srp -> single responsibility principle
# soc -> seperation of concerns
# Both are same things

# A class or function should have single responsibility
# they should not hold multiple responsibilities

# Lets say -> need to make a journal class
# In Journal
# Primary Responsibilties
# We can add an entry
# We can remove an entry


# Version 1 of Journal
# Entries array to keep all the entries in the journal
# Count having -> count of number of entries in the journal
# User can add an entry or remove an entry from the journal
class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.entries.append(f"{self.count}: {text}")
        self.count += 1

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return "\n".join(self.entries)

# Now the requirement comes
# Lets say to save the entry in the DB
# Then option to Load an entry from DB or from the Web

# So If we implement these functions in the Journal class itself
# then this will break SRP
# Now journal is handling responisbilities that is not core to Journal Entity
# Saving to DB
# Loading to DB
# Loading from Web

# These are central functionalities -> That can be used for other types of Documents also
# If all these functionalities are not implemented in a central part For the whole application
# Any change in this functionality -> Will result in implementing this change in all the places
# where the functions are implemented
# So implementing them in Journal class -> Is really bad code


    # break SRP
    def save(self, filename):
        file = open(filename, "w")
        file.write(str(self))
        file.close()

    def load(self, filename):
        pass

    def load_from_web(self, uri):
        pass

# seperate class to handle
# saving and loading data from DB / WEB

class PersistenceManager:
    # save the content in the file
    # Content can be a journal, list, or important data
    # that can saved in a file
    def save_to_file(content, filename):
        file = open(filename, "w")
        file.write(str(journal))
        file.close()
    
    # here doc can be anything
    # can be file, sheets, pdf anything
    # will be saved to DB
    def save_doc_to_db(doc, filename):
        pass
    def load_from_db():
        pass
    def load_from_web():
        pass


j = Journal()
j.add_entry("I cried today.")
j.add_entry("I ate a bug.")
print(f"Journal entries:\n{j}\n")

p = PersistenceManager()
file = r'<put a file path>'
p.save_to_file(j, file)

# verify!
with open(file) as fh:
    print(fh.read())
