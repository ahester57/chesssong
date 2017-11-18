import pygame
import time

pygame.mixer.init()
pygame.display.init()

screen = pygame.display.set_mode( (420, 240) )

playlist = list()
playlist.append( "midnightspecial.mp3" )
playlist.append( "crazyrap.mp3" )
playlist.append( "becauseigothigh.mp3" )

pygame.mixer.music.load( playlist.pop() )
#pygame.mixer.music.queue( playlist.pop() )
pygame.mixer.music.set_endevent( pygame.USEREVENT )
pygame.mixer.music.play()

run = True
while True:
    time.sleep(5)
    for e in pygame.event.get():
        if (e.type == pygame.USEREVENT): # track over
            if (len(playlist) > 0):
                pygame.mixer.music.queue( playlist.pop() )
            else:
                run = False


