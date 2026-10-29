def create_agent(name, role):
    return {
        "name": name,
        "role": role,
        "argument": []
    }

def add_argument(agent, argument):
    agent["argument"].append(argument)

def display_debate(agent1, agent2):
    for round_number, argument1 in enumerate(agent1['argument'], start=1):
        argument2 = agent2['argument'][round_number - 1]

        print(f"\n Round: {round_number}")
        print(f"{agent1['name']} - {agent1['role']}: {argument1}")
        print(f"{agent2['name']} - {agent2['role']}: {argument2}")

topic = input("Enter Topic Name:") #Eg: Does AI improve Human productivity ?

while True:
    try:
        rounds = int(input("Enter the number of Rounds:"))
        if rounds > 0:
            break
        else:
            print("Please enter at least 1 round!")
    except ValueError:
        print("Please enter a valid whole number!")

agent1 = create_agent("AGENT 1", "SUPPORT")
agent2 = create_agent("AGENT 2", "OPPOSE")

agent1_arguments = ["AI improves efficiency of Human beings.",
                    "AI solves complex problems.",
                    "AI can assist people in learning new skills."]

agent2_arguments = ["Overdependence on AI can weaken thinking ability.",
                    "AI can sometimes produce incorrect or misleading results.",
                    "Excess use of AI can make a person lazy."]

for round_number in range(1, rounds + 1):
    argument1 = agent1_arguments[round_number - 1]
    argument2 = agent2_arguments[round_number - 1]

    add_argument(agent1, argument1)
    add_argument(agent2, argument2)

print("\n" + "=" * 50)
print("      AI Debating Agents")
print("=" * 50)
print(f"Topic Name: {topic}")
print(f"Number of Rounds: {rounds}")

display_debate(agent1, agent2)

print("=" * 50)