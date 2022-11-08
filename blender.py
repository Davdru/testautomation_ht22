

class Blender:
    thing: str
    result: str

    def __init__(self):
        self.thing = ""
        self.result = ""

    def add(self, thing):
        self.thing = thing

    def switch_on(self):
        if self.thing == "apple":
            self.result = "apple juice"
        self.thing = ""

