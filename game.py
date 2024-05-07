import pygame
# Test Kommentar eingefügt
pygame.init()
FELDKANTE = 82
RAHMENBREITE = 4
ROT = (255, 0, 0)
ROTH = (250, 105, 105)
BLAU = (5, 17, 25)
BLAUH = (125, 132, 254)
GRUEN = (36, 255, 3)
GRUENH = (159, 250, 145)
VIOLETT = (195, 2, 209)
VIOLETTH = (237, 125, 245)

class Spiel: 
#    def __init__(self, groesse):
    def __init__(self, horizontal, vertikal):
        self.horizontal = horizontal
        self.vertikal = vertikal
        self.FPS = 30
        self.clock = pygame.time.Clock()
        self.spielFeld = Feld(self.horizontal, self.vertikal)
        pygame.display.set_caption("Tectonic")
        self.running = True # While Loop laufen lassen
    def runSpiel(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False # While Loop abbrechen

            self.spielFeld.zeichnen()
            pygame.display.update()
#    def zeichnen(self):
#        self.screen.fill((0, 0, 0))
#       if self.spielStatus == 0: # Spiel beginnt
#            for button in self.buttons:
#                pygame.draw.rect(self.window, ROTH, (button.x_innen, button.y_innen, FELDKANTE, FELDKANTE))  
#            self.screen.blit(self.startHintergrund,
#                             self.startHintergrund.get_rect())
#            self.start.draw_button()
#            self.sound.draw_button()
#            self.anfaenger.draw_button()
#            self.exit.draw_button()
        
class Feld:
#    FELDKANTE = 82
#    RAHMENBREITE = 4
    def __init__(self, horizontal, vertikal):
        self.horizontal = horizontal
        self.vertikal = vertikal
        self.sbreite = self.horizontal * FELDKANTE + (self.horizontal + 1) * RAHMENBREITE
        self.shoehe = self.vertikal * FELDKANTE + (self.vertikal + 1) * RAHMENBREITE

        self.spielStatus = 0 # 0 = Startseite, 1 = Felder zuordnen, 2 = Zwischenräume füllen, 3 = vorhandene Zahlen einsetzen, 4 = lösen

        self.rand = 40
        self.window_width = self.sbreite + 2 * self.rand
        self.window_height = self.shoehe + 2 * self.rand
        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        self.window.fill((166, 171, 167)) 

        self.x_aussen = self.rand
        self.y_aussen = self.rand
        self.width_aussen = self.sbreite
        self.height_aussen = self.shoehe
        pygame.draw.rect(self.window, "black", (self.x_aussen, self.y_aussen, self.width_aussen, self.height_aussen))    

        self.x_innen = self.rand + RAHMENBREITE
        self.y_innen = self.rand + RAHMENBREITE
        self.width_innen = self.sbreite - 2 * RAHMENBREITE
        self.height_innen = self.shoehe - 2 * RAHMENBREITE
        pygame.draw.rect(self.window, "white", (self.x_innen, self.y_innen, self.width_innen, self.height_innen))    

        self.buttons = []
        for y in range(self.vertikal):
            for x in range(self.horizontal):
                print(y, x)
                self.buttons.append(Button(self.window, x, y, self.x_innen, self.y_innen, ROT, ROTH, str(y) + " " + str(x) ))
#        for button in self.buttons:
#            pygame.draw.rect(self.window, ROTH, (button.x_innen, button.y_innen, FELDKANTE, FELDKANTE))  
#        print(self.felder)
            
    def zeichnen(self):
#       self.screen.fill((0, 0, 0))
        if self.spielStatus == 0: # Spiel beginnt
            for button in self.buttons:
#                self.button.draw()
                pygame.draw.rect(self.window, ROTH, (button.x_innen, button.y_innen, FELDKANTE, FELDKANTE))  
#            self.screen.blit(self.startHintergrund,
#                             self.startHintergrund.get_rect())
#            self.start.draw_button()
#            self.sound.draw_button()
#            self.anfaenger.draw_button()
#            self.exit.draw_button()


class Button():
    # colours for button and text
    TEXT_COL = (0, 0, 0)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    WIDTH = 180
    HEIGHT = 70

    def __init__(self, window, x, y, x_innen, y_innen, buttonCol, hoverCol, text):
        self.window = window
        self.fkx = x
        self.fky = y
        self.x_innen = x_innen + self.fkx * (FELDKANTE + RAHMENBREITE)
        self.y_innen = y_innen + self.fky * (FELDKANTE + RAHMENBREITE)
        self.buttonCol = buttonCol
        self.hoverCol = hoverCol
        self.text = text
        button_rect = pygame.Rect(self.x_innen, self.y_innen, FELDKANTE, FELDKANTE)

    def draw_button(self):
        action = False
        pos = pygame.mouse.get_pos()
        # create pygame Rect object for the button
        button_rect = Rect(self.x, self.y, self.WIDTH, self.HEIGHT)
        # check mouseover and clicked conditions
#        if button_rect.collidepoint(pos):
#            pygame.draw.rect(self.screen, self.hoverCol, button_rect)
#        else:
#            pygame.draw.rect(self.screen, self.buttonCol, button_rect)
        # add shading to button
#        pygame.draw.line(self.screen, self.WHITE,
#                         (self.x, self.y), (self.x + self.WIDTH, self.y), 2)
#        pygame.draw.line(self.screen, self.WHITE,
#                         (self.x, self.y), (self.x, self.y + self.HEIGHT), 2)
#        pygame.draw.line(self.screen, self.BLACK, (self.x, self.y +
#                         self.HEIGHT), (self.x + self.WIDTH, self.y + self.HEIGHT), 2)
#        pygame.draw.line(self.screen, self.BLACK, (self.x + self.WIDTH,
#                         self.y), (self.x + self.WIDTH, self.y + self.HEIGHT), 2)
        # add text to button
        font = pygame.font.SysFont("comicsansms", 30)
        text_img = font.render(self.text, True, self.TEXT_COL)
        text_len = text_img.get_width()
        self.screen.blit(
            text_img, (self.x + int(self.WIDTH / 2) - int(text_len / 2), self.y + 13))
        return action


if __name__ == "__main__":
    # Spielinstanz und Spielstart
    spiel = Spiel(6, 6) # Breite, Höhe
    spiel.runSpiel()        