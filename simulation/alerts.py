def check_temperature(pc):

    if pc.temperature > 70:

        return (
            f"🚨 ALERT: "
            f"Computer {pc.id} is overheating!"
        )

    return None


def check_cpu(pc):

    if pc.cpu_usage > 85:

        return (

            f"🚨 ALERT: "
            f"Computer {pc.id} CPU usage is too high!"

        )

    return None


def check_ram(pc):

    if pc.ram_usage > 90:

        return (

            f"🚨 ALERT: "
            f"Computer {pc.id} RAM usage is too high!"

        )

    return None