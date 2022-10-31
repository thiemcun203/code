class Battery:
    def __init__(self, energy=10):
        self.energy=energy
    def setEnergy(self, new_energy):
        self.energy=new_energy
    def getEnergy(self):
        return self.energy
    def decreaseEnergy(self):
        self.energy = self.energy  - 2
class FlashLamp(Battery):
    def __init__(self,energy,status=False ):
        self.status=status
        super().__init__(energy)
    def setBattery(self, b):
        Battery.setEnergy(self,b)
    def getBatteryInfo(self):
        return Battery().getEnergy() if Battery().getEnergy() >0 else 0
    def turnOn(self):
        self.status=True
        print("Light on" if Battery().getEnergy()  else "Light off")
    def turnOff(self):
        self.status=False
        print("Light off")
        self.decreaseEnergy()

class TestFlashLamp:
    def main():
        cuongtuat= Battery()
        cuong=FlashLamp(cuongtuat)
        for i in range(10):
            cuong.turnOn()
            cuong.turnOff()
        print(cuong.getBatteryInfo())
        
        
        
    
if __name__=="__main__":
    TestFlashLamp.main()  
    
        

        
        