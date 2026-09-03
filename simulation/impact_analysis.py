def analyze_lab(total_computers, critical_computers, students):

    available = total_computers - critical_computers

    print("\n----- Lab Impact Analysis -----")

    print("Total computers:", total_computers)
    print("Critical computers:", critical_computers)
    print("Available computers:", available)
    print("Students:", students)

    if available >= students:

        print("✅ The lab can handle all students.")

    else:

        affected = students - available

        print(
            f"❌ {affected} students will be affected."
        )