class Event:
    def __init__(self, time, name, instructor, level):
        self.time = time
        self.name = name
        self.instructor = instructor
        self.level = level

    def to_dict(self):
        return {
            'time': self.time,
            'name': self.name,
            # Konwertujemy obiekt Instructor na słownik
            'instructor': self.instructor.__dict__,
            'level': self.level
        }
