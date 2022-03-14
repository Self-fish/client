

import ApiController
import time


def deep_clean():
    ApiController.send_action("LIGHT_CONTROL", "LIGHTS_ON")
    ApiController.send_action("CLEAN_AQUARIUM", "EMPTY_BOMB_ON")
    starting_time = time.time()
    difference = 0
    print("")
    print("---------------------")
    print("Empty the aquarium...")
    print("---------------------")
    while difference < 300:
        difference = time.time() - starting_time
    ApiController.send_action("CLEAN_AQUARIUM", "EMPTY_BOMB_OFF")
    ApiController.send_action("CLEAN_AQUARIUM", "COVER_UP")
    print("")
    print("-------------------------")
    print("Press any key to continue")
    input("-------------------------")
    ApiController.send_action("CLEAN_AQUARIUM", "COVER_DOWN")
    time.sleep(5)
    ApiController.send_action("CLEAN_AQUARIUM", "FILLING_BOMB_ON")
    starting_time = time.time()
    difference = 0
    print("")
    print("-----------------------")
    print("Filling the aquarium...")
    print("-----------------------")
    while difference < 120:
        difference = time.time() - starting_time
    ApiController.send_action("CLEAN_AQUARIUM", "FILLING_BOMB_OFF")
    ApiController.send_action("CLEAN_AQUARIUM", "COVER_UP")
    print("")
    print("---------------------------------")
    print("Press any key to end the cleaning")
    input("---------------------------------")
    ApiController.send_action("CLEAN_AQUARIUM", "COVER_DOWN")
    ApiController.update_light_preferences()
