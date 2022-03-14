import ApiController


def control_lights(status):
    if status == "ON":
        ApiController.send_action("LIGHT_CONTROL", "LIGHTS_ON")
    else:
        ApiController.send_action("LIGHT_CONTROL", "LIGHTS_OFF")
