def create_agent(name, role):
    return {
        "name": name,
        "role": role,
        "argument": []
    }

def create_prompt(agent, topic, opposing_argument=None):
    if agent['role'] == "SUPPORT":
        prompt = f"""You are a debating agent named {agent['name']}.
Your role is to SUPPORT the topic: {topic}.
Generate strong arguments defending the topic and challenging the opposing position."""

    elif agent['role'] == 'OPPOSE':
        prompt = f"""You are a debating agent named {agent['name']}.
Your role is to OPPOSE the topic: {topic}.
Generate strong arguments challenging the topic and defending the opposing position."""

    else:
        raise ValueError("Invalid agent role!")

    if opposing_argument is not None:
        prompt += f"""

The opposing agent presented this argument:
{opposing_argument}

Respond to this argument while defending your position."""

    return prompt


def add_argument(agent, argument):
    agent["argument"].append(argument)

def collect_argument(agent, round_number):
    while True:
        argument = input(
            f"Enter argument {round_number} for {agent['name']} ({agent['role']}): "
        ).strip()

        if argument:
            break
        else:
            print("Argument cannot be empty. Please try again!")

    add_argument(agent, argument)

def display_debate(agent1, agent2):
    for round_number, (first, second) in enumerate(zip(agent1['argument'], agent2['argument']), start=1):
        print(f"\n Round: {round_number}")
        print(f"{agent1['name']} - {agent1['role']}: {first}")
        print(f"{agent2['name']} - {agent2['role']}: {second}")

    print(f"\nTotal debate rounds: {len(agent1['argument'])}")

def debate_summary(topic, rounds, agent1, agent2):
    print("=" * 55)
    print("                  DEBATE SUMMARY")
    print(f"Topic name: {topic}")
    print(f"Number of rounds: {rounds}")
    print(f"Total arguments: {len(agent1['argument']) + len(agent2['argument'])}")
    print(f"{agent1['name']} arguments: {len(agent1['argument'])}")
    print(f"{agent2['name']} arguments: {len(agent2['argument'])}")

def get_topic():
    while True:
        topic = input("Enter the topic name: ").strip()

        if topic:
            return topic

        print("Enter a valid topic name!")

agent1 = create_agent("AGENT 1", "SUPPORT")
agent2 = create_agent("AGENT 2", "OPPOSE")

topic = get_topic()

def get_rounds():
    while True:
        try:
            rounds = int(input("Enter the number of rounds: "))

            if 0 < rounds <= 3:
                return rounds

            print("Please enter between 1 and 3 rounds!")

        except ValueError:
            print("Please enter a valid whole number!")

rounds = get_rounds()

for round_number in range(1, rounds + 1):
    if round_number == 1:
        collect_argument(agent1, round_number)
        collect_argument(agent2, round_number)

    else:
        opposing_argument1 = agent2['argument'][round_number - 2]
        prompt1 = create_prompt(agent1, topic, opposing_argument1)
        print(f"\n--- {agent1['name']} PROMPT---")
        print(prompt1)
        collect_argument(agent1, round_number)

        opposing_argument2 = agent1['argument'][round_number - 2]
        prompt2 = create_prompt(agent2, topic, opposing_argument2)
        print(f"\n--- {agent2['name']} PROMPT---")
        print(prompt2)
        collect_argument(agent2, round_number)


print("\n" + "=" * 55)
print("                 AI Debating Agents")
print("=" * 55)
print(f"Debate Topic: {topic}")
print(f"Number of Rounds: {rounds}")

display_debate(agent1, agent2)
debate_summary(topic, rounds, agent1, agent2)

print("=" * 55)
