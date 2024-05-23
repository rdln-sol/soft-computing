import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt


temperature = ctrl.Antecedent(np.arange(0, 41, 1), "temperature")
time_of_day = ctrl.Antecedent(np.arange(0, 24, 1), "time_of_day")
occupancy = ctrl.Antecedent(np.arange(0, 51, 1), "occupancy")
ac_status = ctrl.Consequent(np.arange(0, 4, 1), "ac_status")


temperature["low"] = fuzz.trimf(temperature.universe, [0, 0, 20])
temperature["medium"] = fuzz.trimf(temperature.universe, [15, 25, 30])
temperature["high"] = fuzz.trimf(temperature.universe, [25, 40, 40])

time_of_day["morning"] = fuzz.trimf(time_of_day.universe, [6, 6, 12])
time_of_day["afternoon"] = fuzz.trimf(time_of_day.universe, [12, 12, 18])
time_of_day["evening"] = fuzz.trimf(time_of_day.universe, [18, 18, 24])

occupancy["low"] = fuzz.trimf(occupancy.universe, [0, 0, 10])
occupancy["medium"] = fuzz.trimf(occupancy.universe, [5, 15, 30])
occupancy["high"] = fuzz.trimf(occupancy.universe, [20, 50, 50])

ac_status["off"] = fuzz.trimf(ac_status.universe, [0, 0, 1])
ac_status["low"] = fuzz.trimf(ac_status.universe, [0, 1, 2])
ac_status["medium"] = fuzz.trimf(ac_status.universe, [1, 2, 3])
ac_status["high"] = fuzz.trimf(ac_status.universe, [2, 3, 3])


rule1 = ctrl.Rule(
    temperature["high"] & time_of_day["morning"] & occupancy["high"], ac_status["high"]
)
rule2 = ctrl.Rule(
    temperature["medium"] & time_of_day["afternoon"] & occupancy["medium"],
    ac_status["medium"],
)
rule3 = ctrl.Rule(
    temperature["low"] & time_of_day["evening"] & occupancy["low"], ac_status["off"]
)
rule4 = ctrl.Rule(
    temperature["high"] & time_of_day["afternoon"] & occupancy["low"],
    ac_status["medium"],
)
rule5 = ctrl.Rule(
    temperature["medium"] & time_of_day["morning"] & occupancy["high"], ac_status["low"]
)
rule6 = ctrl.Rule(
    temperature["low"] & time_of_day["afternoon"] & occupancy["medium"],
    ac_status["low"],
)
rule7 = ctrl.Rule(
    temperature["high"] & time_of_day["evening"] & occupancy["low"], ac_status["off"]
)
rule8 = ctrl.Rule(
    temperature["medium"] & time_of_day["evening"] & occupancy["high"],
    ac_status["high"],
)
rule9 = ctrl.Rule(
    temperature["low"] & time_of_day["morning"] & occupancy["low"], ac_status["off"]
)
rule10 = ctrl.Rule(
    temperature["medium"] & time_of_day["morning"] & occupancy["low"], ac_status["off"]
)
rule11 = ctrl.Rule(
    temperature["high"] & time_of_day["afternoon"] & occupancy["medium"],
    ac_status["high"],
)
rule12 = ctrl.Rule(
    temperature["medium"] & time_of_day["evening"] & occupancy["medium"],
    ac_status["high"],
)
rule13 = ctrl.Rule(
    temperature["low"] & time_of_day["morning"] & occupancy["high"], ac_status["medium"]
)
rule14 = ctrl.Rule(
    temperature["medium"] & time_of_day["afternoon"] & occupancy["high"],
    ac_status["high"],
)
rule15 = ctrl.Rule(
    temperature["high"] & time_of_day["evening"] & occupancy["high"], ac_status["high"]
)
rule16 = ctrl.Rule(
    temperature["low"] & time_of_day["afternoon"] & occupancy["high"],
    ac_status["medium"],
)
rule17 = ctrl.Rule(
    temperature["medium"] & time_of_day["morning"] & occupancy["medium"],
    ac_status["low"],
)
rule18 = ctrl.Rule(
    temperature["high"] & time_of_day["evening"] & occupancy["medium"],
    ac_status["high"],
)
rule19 = ctrl.Rule(
    temperature["low"] & time_of_day["afternoon"] & occupancy["low"], ac_status["off"]
)
rule20 = ctrl.Rule(
    temperature["medium"] & time_of_day["evening"] & occupancy["low"], ac_status["off"]
)
rule21 = ctrl.Rule(
    temperature["low"] & time_of_day["morning"] & occupancy["medium"], ac_status["low"]
)
rule22 = ctrl.Rule(
    temperature["high"] & time_of_day["morning"] & occupancy["low"], ac_status["low"]
)
rule23 = ctrl.Rule(
    temperature["medium"] & time_of_day["morning"] & occupancy["high"], ac_status["low"]
)
rule24 = ctrl.Rule(
    temperature["low"] & time_of_day["afternoon"] & occupancy["low"], ac_status["off"]
)
rule25 = ctrl.Rule(
    temperature["medium"] & time_of_day["afternoon"] & occupancy["low"],
    ac_status["low"],
)
rule26 = ctrl.Rule(
    temperature["high"] & time_of_day["afternoon"] & occupancy["high"],
    ac_status["high"],
)
rule27 = ctrl.Rule(
    temperature["medium"] & time_of_day["evening"] & occupancy["low"], ac_status["off"]
)


ac_ctrl = ctrl.ControlSystem(
    [
        rule1,
        rule2,
        rule3,
        rule4,
        rule5,
        rule6,
        rule7,
        rule8,
        rule9,
        rule10,
        rule11,
        rule12,
        rule13,
        rule14,
        rule15,
        rule16,
        rule17,
        rule18,
        rule19,
        rule20,
        rule21,
        rule22,
        rule23,
        rule24,
        rule25,
        rule26,
        rule27,
    ]
)
ac_simulation = ctrl.ControlSystemSimulation(ac_ctrl)

ac_simulation.input["temperature"] = int(
    input("What is the Temperature ? [ 0 , 41 ] : ")
)
ac_simulation.input["time_of_day"] = int(
    input("What is the Time of the day? ? [ 24H ] : ")
)
ac_simulation.input["occupancy"] = int(
    input("How many people are currently present in this class? [ 0  , 51 ] :  ")
)

ac_simulation.compute()
print(ac_simulation.output["ac_status"])
output_status = ac_simulation.output["ac_status"]


print("Fuzzy Output (AC Status):", output_status)


temperature.view()
time_of_day.view()
occupancy.view()
ac_status.view(sim=ac_simulation)

plt.show()
