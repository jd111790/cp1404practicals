

COLOUR_NAME_TO_HEX = {"absolute zero": "#0048ba", "amber": "#ffbf00",
                      "aqua": "#00ffff", "blue1": "#0000ff",
                      "brink pink": "#fb607f", "british racing green": "#004225",
                      "cardinal": "#c41e3a", "chestnut": "#954535",
                      "cobalt": "#0047ab", "crimson": "#dc143c"}

colour_name = input("Enter a colour: ").lower()
while colour_name != "":
    try:
        print("Hexadecimal:", COLOUR_NAME_TO_HEX[colour_name])
    except KeyError:
        print("Invalid colour name")
    colour_name = input("Enter a colour: ").lower()