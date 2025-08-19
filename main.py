import pygame
from constants import * 
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)  # Create a player at the center of the screen
    clock = pygame.time.Clock() #object that helps tracking time
    dt = 0 # initializing delta time

    while True: #keeps looping infinitely until you tell it to stop
        for event in pygame.event.get(): # detects every event (mouse click, keyboard etc...)
            if event.type == pygame.QUIT: # pygame.QUIT is the event that happens when you click the close button on the window
                return

        player.update(dt)
        
        screen.fill("black")  # Or screen.fill((0, 0, 0)) - Fills the screen with black        
        player.draw(screen)
        pygame.display.flip()  # Update the display

        # time tracker/checker at the end of every loop iteration
        #it will pause the game loop until 1/60th of a second has passed
        dt = clock.tick(60) / 1000.0  # Convert milliseconds to seconds
        # "delta time" is the time that passed from one frame to another
        

if __name__ == "__main__":
    main()
