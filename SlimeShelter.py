import pygame
import sys
from pygame.locals import QUIT, Rect

import Codes.SystemChannel


def setting_import():
    settings_file = open("setting.txt", "r")
    settings = {}
    while True:
        line = settings_file.readline()
        line.replace("\n", "")
        if line:
            line = line.split(":")
            settings[line[0]] = int(line[1])
        else:
            break
    return settings


setting = setting_import()

Display_width = setting["Display_width"]
Display_height = setting["Display_height"]

Surface_width = 2400
Surface_height = 1600

display_ratio_x = Display_width / Surface_width
display_ratio_y = Display_height / Surface_height

FPS = setting["FPS"]

pygame.init()
DISPLAY = pygame.display.set_mode((Display_width, Display_height))
SURFACE = pygame.Surface((Surface_width, Surface_height))
FPSCLOCK = pygame.time.Clock()

gamestart_button_rect = Rect(225, 1200, 1950, 240)
gamestart_button_image = pygame.transform.scale(pygame.image.load("Resources/gamestart_button.png"),
                                                (gamestart_button_rect.width, gamestart_button_rect.height * 2))


def main():
    Channel = Codes.SystemChannel.SysChannel()
    while True:
        pygame_events = pygame.event.get()
        for pygame_event in pygame_events:
            if pygame_event.type == QUIT:
                pygame.quit()
                sys.exit()
            if pygame_event.type == pygame.MOUSEBUTTONDOWN:
                event_pos = pygame_event.pos
                event_pos = (event_pos[0] / display_ratio_x, event_pos[1] / display_ratio_y)

                if Channel.channel == 0:
                    if gamestart_button_rect.collidepoint(event_pos):
                        Channel.shift(1)

        PygameMouse = pygame.mouse.get_pos()
        PygameMouse = (PygameMouse[0] / display_ratio_x, PygameMouse[1] / display_ratio_y)

        SURFACE.fill((255, 0, 0))

        if Channel.channel == 0:
            if gamestart_button_rect.collidepoint(PygameMouse):
                SURFACE.blit(gamestart_button_image, gamestart_button_rect.topleft,
                             (0, gamestart_button_rect.height, gamestart_button_rect.width, gamestart_button_rect.height))
            else:
                SURFACE.blit(gamestart_button_image, gamestart_button_rect.topleft,
                             (0, 0, gamestart_button_rect.width, gamestart_button_rect.height))

        DISPLAY.blit(pygame.transform.scale(SURFACE, (Display_width, Display_height)), (0, 0))
        pygame.display.update()
        FPSCLOCK.tick(FPS)


if __name__ == "__main__":
    main()
