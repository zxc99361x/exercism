def is_criticality_balanced(temperature, neutrons_emitted):
    return temperature <800 and neutrons_emitted >500 and (temperature*neutrons_emitted) <500000
def reactor_efficiency(voltage, current, theoretical_max_power):
    if (voltage*current)/theoretical_max_power*100 >=80:
        return 'green'
    elif (voltage*current)/theoretical_max_power*100 <80 and (voltage*current)/theoretical_max_power*100 >=60:
        return 'orange'
    elif (voltage*current)/theoretical_max_power*100 <60 and (voltage*current)/theoretical_max_power*100 >=30:
        return 'red'
    elif (voltage*current)/theoretical_max_power*100 <30:
        return 'black'
def fail_safe(temperature, neutrons_produced_per_second, threshold):
    reactor_output = temperature * neutrons_produced_per_second

    if reactor_output < 0.9 * threshold:
        return 'LOW'
    elif 0.9 * threshold <= reactor_output <= 1.1 * threshold:
        return 'NORMAL'
    else:
        return 'DANGER'
