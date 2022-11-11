import pygame

class State():
    def __init__(self):
        self.done = False

    def handle_event(self, event):
        print("hello", event)
        if event.type == pygame.QUIT:

            self.done = True

    def update(self):
        pass

    def draw(self, screen):
        pass



class Menu(State):
    def __init__(self):
        super().__init__()

    def handle_event(self, event):
        super().handle_event(event)
