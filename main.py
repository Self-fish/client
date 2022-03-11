import ControlLights
import DeepClean
import SoftClean

if __name__ == '__main__':
    print("")
    print("Please select one option:")
    print("[1] Turn ON Lights")
    print("[2] Turn OFF Lights")
    print("[3] Soft clean aquarium")
    print("[4] Deep clean aquarium")
    x = input("")
    if x == "1":
        ControlLights.control_lights("ON")
    elif x == "2":
        ControlLights.control_lights("OFF")
    elif x == "3":
        SoftClean.sof_clean()
    elif x == "4":
        DeepClean.deep_clean()
