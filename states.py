import pygame
import colours
import menusprites


class State():
    def __init__(self):
        self.done = False
        self.next_screen = None

    def handle_event(self, event):
        if event.type == pygame.QUIT:

            self.done = True

    def update(self):
        pass

    def draw(self, screen):
        pass



class Menu(State):
    def __init__(self):
        super().__init__()
        self.buttons = [ menusprites.Button("Start Game", 30, 50),
                         menusprites.Button("Options", 30, 250),
                         menusprites.Button("Quit", 30, 350)
                         ]



    def handle_event(self, event):
        super().handle_event(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in self.buttons:
                if button.is_mouse_over():
                    self.next_screen = Game()
                    self.done = True


    def update(self):
        for button in self.buttons:
            button.check_mouse_over()

    def draw(self, screen):
        screen.fill(colours.RED)
        for button in self.buttons:
            button.draw(screen)

class Game(State):
    def __init__(self):
        super().__init__()

    def draw(self, screen):
        screen.fill(colours.GREEN)