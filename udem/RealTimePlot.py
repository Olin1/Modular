from pyArduinoPlot import *

maxSample = 100
sampleTime = 100
sizeData = 2
legendLabel = ['ax','ay','az','gx','gy','gz']
xLimit = [(0,maxSample)]*sizeData
yLimit = [(-20,20),(-20,20),(-20,20),(-500,500),(-500,500),(-500,500)]
style = ['r-','g-','b-','r-','g-','b-']
anim = []

port = 'COM3'
baudRate = 115200

arduino = realTimePlot(port,baudRate,maxSample,sizeData)
arduino.readSerialStart()

for i in range(sizeData):
     fig, ax = makeFigure(xLimit[i], yLimit[i],'Data'+str(i+1))
     lines = ax.plot([],[],style[i],label=legendLabel[i])[0]
     legendValue = ax.text(0.50,0.90,'',transform=ax.transAxes)
     anim.append(animation.FuncAnimation(fig,arduino.getSerialData,fargs = (lines,legendValue,legendLabel[i],i),interval = sampleTime))
     plt.legend(loc="upper left")
     plt.grid()

plt.show()

arduino.close()



