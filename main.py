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

for round_number in range(rounds):
    add_argument(
        agent1, "AI can improve productivity and help people solve complex problems."
    )

    add_argument(
        agent2, "Overdependence on AI can weaken independent thinking and judgment."
    )


print("\n" + "=" * 50)
print("      AI Debating Agents")
print("=" * 50)
print(f"Topic Name: {topic}")
print(f"Number of Rounds: {rounds}")

display_debate(agent1, agent2)

print("=" * 50)