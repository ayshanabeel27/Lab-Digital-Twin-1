def calculate_health(cpu, ram, temp):

    score = 100

    score -= cpu * 0.3
    score -= ram * 0.2
    score -= temp * 0.5

    return max(score, 0)
    print(calculate_health(20,30,40))