def dofft():  #Function that performs FFT on the detrended arrays and finds out the heartrate by taking the blue and hue signal into account
    yd1 = fft(dred)
    yd2 = fft(dgreen)
    yd3 = fft(dblue)
    yd4 = fft(dhue)
    yd5 = fft(dvalue)
    yd6 = fft(dsaturation)
    
    N = len(red)
    T = 1.0 / 100.0
    x = np.linspace(0.0, N*T, N) 
    
    yg1 = np.abs(yd1[:N//2])
    yg2 = np.abs(yd2[:N//2])
    yg3 = np.abs(yd3[:N//2])
    yg4 = np.abs(yd4[:N//2])
    yg5 = np.abs(yd5[:N//2])
    yg6 = np.abs(yd6[:N//2])
    
    xf = np.linspace(0.0, 1.0/(2.0*T), N/2)
    xint = list(xf)
    xf1 = xf*10
    
    # Method to convert all the x and y values into a dcitionary so that it can be iterated
    
    mylist0 = zip(xf1,yg3)
    mydict0 = dict(mylist0)
    xarray0 = mydict0.keys()
    yarray0 = mydict0.values()
    print(xf1)
    print(yg2)
    
    # Finds the heartrate of the person according to the blue color
    a0=[]
    for key in xarray0:
        a0.append(key)
    b0 = []
    for values in yarray0:
        b0.append(values)
    max0 = 0
    maxx = 0
    for ij in range(len(b0)):
        if(a0[ij] > 65 and a0[ij] < 120 ):
                if( b0[ij] > max0 and ( b0[ij] < 100 and b0[ij] > 65 ) ):
                    max0 = b0[ij]
                    maxx = a0[ij]
    print(max0)
    print(maxx)
    
    # Finds the heartrate of the person according to the Hue changes
    
    mylist1 = zip(xf1,yg4)
    mydict1 = dict(mylist1)
    xarray1 = mydict1.keys()
    yarray1 = mydict1.values()
    a1=[]
    for key in xarray1:
        a1.append(key)
    b1 = []
    for values in yarray1:
        b1.append(values)
    max1 = 0
    maxx1 = 0
    for ij in range(len(b1)):
        if(a1[ij] > 65 and a1[ij] < 120 ):
                if( b1[ij] > max1 and ( b1[ij] < 100 and b1[ij] > 65 ) ):
                    max1 = b1[ij]
                    maxx1 = a1[ij]
    print(max1)
    print(maxx1)
    
