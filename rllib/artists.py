""""Modelling the artists of the festival"""

import csv
import json

class Artists:
    """Class of the artists who are performing at Rolling Loud Munich
    The data of the artists is saved in `data.csv`"""
    
    def __init__(self):
        """Checks if the `data.csv` and `paths.csv` file is accessable and initialization of the args
        
        Args:
            name: name of the artist
            headliner: is the artist headliner or not (boolean)
            stage: main stage or secondary stage
            date: DD.MM.YYYY of when the artist is on stage
            time: the timespan for every artist on stage"""
    
        try: #checks if the file is openable
            with open(r'RL-Library-Project\rllib\paths.json') as p:
                paths = json.load(p)
        except:
            raise RuntimeError("The paths.json file could not been opened. Please check!")

        try: #checks if the file is openable
            file_path = paths["link_collection"][1]["links"][0]
            f = open(file_path, 'r')
            reader = csv.reader(f)
        except: #raises error if not, so the GUI wont open at all
            raise RuntimeError("The data.csv file could not been opened. Please check!")
                           
        next(reader) #header line will be skipped, that only the important data will be written in file
        self.artists = tuple(artists[0] for artists in reader)
        f.seek(0) #resets the "read" state of the file
        next(reader)
        self.headliner = tuple(headliner[1] for headliner in reader)
        f.seek(0)
        next(reader)
        self.stage = tuple(stage[2] for stage in reader)
        f.seek(0)
        next(reader)
        self.date = tuple(date[4] for date in reader)
        f.seek(0)
        next(reader)
        self.time = tuple(time[3] for time in reader)
        f.seek(0)
        next(reader)

    def __len__(self): #not very usefull, implemented before we had a proper plan, same goes for __getitem__
        """Returns the number of artists"""
        return len(self.artists)
    
    def __getitem__(self, index):
        """Returns the artist details at the provided index"""
        artist = self.artists[index]
        headliner = self.headliner[index]
        stage = self.stage[index]
        date = self.date[index]
        time = self.time[index]
        return {
            'artist': artist,
            'headliner': headliner,
            'stage': stage,
            'date': date,
            'time': time
        }

    def check_rows(self):
        """Checks if all rows are complete. If this is not the case, a RuntimeError will be raised."""
        if len(self) == 59:
            pass
        else:
            raise RuntimeError("Missing column. Please check!")

      
    def check_rows(self):
        """Checks if all rows are complete. If this is not the case, a RuntimeError will appear.
        The number 59 is predefined"""
        
        #only artists collum will be checked, because all collumns have the same length
        if len(self.artists) == 59:
            pass
        else:
            raise RuntimeError("Missing collum. Please check!")
            
    
    def search_artist(self, user_input):
        """Searchs for an artist by user input (GUI). It takes the data from the tuple above.
        Input: name of the artist (typecasting: everything besides special characters) (through GUI)
        Output: name, headliner, stage, time, date"""
        
        user_input = user_input.replace(" ", "").lower() #typecasting
        found = False 
        output = None

        for artist in self.artists: #loops over the tuple artists
            formatted_artist = artist.replace(" ", "").lower() #typecasting
            if user_input in formatted_artist:
                index = formatted_artist.index(user_input) #finds index to search in the other tuples
                headliner = self.headliner[index]
                if headliner == "true": #not necessary
                    headliner = "is headliner"
                else:
                    headliner = "no headliner"
                stage = self.stage[index] #searches in index of other tuples
                time = self.time[index]
                date = self.date[index]
                output = ", ".join([artist, stage, time, date]) #saves the found values together in `output`
                found = True #variable form above to true, function ends

        if not found: #= if found != true
            output = "Sorry! We couldn't find what you were looking for "
        
        return output #returns output
            
            
    def search_headliner(self):
        """Searches for a headliner by user input. It takes the data from the tuple above.
        Input: pressing a button in the GUI
        Output: name, time and date"""

        found_indices = [] #list to store the found indices in different collums
        user_input = "true" #predefined value
        
        if user_input == "true":
            for index, cell in enumerate(self.headliner): #searches for matching cell
                if cell == user_input:
                    found_indices.append(index) #appends the index of the found cell

            if found_indices:
                output = "\n".join([f"{self.artists[index]}, {self.time[index]}, {self.date[index]}" for index in found_indices]) #searches the index in other collums
            else:
                output = "Sorry! We couldn't find what you were looking for!" 
        else:
            output = "Wrong input. Please redo!"
        return output #return the result
            
            
    def search_stage(self): # not very important (not implemented)
        """This is a search based on the stage you want to know by user input. 
        It takes the data from the tuple above.
        Input: mainstage / secondarystage (typecasting activated)
        Output: name, date, time"""
        
        user_input = input("Search Stage: ") 
        user_input = user_input.replace(" ", "").lower()
        found_indices = []
        found = False
        output = None

        while not found:
            for index, stage in enumerate(self.stage):
                formatted_stage = stage.replace(" ", "").lower()
                if user_input in formatted_stage:
                    found_indices.append(index)

            for index in found_indices:
                output = ", ".join([self.artists[index], self.date[index], self.time[index]])
                found = True

        if not found:
            output = "Sorry! We couldn't find what you were looking for!"

        return output
    
    def search_time(self, user_input): #same logic as above 
        """This is a search, based on the time by user input. It takes the data from the tuple above.
        Input: timespan (through GUI)
        output: Date, Artist and Stage"""

        found_indices = []
        found = False
        output = ""

        while not found:
            for index, time_span in enumerate(self.time): 
                if time_span in user_input:
                    found_indices.append(index)

            for index in found_indices:
                output += ", ".join([self.date[index], self.artists[index], self.stage[index]]) + "\n"
                found = True

            if not found:
                output = "Sorry! We couldn't find what you were looking for!"
                print(output)
        return output       
        
        
        
            
            
         
            
    
        








        

        
        
        
    
    
    