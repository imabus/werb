import os
import magichue

user = ""
password = ""
api = ""
light1 = ""
light2 = ""

#set up magichue
def render():
    global user
    global password
    global api
    global light1
    global light2

    user = 'churjaydan@gmail.com'
    password = 'mana1@1@'
    api = magichue.RemoteAPI.login_with_user_password(user=user, password=password)
    light2 = api.get_online_bulbs()[0]
    light1 = api.get_online_bulbs()[1]



colours = {'red':(255,0,0), 'green':(0,255,0), 'blue':(0,0,255), 'purple':(255,0,255), 'cyan':(0,255,255)}
power = {"on": True, "off":False}
old_colour1 = ()
old_colour2 = ()
chosen_light = 3
render()




def change_colour(colour):
    global old_colour1
    global old_colour2
    
    old_colour1 = light1.rgb
    old_colour2 = light2.rgb
    light1.rgb = colours[colour]
    light2.rgb = colours[colour]

def Power(command):
    if chosen_light == 1:
        light1.on = power[command]
    elif chosen_light == 2:
        light2.on = power[command]
    else:
        light1.on = power[command]
        light2.on = power[command]

def go_back():
    if chosen_light == 1:
        light1.rgb = old_colour1
    elif chosen_light == 2:
        light2.rgb = old_colour2
    elif chosen_light == 3:
        light1.rgb = old_colour1
        light2.rgb = old_colour2

    
def save_colour():
    global colours
    colour_name = input("name: ")
    if chosen_light == 1:
        colours[colour_name] = light1.rgb
    elif chosen_light == 2:
        colours[colour_name] = light2.rgb
    elif chosen_light == 3 and light1.rgb == light2.rgb:
        colours[colour_name] = light1.rg

def brightness(command):
    brightness = int(command[10:])
    light1.brightness = (brightness * 2)
    print(f"set brightness to {brightness}")


def set_rgb(x):
    try:
        #x = int(command[6::])

        vals = x.split(", ")
        r = int(vals[0])
        g = int(vals[1])
        b = int(vals[2])
        if chosen_light == 1:
            light1.r = r
            light1.g = g
            light1.b = b
        elif chosen_light == 2:
            light2.r = r
            light2.g = g
            light2.b = b
        elif chosen_light == 3:
            light1.r = r
            light1.g = g
            light1.b = b
            light2.r = r
            light2.g = g
            light2.b = b
    except:
        exit()


def operate(command):
    global chosen_light
    x = ""
    if command in colours:
        change_colour(command)
        x = f"changed colour to {command}"
    elif 'brightness' in command:
        brightness(command)
        x = f"set brightness to {command}"
    elif command == "light1":
        chosen_light = 1
        x = f"selected light {chosen_light}"
    elif command == "light2":
        chosen_light = 2
        x = f"selected light {chosen_light}"
    elif command == "both":
        chosen_light = 3
        x = "selected both lights"
    elif command == "clear":
        os.system('cls' if os.name == 'nt' else 'clear')
    elif command == "go back":
        go_back()
        x = "set to previous colour"
    elif command in power:
        Power(command)
        x = f"turned lights {command}"
    elif "set rgb" in command:
        set_rgb(command)
    elif command == "save colour":
        save_colour()
    elif command == "reload":
        render()
        x = f"reloaded"
    else:
        try:
            x = eval(command)
        except:
            x = "unknown command"
    return x

