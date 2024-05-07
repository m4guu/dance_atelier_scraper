class Day:
    def __init__(self, day_of_the_week):
        self.day_of_the_week = day_of_the_week
        self.events = []

    def add_event(self, event):
        self.events.append(event)

    def to_dict(self):
        return {
            'day_of_the_week': self.day_of_the_week,
            'events': [event.to_dict() for event in self.events]
        }
