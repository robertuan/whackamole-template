import pygame
import random

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))

        x,y =0, 0
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    if x <= mouse_x < x + 32 and y <= mouse_y < y + 32:
                        x = random.randrange(0, 640, 32)
                        y = random.randrange(0, 512, 32)

            screen.fill((255, 193, 204))
            #vertical lines
            for i in range(0,640,32):
                pygame.draw.line(screen, "black", (i, 0), (i, 512))
            #horizontal lines
            for i in range(0,512,32):
                pygame.draw.line(screen, "black", (0, i), (640, i))
            screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
