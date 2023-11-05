#!usr/bin/env python3

import tcod
#import time

from actions import EscapeAction, MovementAction
#from entity import Entity
from input_handlers import EventHandler

def main() -> None:
    screen_width = 80
    screen_height = 50

    player_x = int(screen_width / 2)
    player_y = int(screen_height / 2)

    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    event_handler = EventHandler()

    # player = Entity(int(screen_width / 2), int(screen_height / 2), "@", (255, 255, 255))
    # npc = Entity(int(screen_width / 2 - 5), int(screen_height / 2), "@", (255, 255, 0))
    # weapon = Entity(int(screen_width / 2 + 5), int(screen_height / 2), "!", (0, 0, 255))
    # money = Entity(int(screen_width / 2 + 10), int(screen_height / 2), "$", (0, 255, 0))
    # potion = Entity(int(screen_width / 2 + 15), int(screen_height / 2), "!", (255, 255, 0))
    # health_potion = Entity(int(screen_width / 2 + 20), int(screen_height / 2), "!", (255, 255, 255))
    # armor = Entity(int(screen_width / 2 + 25), int(screen_height / 2), "!", (255, 0, 255))
    # entities = {npc, weapon, money, potion, health_potion, armor, player}

    dark_orange = tcod.Color(255, 140, 0) # Color for the player
    black = tcod.Color(0, 0, 0) # Color for the background
    red = tcod.Color(255, 0, 0) # Color for the enemy
    blue = tcod.Color(0, 0, 255) # Color for the weapon
    green = tcod.Color(0, 255, 0) # Color for the money
    yellow = tcod.Color(255, 255, 0) # Color for the potion
    white = tcod.Color(255, 255, 255) # Color for the health potion
    purple = tcod.Color(255, 0, 255) # Color for the armor


    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="RPG Test Game",
        vsync=True,
    ) as context:
        root_console = tcod.Console(screen_width, screen_height, order="F")
        while True:
            root_console.print(x=player_x, y=player_y, string="@", fg=dark_orange, bg=black)
            context.present(root_console)
            # root_console.print(x=player.x, y=player.y, string=player.char, fg=player.color)

            root_console.clear()

            for event in tcod.event.wait():
                action = event_handler.dispatch(event)

                if action is None:
                    continue

                if isinstance(action, MovementAction):
                    player_x += action.dx
                    player_y += action.dy
                    # player.move(dx=action.dx, dy=action.dy)

                elif isinstance(action, EscapeAction):
                    raise SystemExit()
                
if __name__ == "__main__":
    main()