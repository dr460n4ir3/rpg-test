#!usr/bin/env python3

import tcod

from engine import Engine
from entity import Entity
from input_handlers import EventHandler
from procgen import generate_dungeon

def main() -> None:
    screen_width = 80
    screen_height = 50

    map_width = 80
    map_height = 45

    room_max_size = 10
    room_min_size = 6
    max_rooms = 30

    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    event_handler = EventHandler()

    player = Entity(int(screen_width / 2), int(screen_height / 2), "@", (255, 140, 0)) #color:dark_orange
    enemy = Entity(int(screen_width / 2 - 5), int(screen_height / 2), "E", (255, 0, 0)) #color:red
    weapon = Entity(int(screen_width / 2 + 5), int(screen_height / 2), "!", (0, 0, 255)) #color:blue
    gold = Entity(int(screen_width / 2 + 10), int(screen_height / 2), "$", (255, 255, 0)) #color:yellow
    potion = Entity(int(screen_width / 2 + 15), int(screen_height / 2), "*", (0, 255, 0)) #color:green
    health_potion = Entity(int(screen_width / 2 + 20), int(screen_height / 2), "%", (255, 255, 255)) #color:white
    armor = Entity(int(screen_width / 2 + 25), int(screen_height / 2), "^", (255, 0, 255)) #color:purple
    entities = {player, enemy, weapon, gold, potion, health_potion, armor}

    game_map = generate_dungeon(
        max_rooms=max_rooms,
        room_min_size=room_min_size,
        room_max_size=room_max_size,
        map_width=map_width,
        map_height=map_height,
        player=player,
    )

    engine = Engine(entities=entities, event_handler=event_handler, player=player, game_map=game_map)

    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="RPG Test Game",
        vsync=True,
    ) as context:
        root_console = tcod.Console(screen_width, screen_height, order="F")
        while True:
            engine.render(console=root_console, context=context)

            events = tcod.event.wait()
            
            engine.handle_events(events)
                
if __name__ == "__main__":
    main()