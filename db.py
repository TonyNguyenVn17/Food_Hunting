import sqlite3
from datetime import datetime


class FoodDatabase():
    def __init__(self):
        """
        database already connect to table
        """
        self.connect_db()
        self.init_table()
    def connect_db(self):
        self.con = sqlite3.connect("food.db") ##create connection to food.db database 
        self.cur = self.con.cursor() #create database cursors
    def init_table(self):
        self.cur.execute("CREATE TABLE IF NOT EXISTS food_event(name,id,date,time,location,tags)")
        self.con.commit()
    def date_format(self,date):   #format date Thur, Mar 07, 2024 -> Thu 2024-03-07
        try:
            vcl = date.split(", ")
            vcl[0] = vcl[0][0:3]
            input_str = ', '.join(vcl)

        # Format string indicating the format of the input string
            input_format = "%a, %b %d, %Y"

        # Parse the input string into a datetime object
            input_datetime = datetime.strptime(input_str, input_format)
            return input_datetime.strftime("%a") + " "+ input_datetime.strftime("%Y-%m-%d")

        except ValueError as e:
            return "Error:", e
    def add_event(self,event):
        """
        insert individual event (dictionary) into database 
        """
        self.cur.execute(f"INSERT INTO food_event VALUES(?, ?, ?, ?, ?, ?)", (event["name"], str(self.generate_id() + 1), self.date_format(event["date"]), event["time"], event["location"], event["tags"]))
        self.con.commit()
    def generate_id(self):
        """
        generate individual event id by its index in database
        """
        query = f"SELECT COUNT(*) FROM food_event"
        self.cur.execute(query)
        result = self.cur.fetchone()[0]+1
        return result
    def get_all_event(self):
        """
        return all event row in database
        """
        query = "SELECT * FROM food_event"
        self.cur.execute(query)
        rows = self.cur.fetchall()
        return rows
    def remove_data(self):
        """
        remove all rows
        only run if necessary
        """
        query = "DELETE FROM food_event"
        self.cur.execute(query)
        self.con.commit()
    def __del__(self):
        self.close_db()
    def close_db(self):
        self.con.commit()
        self.cur.close()
        self.con.close()

if __name__ == "__main__":
    db = FoodDatabase()
    
    # mock data
    events = [
        {"name": "Event1", "date": "Thur, Mar 07, 2024", "time": "12:00", "location": "Location1", "tags": "tag1"},
        {"name": "Event2", "date": "Mon, Mar 07, 2024", "time": "13:00", "location": "Location2", "tags": "tag2"},
        {"name": "Event3", "date": "Tues, Mar 07, 2024", "time": "14:00", "location": "Location3", "tags": "tag3"},
        {"name": "Event4", "date": "Wed, Mar 07, 2024", "time": "15:00", "location": "Location4", "tags": "tag4"},
        {"name": "Event5", "date": "Thur, Mar 07, 2024", "time": "16:00", "location": "Location5", "tags": "tag5"},
        {"name": "Event6", "date": "Thur, Mar 07, 2024", "time": "17:00", "location": "Location6", "tags": "tag6"},
        {"name": "Event7", "date": "Fri, Mar 07, 2024", "time": "18:00", "location": "Location7", "tags": "tag7"},
        {"name": "Event8", "date": "Sun, Mar 07, 2024", "time": "19:00", "location": "Location8", "tags": "tag8"},
        {"name": "Event9", "date": "Sat, Mar 07, 2024", "time": "20:00", "location": "Location9", "tags": "tag9"},
        {"name": "Event10", "date": "Thur, Mar 07, 2024", "time": "21:00", "location": "Location10", "tags": "tag10"}
    ]

    for event in events:
        db.add_event(event)

    
   
    events = db.get_all_event()
    for event in events:
        print(event)
    
    
    






