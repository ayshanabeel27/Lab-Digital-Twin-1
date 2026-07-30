from twin_state import ComputerTwin
from simulator import (
    simulate_lab,
    simulate_failure,
    check_lab_capacity
)
from alerts import (
    check_temperature,
    check_cpu,
    check_ram
)

pc1 = ComputerTwin(1, 95, 60, 80)

pc2 = ComputerTwin(2, 20, 30, 35)

pc3 = ComputerTwin(3, 90, 95, 75)

computers = [pc1, pc2, pc3]

simulate_lab(computers)
simulate_failure(computers, [2])

check_lab_capacity(

    total_computers=40,

    failed_computers=10,

    students=40

)
print("\n----- Alerts -----")

for pc in computers:

    temp_alert = check_temperature(pc)

    cpu_alert = check_cpu(pc)

    ram_alert = check_ram(pc)

    if temp_alert:

        print(temp_alert)

    if cpu_alert:

        print(cpu_alert)

    if ram_alert:

        print(ram_alert)
