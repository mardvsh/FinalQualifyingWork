import pygame

def play_notification_sound():
    pygame.mixer.init()
    pygame.mixer.music.load("resources\sos.mp3")
    pygame.mixer.music.play()

