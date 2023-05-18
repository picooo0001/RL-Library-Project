""""Modelling the artists of the festival."""

import json

class Artists:
    """Class of the artists who perform at Rolling Loud Munich
    
    The data of the artists is saved in `data.json`"""
    
    def __init__(self, name, headliner, stage, time, date): #name, headliner, etc, useful? notwendig
        """Reads the file `data.json` 
        and checks if every arg has its values (one for every artist)
        
        Args:
            name: name of the artist
            headliner: is the artist headliner or not (boolean)
            stage: main stage or secondary stage
            time: the timespan for every artist on stage 
            date: DD/MM/YYYY of when the artist is on stage"""
        
        try:
            f = open("rllib/data.json")
            data = json.load(f)
        except:
            raise RuntimeError("The `data.json` file could not been opened. Please check!")
            
        names = (artist["name"] for artist in data["artists"])
        stage = (artist["stage"] for artist in data["artists"])
        time = (artist["time"] for artist in data["artists"])
        date = (artist["date"] for artist in data["artists"])

        if all(names) & all(headliner) & all(time) & all(date):
            pass
        else:
            raise RuntimeError("There are missing values in `names` section. Please check!")
            
        #To-Do check "Headliner" Values

        f.close()
            
            
        

        
        
        
    
    
    