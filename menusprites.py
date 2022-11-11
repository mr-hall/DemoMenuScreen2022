import colours
import pygame
import constants

class Button():
    def __init__(self, txt, x, y):
        font = pygame.font.SysFont('Calibri', 25, True, False)
        self.txtimage = font.render(txt, True, colours.BLACK)
        self.colour = colours.GREEN
        self.nonhovercolour = colours.GREEN
        self.hovercolour = colours.BLUE
        self.rect = pygame.Rect(x, y, constants.BUTTON_WIDTH, constants.BUTTON_HEIGHT)
        self.width = 5

    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, self.rect)
        screen.blit(self.txtimage, (self.rect.x, self.rect.y))

    def check_mouse_over(self):
        if self.is_mouse_over():
            self.colour = self.hovercolour
        else:
            self.colour = self.nonhovercolour

    def is_mouse_over(self):
        mouse_position = pygame.mouse.get_pos()
        return self.rect.collidepoint(mouse_position)

