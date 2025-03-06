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

    def __str__(self):
        return f"{self.subject} ({self.days}): {self.start_time} - {self.end_time}, {self.units} units"

    def __repr__(self):
        return f"Classes(subject={self.subject}, days={self.days}, start_time={self.start_time}, end_time={self.end_time}, units={self.units})"