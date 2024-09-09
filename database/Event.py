from typing import Dict, Set, Union
# define Event object


class Event:
    def __init__(self, name="", id="", tags=set(), date="", time="", location="") -> None:
        self.name = name
        self.id = id
        self.tags = tags
        self.date = date
        self.time = time
        self.location = location

    def get_info(self) -> Dict[str, Union[str, Set[str]]]:
        return {"name": self.name,
                "id": self.id,
                "tags": self.tags,
                "date": self.date,
                "time": self.time,
                "location": self.location}