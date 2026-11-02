def create_agent(name, role):
    return {
        "name": name,
        "role": role,
        "argument": []
    }

def add_argument(agent, argument):
    agent["argument"].append(argument)

def collect_arguments(agent, rounds):
    for round_number in range(1, rounds + 1):
        argument = input(
            f"Enter argument {round_number} for {agent['name']} ({agent['role']}):"
        )

        add_argument(agent, argument)

def display_debate(agent1, agent2):
    for round_number, (first,second) in enumerate(zip(agent1['argument'], agent2['argument']), start=1):
        print(f"\n Round: {round_number}")
        print(f"{agent1['name']} - {agent1['role']}: {first}")
        print(f"{agent2['name']} - {agent2['role']}: {second}")

agent1 = create_agent("AGENT 1", "SUPPORT")
agent2 = create_agent("AGENT 2", "OPPOSE")

while True:
    topic = input("Enter the Topic name:").strip() #Eg: Does AI improve Human Productivity ?
    if topic:
        break
    else:
        print("Enter a valid topic name!")

while True:
    try:
        rounds = int(input("Enter the number of Rounds:"))

        if 0 < rounds <= 3:
            break
        else:
            print(f"Please enter between 1 and 3 rounds!")

    except ValueError:
        print("Please enter a valid whole number!")

collect_arguments(agent1, rounds)
collect_arguments(agent2, rounds)


print("\n" + "=" * 50)
print("      AI Debating Agents")
print("=" * 50)
print(f"Topic Name: {topic}")
print(f"Number of Rounds: {rounds}")

display_debate(agent1, agent2)

print("=" * 50)
