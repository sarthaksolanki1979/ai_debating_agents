def create_agent(name, role):
    return {
        "name": name,
        "role": role,
        "argument": []
    }

def add_argument(agent, argument):
    agent["argument"].append(argument)

def display_agent(agent):
    print(f"{agent['name']} - {agent['role']}")

    for round_number, argument in enumerate(agent["argument"], start=1):
        print(f"Round {round_number}: {argument}")

topic = input("Enter Topic Name:")
rounds = int(input("Enter the number of Rounds:"))

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

display_agent(agent1)
display_agent(agent2)

print("=" * 50)