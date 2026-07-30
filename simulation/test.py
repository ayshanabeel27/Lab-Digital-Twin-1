from impact_simulator import simulate_impact  
from impact_simulator import get_priority

simulate_impact(

    total_computers=40,

    predicted_failed=8,

    students=38

)

print(get_priority(8))