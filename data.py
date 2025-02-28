class Classes:
    def __init__(self, subject: str, days: str, start_time: str, end_time: str, units: int):
        self.subject = subject
        self.days = days
        self.start_time = start_time
        self.end_time = end_time
        self.units = units

    def __eq__(self, other):
        if isinstance(other,str):
            return other == self.subject
