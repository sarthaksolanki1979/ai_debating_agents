import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found. Please check your .env file.")

client = Groq(api_key=api_key)

MODEL = "openai/gpt-oss-20b"

def generate_response(prompt):
    responses = client.chat.completions.create(
        model=MODEL,
        messages= [
            {
                'role': 'user',
                'content': prompt
            }
        ]
    )

    print("DEBUG RESPONSE:", repr(responses.choices[0].message.content))
    return responses.choices[0].message.content

def generate_agent_argument(agent, topic, opposing_argument=None):
    prompt = create_prompt(agent, topic, opposing_argument)

    print(f"\nGenerating argument for {agent['name']}...")

    argument = generate_response(prompt)

    add_argument(agent, argument)

    return argument

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

Build a strong argument defending the topic.
Use logical reasoning and challenge the opposing position where relevant.

You must consistently defend the topic's central claim.
Never switch sides or defend the opposing position."""

    elif agent['role'] == "OPPOSE":
        prompt = f"""You are a debating agent named {agent['name']}.
Your role is to OPPOSE the topic: {topic}.

Build a strong argument challenging the topic.
Defend the alternative position using logical reasoning.

You must consistently argue against the topic's central claim.
Never switch sides or defend the supporting position."""

    else:
        raise ValueError("Invalid agent role!")

    prompt += """

Maintain your assigned position throughout the entire debate.

Keep your argument between 80 and 100 words.
Use simple, direct language.
Focus on 2 or 3 strong points.
Avoid lengthy explanations, repetition, tables, and unnecessary headings.
Do not invent statistics, research findings, or citations.
Use factual claims only when you can state them reliably."""

    if opposing_argument is not None:
        prompt += f"""

The opposing agent presented this argument:
{opposing_argument}

Your task:
1. Identify the opponent's most important claims.
2. Challenge their reasoning with relevant counterarguments.
3. Defend your assigned position using logical explanations.
4. Avoid repeating your previous arguments.
5. Keep your rebuttal focused on the strongest opposing claims."""

    return prompt


def add_argument(agent, argument):
    agent["argument"].append(argument)

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

    opposing_argument1 = None
    opposing_argument2 = None

    if round_number > 1:
        opposing_argument1 = agent2['argument'][round_number - 2]
        opposing_argument2 = agent1['argument'][round_number - 2]

    generate_agent_argument(agent1, topic, opposing_argument1)

    generate_agent_argument(agent2, topic, opposing_argument2)


print("\n" + "=" * 55)
print("                 AI Debating Agents")
print("=" * 55)
print(f"Debate Topic: {topic}")
print(f"Number of Rounds: {rounds}")

display_debate(agent1, agent2)
debate_summary(topic, rounds, agent1, agent2)

print("=" * 55)
