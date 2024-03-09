import sqlite3

#create a connection to food.db database 

class FoodDatabase():
    def __init__(self):
        self.connect_db()
        self.init_table()
    def connect_db(self):
        self.con = sqlite3.connect("food.db") #return Connection object
        self.cur = self.con.cursor() #create database cursors
    def init_table(self):
        self.cur.execute("CREATE TABLE IF NOT EXISTS food_event(name,id,date,time,location,tags)")
        self.con.commit()
    def add_event(self,event_list):
        for event in event_list:
            self.cur.execute(f"INSERT INTO food_event VALUES(?, ?, ?, ?, ?, ?)", (event["name"], str(self.generate_id() + 1), event["date"], event["time"], event["location"], event["tags"]))
            self.con.commit()
    def generate_id(self):
        query = f"SELECT COUNT(*) FROM food_event"
        self.cur.execute(query)
        result = self.cur.fetchone()[0]+1
        return result
    def close_db(self):
        self.con.commit()
        self.cur.close()
        self.con.close()
    def __del__(self):
        self.close_db()
    def get_all_event(self):
        query = "SELECT * FROM food_event"
        self.cur.execute(query)
        rows = self.cur.fetchall()
        return rows
    def remove_data(self):
        query = "DELETE FROM food_event"
        self.cur.execute(query)
        self.con.commit()

if __name__ == "__main__":
    db = FoodDatabase()
    
    events = [
        {"name": "Event1", "date": "2024-03-09", "time": "12:00", "location": "Location1", "tags": "tag1"},
        {"name": "Event2", "date": "2024-03-10", "time": "13:00", "location": "Location2", "tags": "tag2"},
        {"name": "Event3", "date": "2024-03-11", "time": "14:00", "location": "Location3", "tags": "tag3"},
        {"name": "Event4", "date": "2024-03-12", "time": "15:00", "location": "Location4", "tags": "tag4"},
        {"name": "Event5", "date": "2024-03-13", "time": "16:00", "location": "Location5", "tags": "tag5"},
        {"name": "Event6", "date": "2024-03-14", "time": "17:00", "location": "Location6", "tags": "tag6"},
        {"name": "Event7", "date": "2024-03-15", "time": "18:00", "location": "Location7", "tags": "tag7"},
        {"name": "Event8", "date": "2024-03-16", "time": "19:00", "location": "Location8", "tags": "tag8"},
        {"name": "Event9", "date": "2024-03-17", "time": "20:00", "location": "Location9", "tags": "tag9"},
        {"name": "Event10", "date": "2024-03-18", "time": "21:00", "location": "Location10", "tags": "tag10"}
    ]
    db.add_event(events)
    events = db.get_all_event()
    for event in events:
        print(event)
    
    
    






