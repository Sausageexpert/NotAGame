
# Pygame Events

you can use event.type == pygame.MOUSEMOTION to track the mouse, print(event.pos)
you can use event.type == pygame.MOUSEBUTTONDOWN to check if the mouse is being clicked, MOUSEBUTTONUP is obvious
same way, KEYDOWN and KEYUP.

if event.type == pygame.KEYDOWN:
    if event.key = pygame.K_SPACE:
        print(jump)