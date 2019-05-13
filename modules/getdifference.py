def getdifference(): #Function that calculates the difference between two consecutive frames
    for i in range(len(blue)-1):
        blue[i] = (blue[i+1]-blue[i])
    for i in range(len(green)-1):
        green[i] = (green[i+1]-green[i])    
    for i in range(len(red)-1):
        red[i] = (red[i+1]-red[i])
    for i in range(len(hue)-1):
        hue[i] = abs(hue[i+1]-hue[i])
    for i in range(len(value)-1):
        value[i] = abs(value[i+1]-value[i])
    for i in range(len(saturation)-1):
        saturation[i] = abs(saturation[i+1]-saturation[i])

getdifference()
