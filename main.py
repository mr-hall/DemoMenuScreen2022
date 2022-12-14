import pygame
import states


class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800,600))
        self.state = states.Menu()
        self.running = True

    def gameloop(self):
        while self.running:
            for event in pygame.event.get():
                self.state.handle_event(event)
            self.state.update()
            self.state.draw(self.screen)
            pygame.display.flip()
            if self.state.done:
                if self.state.next_screen:
                    self.state = self.state.next_screen
                else:
                    self.running = False


myGame = Game()
myGame.gameloop()
pygame.quit()