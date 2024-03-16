from typing import Dict, Set, Union
# define Event object


class Event:
    def __init__(self) -> None:
        self.name = ""
        self.id = ""
        self.tags = set()
        self.date = ""
        self.time = ""
        self.location = ""

    def get_info(self) -> Dict[str, Union[str, Set[str]]]:
        return {"name": self.name,
                "id": self.id,
                "tags": self.tags,
                "date": self.date,
                "time": self.time,
                "location": self.location}