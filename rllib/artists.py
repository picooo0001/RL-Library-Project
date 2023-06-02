""""Modelling the artists of the festival."""

import csv

class Artists:
    """Class of the artists who perform at Rolling Loud Munich
    
    The data of the artists is saved in `data.csv`"""
    
    def __init__(self):
        """Checks if the .csv file is accessable and instaziation of the args
        
        Args:
            name: name of the artist
            headliner: is the artist headliner or not (boolean)
            stage: main stage or secondary stage
            date: DD.MM.YYYY of when the artist is on stage
            time: the timespan for every artist on stage """
    
        
        try: #checks if the file is openable
            file_path = r"C:\Users\NicoPeuser\Desktop\rlli_tests\RL-Library-Project\rllib\data.csv"
            f = open(file_path, "r")
            reader = csv.reader(f)
        except:
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
        
    def check_rows(self):
        """ Checks if all rows are complete. If this is not the case, a RuntimeError will appear.
        The number 59 is pre defined. """
        
        #only artists collum will be checked, because all collums have the same length
        if len(self.artists) == 59:
            pass
        else:
            raise RuntimeError("Missing collum. Please check!")
            
    
    def search_artist(self, user_input):
        """Searchs for an artist by user input. It takes the data from the tuple above.
        Input: name of the artist (typecasting: everything besides special characters)
        Output: name, headliner, stage, time, date
        """
        
        user_input = user_input.replace(" ", "").lower() #typecasting
        found = False 
        output = None

        for artist in self.artists: #loops over the tuple artists
            formatted_artist = artist.replace(" ", "").lower() #typecasting
            if user_input in formatted_artist:
                index = formatted_artist.index(user_input) #find index to search in the other tuples
                headliner = self.headliner[index]
                if headliner == "true": #not necessary
                    headliner = "is headliner"
                else:
                    headliner = "no headliner"
                stage = self.stage[index]
                time = self.time[index]
                date = self.date[index]
                output = ", ".join([artist, stage, time, date]) #print the output in one line
                found = True #variable form above to true, function ends

        if not found: #= if found != true
            output = "Sorry! We couldn't find what you were looking for "
        
        return output
            
            
    def search_headliner(self):
        """Searches for a headliner by user input. It takes the data from the tuple above.
        Input: "headliner" (typecasting activated)
        Output: name, time and date
        """
    
        found = False
        found_indices = []
        output = ""
        user_input = "Headliner"
        
        if user_input.lower().replace(" ", "") == "headliner":
            user_input = "true"
        else:
            output = "Wrong input. Please redo!"
        while not found:
            for index, cell in enumerate(self.headliner):
                if cell == user_input:
                    found_indices.append(index)

            for index in found_indices:
                output += ", ".join([self.artists[index], self.time[index], self.date[index]]) + "\n"
                found = True

        if not found:
            output = "Sorry! We couldn't find what you were looking for!"
        
        return output
            
            
    def search_stage(self):
        """This is a search based on the stage you want to know by user input. It takes the data from 
        the tuple above.
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
    
    def search_time(self, user_input):
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
        
        
        
            
            
         
            
    
        








        

        
        
        
    
    
    