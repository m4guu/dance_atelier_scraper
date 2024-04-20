class Instructor:
    def __init__(self, name, link):
        self.name = name
        self.link = link

    def __str__(self):
        return f"Instructor: {self.name}, Link: {self.link}"

    def default(self):
        return {
            "name": self.name,
            "link": self.link
        }
