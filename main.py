
import core

def setup():
    print("setup START______")
    core.fps = 30
    core.WINDOW_SIZE = [800,800]

def run():
    core.cleanScreen()
    core.printMemory()

core.main(setup,run)
