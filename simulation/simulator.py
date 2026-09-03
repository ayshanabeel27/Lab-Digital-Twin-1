from twin_state import ComputerTwin
from twin_state import ComputerTwin



def simulate_lab(computers):

    total_health = 0

    for pc in computers:

        health = pc.calculate_health()

        total_health += health

        print(
            f"Computer {pc.id}: "
            f"Health = {health}, "
            f"Status = {pc.get_status()}"
        )

    average_health = total_health / len(computers)

    print("\nAverage Health:", average_health)

def simulate_failure(computers, failed_ids):

    print("\n----- Failure Simulation -----")

    for pc in computers:

        if pc.id in failed_ids:

            print(f"Computer {pc.id}: FAILED ❌")

        else:

            print(
                f"Computer {pc.id}: RUNNING ✅ "
                f"({pc.get_status()})"
            )
        count = 0
    for pc in computers:
        if pc.id in failed_ids:
            count += 1

    print(f"Total computers = {len(computers)} \n"
          f"Failed computers = {count} \n"    
          f"working computers ={len(computers)-count}\n"    
    )

def check_lab_capacity(total_computers, failed_computers, students):

    working_computers = total_computers - failed_computers

    print("\n----- Lab Capacity Check -----")

    print("Total computers:", total_computers)

    print("Failed computers:", failed_computers)

    print("Working computers:", working_computers)

    print("Students:", students)

    if students <= working_computers:

        print("The lab can handle all students ✅")

    else:

        extra_students = students - working_computers

        print(
            f"The lab cannot handle all students ❌"
        )

        print(
            f"{extra_students} students do not have computers."
        )


