class Event:
    def __init__(self):
        self.events = {}

    def on(self, event_name, callback):
        self.events[event_name] = callback

    def trigger(self, event_name):
        if event_name in self.events:
            self.events[event_name]()
        else:
            print("trigger is not found")

    def off(self, event_name):
        if event_name in self.events:
            del self.events[event_name]

event = Event()
event.on("onClickButton1", lambda: print("button 1 rocks!"))
event.on("onClickButton2", lambda: print("button 2 rocks!"))
event.on("onClickButton3", lambda: print("button 3 rocks!"))
event.trigger("onClickButton2")
event.on("onClickButton2", lambda: print("button 2 rocks too much!"))
event.trigger("onClickButton2")

event = Event()
event.on("onClickButton1", lambda: print("button 1 rocks!"))
event.on("onClickButton2", lambda: print("button 2 rocks!"))
event.on("onClickButton3", lambda: print("button 3 rocks!"))
event.off("onClickButton1")
event.off("onClickButton2")
event.off("onClickButton3")
event.trigger("onClickButton1")
event.trigger("onClickButton2")
event.trigger("onClickButton3")
