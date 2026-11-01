def create_agent(name, role):
    return {
        "name": name,
        "role": role,
        "argument": []
    }

def add_argument(agent, argument):
    agent["argument"].append(argument)

def display_debate(agent1, agent2):
    for round_number, (first,second) in enumerate(zip(agent1['argument'], agent2['argument']), start=1):
        print(f"\n Round: {round_number}")
        print(f"{agent1['name']} - {agent1['role']}: {argument1}")
        print(f"{agent2['name']} - {agent2['role']}: {argument2}")

agent1 = create_agent("AGENT 1", "SUPPORT")
agent2 = create_agent("AGENT 2", "OPPOSE")

agent1_arguments = ["AI improves efficiency of Human beings.",
                    "AI solves complex problems.",
                    "AI can assist people in learning new skills."]

agent2_arguments = ["Overdependence on AI can weaken thinking ability.",
                    "AI can sometimes produce incorrect or misleading results.",
                    "Excess use of AI can make a person lazy."]

while True:
    topic = input("Enter the Topic name:").strip() #Eg: Does AI improve Human Productivity ?
    if topic:
        break
    else:
        print("Enter a valid topic name!")

max_rounds = min(len(agent1_arguments), len(agent2_arguments))
while True:
    try:
        rounds = int(input("Enter the number of Rounds:"))

        if 0 < rounds <= max_rounds:
            break
        else:
            print(f"Please enter between 1 and {max_rounds} rounds!")

    except ValueError:
        print("Please enter a valid whole number!")
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
