import random

class Component:
    def __init__(self, model, manufacturer, power_usage):
        self.model = model
        self.manufacturer = manufacturer
        self.power_usage = power_usage
        self.status = "ok" # Статус по умолчанию

    def get_info(self):
        return f"Model: {self.model}, Manufacturer: {self.manufacturer}, Power Usage: {self.power_usage}W, Status: {self.status}"

    def run_diagnostic(self):
        raise NotImplementedError("This method should be implemented by subclasses")

class CPU(Component):
    def __init__(self, model, manufacturer, power_usage, cores, frequency, temperature, status="OK"):
        super().__init__(model, manufacturer, power_usage)
        self.cores = cores
        self.frequency = frequency
        self.temperature = temperature
        self.status = status

    def run_diagnostic(self):
        temp = random.randint(40, 100) # Случайная температура
        if temp > 85:
            self.status = "overheating"
            return False
        self.status = "OK"
        return True

class GPU(Component):
    def __init__(self, model, manufacturer, power_usage, vram, frequency, driver_installed, status="OK"):
        super().__init__(model, manufacturer, power_usage)
        self.vram = vram
        self.frequency = frequency
        self.driver_installed = driver_installed
        self.status = status

    def run_diagnostic(self):
        if not self.driver_installed or self.vram < 2:
            self.status = "missing drivers or low VRAM"
            return False
        self.status = "OK"
        return True

class RAM(Component):
    def __init__(self, model, manufacturer, power_usage, size, frequency, usage, status="OK"):
        super().__init__(model, manufacturer, power_usage)
        self.size = size
        self.frequency = frequency
        self.usage = usage
        self.status = status

    def run_diagnostic(self):
        if self.usage > 95 or self.size < 2:
            self.status = "memory error"
            return False
        self.status = "OK"
        return True

class Storage(Component):
    def __init__(self, model, manufacturer, power_usage, storage_type, capacity, read_speed, bad_sectors, status="OK"):
        super().__init__(model, manufacturer, power_usage)
        self.storage_type = storage_type
        self.capacity = capacity # В GB или TB
        self.read_speed = read_speed # В MB/s
        self.bad_sectors = bad_sectors
        self.status = status

    def run_diagnostic(self):
        if self.read_speed < 10 or self.bad_sectors > 100:
            self.status = "read speed is low or too many bad sectors"
            return False
        self.status = "OK"
        return True

# Создание объектов
cpu_component = CPU(model="Intel i7-12700", manufacturer="Intel", power_usage=65, cores=8, frequency=3.6, temperature=50)
gpu_component = GPU(model="RTX 3080", manufacturer="NVIDIA", power_usage=320, vram=10, frequency=1.71, driver_installed=True)
ram_component = RAM(model="DDR4", manufacturer="Corsair", power_usage=15, size=16, frequency=3200, usage=50)
storage_component = Storage(model="Samsung 970 EVO", manufacturer="Samsung", power_usage=15, storage_type="SSD", capacity=1000, read_speed=3500, bad_sectors=0)

# Добавление объектов в список
compArr = [cpu_component, gpu_component, ram_component, storage_component]

# Вывод информации и диагностика
for component in compArr:
    print(component.get_info())
    print(f"Diagnostic: {component.run_diagnostic()}")
    print(f"Status: {component.status}\n")



class Computer:
    def __init__(self):
        self.components = []
    
    def addComponents(self,component):
        self.components.append(component)
        
    
    def totalPower(self):
        sum1 = 0
        for i in self.components:
            sum1 += i.power_usage
        return sum1
    
    def diagnosting_all(self):
        pass
            
            
computer = Computer()
computer.addComponents(CPU)
computer.addComponents(GPU)
computer.addComponents(RAM)
computer.addComponents(Storage)


print(computer.totalPower())
        
        
    
        
        
        
        