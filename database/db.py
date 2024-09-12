import sqlite3
from datetime import datetime
from typing import Dict, List, Union, Set
from .event import Event



class FoodDatabase:
    def __init__(self) -> None:
        """
        database already connect to table
        """
        self.connect_db()
        self.init_table()

    def connect_db(self) -> None:
        # create connection to food.db database
        self.con = sqlite3.connect("food.db")
        self.cur = self.con.cursor()  # create database cursors

    def init_table(self) -> None:
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS food_event(name,id,date,time,location,tags)")
        self.con.commit()

    def date_format(self, date: str) -> str:
        # format date Thur, Mar 07, 2024 -> Thu 2024-03-07
        try:
            date_parts = date.split(", ")
            date_parts[0] = date_parts[0][0:3]
            input_str = ', '.join(date_parts)

        # Format string indicating the format of the input string
            input_format = "%a, %b %d, %Y"

        # Parse the input string into a datetime object
            input_datetime = datetime.strptime(input_str, input_format)
            return str(input_datetime.strftime("%a") + " " + input_datetime.strftime("%Y-%m-%d"))

        except ValueError as e:
            return "Error:", e

    def add_event(self, event : Event) -> None:
        """
        insert individual event (dictionary) into database 
        """
        tags = ', '.join(event["tags"])  # Convert set to string
        self.cur.execute(f"INSERT INTO food_event VALUES(?, ?, ?, ?, ?, ?)", (event["name"], str(
            self.generate_id() + 1), str(self.date_format(event["date"])), str(event["time"]), str(event["location"]), tags))
        self.con.commit()

    def generate_id(self) -> int:
        """
        generate individual event id by its index in database
        """
        query = f"SELECT COUNT(*) FROM food_event"
        self.cur.execute(query)
        result = self.cur.fetchone()[0]+1
        return result

    def get_all_event(self) -> List[Dict[str, Union[str, Set[str]]]]:
        """
        return all event row in database
        """
        query = "SELECT * FROM food_event"
        self.cur.execute(query)
        rows = self.cur.fetchall()
        return rows
    
    def get_today_event(self) -> tuple:
        """
        return event only today from database
        """
        today = datetime.today()
        formatted_date = today.strftime("%a %Y-%m-%d")
        
        self.cur.execute("SELECT * FROM food_event WHERE date = ?", (formatted_date,))
        today_events = self.cur.fetchall()
        self.con.commit()
        
        return today_events if today_events else None
        
    def remove_data(self) -> None:
        """
        remove all rows
        only run if necessary
        """
        query = "DELETE FROM food_event"
        self.cur.execute(query)
        self.con.commit()
    
    def close_db(self) -> None:
        self.con.commit()
        self.cur.close()
        self.con.close()

    def __del__(self) -> None:
        self.close_db()


if __name__ == "__main__":
    db = FoodDatabase()
    # today = datetime.today()
    # formatted_date = today.strftime("%a %Y-%m-%d")
    # logging.info(f"Today is: {formatted_date}")
    # from bot.cron_job import scrape_data
    # scrape_data()
  