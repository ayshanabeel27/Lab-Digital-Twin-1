class ComputerTwin:

    def __init__(self, id, cpu_usage, ram_usage, temperature):

        self.id = id
        self.cpu_usage = cpu_usage
        self.ram_usage = ram_usage
        self.temperature = temperature

    def display_info(self):

        print("Computer ID:", self.id)
        print("CPU Usage:", self.cpu_usage, "%")
        print("RAM Usage:", self.ram_usage, "%")
        print("Temperature:", self.temperature, "°C")
    def calculate_health(self):

        health = 100

        health -= self.cpu_usage * 0.3
        health -= self.ram_usage * 0.2
        health -= self.temperature * 0.5

        return max(health, 0)
    
    def get_status(self):

        health = self.calculate_health()

        if health >= 70:
            return "Healthy"

        elif health >= 40:
            return "Warning"

        else:
            return "Critical"