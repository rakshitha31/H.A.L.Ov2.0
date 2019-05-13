from scipy import signal

detrend(): #Function that performs detrending on the array values
    dred= signal.detrend(red)
    dgreen = signal.detrend(green)
    dblue = signal.detrend(blue)
    dhue = signal.detrend(hue)
    dvalue = signal.detrend(value)
    dsaturation = signal.detrend(saturation)
    
detrend()
