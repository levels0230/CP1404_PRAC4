CodeOfColour = {"AliceBlue": "#f0f8ff", "bisque1": "#ffe4c4",
                "bisque2": "#eed5b7", "bisque3": "#cdb79e",
                "bisque4": "#8b7d6b", "black": "#000000",
                "BlanchedAlmond": "#ffebcd", "blue1": "#0000ff",
                "blue2": "#0000ee", "blue4": "#00008b"}
ColourOfName = input("Enter the colour name: ")
while ColourOfName !="":
    print("The code for \"{}\" is {}".format(ColourOfName,CodeOfColour.get(ColourOfName)))
    ColourOfName = input("Enter the colour name: ")