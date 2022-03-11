import SendAction


def control_lights(status):
    if status == "ON":
        SendAction.send_action("LIGHT_CONTROL", "LIGHTS_ON")
    else:
        SendAction.send_action("LIGHT_CONTROL", "LIGHTS_OFF")
