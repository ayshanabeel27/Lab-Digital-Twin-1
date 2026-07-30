def simulate_impact(total_computers, predicted_failed, students):

    working_computers = total_computers - predicted_failed

    print("\n----- Impact Analysis -----")

    print("Total computers:", total_computers)
    print("Predicted failures:", predicted_failed)
    print("Working computers:", working_computers)
    print("Students:", students)

    if working_computers >= students:

        print("✅ Lab can still handle all students")

    else:

        affected_students = students - working_computers

        print(
            f"❌ {affected_students} students will be affected"
        )

def get_priority(predicted_failed):

    if predicted_failed <= 2:

        return "Low Priority"

    elif predicted_failed <= 5:

        return "Medium Priority"

    else:

        return "High Priority"