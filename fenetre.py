
class Fenetre:
        def __init__(self):
            self.hauteur = 400
            self.largeur = 400
            self.fps = 0
            self.couleur = (0, 0, 0)

        def set(self, core):
            core.bgColor = self.couleur
            core.WINDOW_SIZE = [self.hauteur, self.largeur]
            core.fps = self.fps
