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

agent1 = create_agent("AGENT 1", "SUPPORT")
agent2 = create_agent("AGENT 2", "OPPOSE")

add_argument(agent1, "AI proceeds to help mankind to improve their work and efficiency.")
add_argument(agent2, "Too much dependence on AI can weaken thinking and make humans over-dependent.")

print("\n" + "=" * 50)
print("      AI Debating Agents")
print("=" * 50)
print(f"Topic Name: {topic}")

display_agent(agent1)
display_agent(agent2)

print("=" * 50)