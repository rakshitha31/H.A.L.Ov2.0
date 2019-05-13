import matplotlib.pyplot as plt

plot(): #Function to plot all the 6 ECG graphs obtained , that is -->Red,Green,Blue,Hue,Saturation,Value
    plt.figure(1)
    plt.plot(xf*10, yg3 , color="blue")
    plt.figure(2)
    plt.plot(xf*10, yg1 , color="red")
    plt.figure(3)
    plt.plot(xf*10, yg2, color="green")
    plt.figure(4)
    plt.plot(xf*10, yg4, color="cyan")
    plt.figure(5)
    plt.plot(xf*10, yg5, color="orange")
    plt.figure(6)
    plt.plot(xf*10, yg6, color="black")
    plt.show()
    
plot()
