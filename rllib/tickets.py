"""Modelling the ticket categories of the festival"""

import csv
import json


class Tickets:
    """Class of the different ticket categories, which are up for sale for Rolling Loud Munich"""

    def __init__(self):
        """Checks if paths.json and tickets.csv file is accessable.
        Initializes the different ticket categories based on the `tickets.csv`
        There will also be a list `all_tickets`, which is initialized"""

        try:  # checks if the file is openable
            with open(r"RL-Library-Project\rllib\paths.json") as p:
                paths = json.load(p)
        except:
            raise RuntimeError(
                "The paths.json file could not been opened. Please check!"
            )

        try:  # checks if the file is openable
            file_path = paths["link_collection"][0]["links"][0]
            f = open(file_path, "r")
            reader = csv.reader(f)
        except:
            raise RuntimeError("The data.csv file could not been opened. Please check!")

        self.all_tickets = []  # all the tuples below will be saved in this list
        f.seek(0)
        weekend_ga = tuple(weekend_ga[1] for weekend_ga in reader)  # creates tuple
        self.all_tickets.append(weekend_ga)  # appending it to the list

        f.seek(0)
        weekend_ga_plus = tuple(weekend_ga_plus[2] for weekend_ga_plus in reader)
        self.all_tickets.append(weekend_ga_plus)

        f.seek(0)
        weekend_vip = tuple(weekend_vip[3] for weekend_vip in reader)
        self.all_tickets.append(weekend_vip)

        f.seek(0)
        weekend_munchies = tuple(weekend_munchies[4] for weekend_munchies in reader)
        self.all_tickets.append(weekend_munchies)

        f.seek(0)
        friday = tuple(friday[5] for friday in reader)
        self.all_tickets.append(friday)

        f.seek(0)
        friday_vip = tuple(friday_vip[6] for friday_vip in reader)
        self.all_tickets.append(friday_vip)

        f.seek(0)
        saturday = tuple(saturday[7] for saturday in reader)
        self.all_tickets.append(saturday)

        f.seek(0)
        saturday_vip = tuple(saturday_vip[8] for saturday_vip in reader)
        self.all_tickets.append(saturday_vip)

        f.seek(0)
        sunday = tuple(sunday[9] for sunday in reader)
        self.all_tickets.append(sunday)

        f.seek(0)
        sunday_vip = tuple(sunday_vip[10] for sunday_vip in reader)
        self.all_tickets.append(sunday_vip)

    def catch_userinput(
        self,
        single_day,
        incl_merch,
        fast_lane,
        sep_toilets,
        vip_area,
        below_100,
        below_200,
        below_300,
    ):
        """Catches the user input through GUI input.
        The parameters are the possibilities which a user can select searching his perfect ticket"""

        # the search gets filled up with all the different inputs from GUI
        self.search = (
            single_day,
            incl_merch,
            fast_lane,
            sep_toilets,
            vip_area,
            below_100,
            below_200,
            below_300,
        )

        # lists for different types of results
        self.exact_matches = []
        self.partial_matches = []
        self.max_match_count = 0

    def search_tickets(self):
        """Search algorithm, which searches for the best matching ticket(s), based on the user input (through GUI)
        This method takes values from the methods above"""

        for ticket in self.all_tickets:
            # counts the number of matches between the ticket's values and the user's search decisions
            self.match_count = sum(
                search_value == ticket[i + 1]
                for i, search_value in enumerate(self.search)
            )
            if self.match_count == 8:  # exact match
                self.exact_matches.append(
                    ticket[0]
                )  # first Index of tuple is given to exact_matches
            elif (
                self.match_count > self.max_match_count
            ):  # partial match with most matches so far
                self.partial_matches_first_point = [
                    ticket[0]
                ]  # re-initialized as a list containing the identifier of the current ticket
                self.max_match_count = (
                    self.match_count
                )  # max_match_count is updated to the new match_count.
            elif (
                self.match_count == self.max_match_count
            ):  # additional partial match with the same match count
                self.partial_matches_first_point.append(ticket[0])

        # returns the results
        if self.exact_matches:
            output = "Your exact match ticket(s): \n" + "\n".join(
                self.exact_matches
            )  # \n  is used to make sure that the output fits into the GUI Label
        elif self.partial_matches_first_point:
            output = "Tickets with the most matches:\n" + "\n".join(
                self.partial_matches_first_point
            )
        else:
            output = "No matching tickets found."

        return output
