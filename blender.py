

class Blender:
    thing: str
    result: str

    def __init__(self):
        self.thing = ""
        self.result = ""

    def add(self, thing):
        self.thing = thing
        print(self.thing)

    def switch_on(self):
        if self.thing == "apple":
            self.result = "apple juice"
        elif self.thing == "frog":
            self.result = "something disgusting"
        elif self.thing == "banana":
            self.result = "something disgusting"
        elif self.thing == "orange":
            self.result = "orange juice"
        self.thing = ""

