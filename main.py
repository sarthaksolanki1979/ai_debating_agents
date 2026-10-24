def ai_debate_agent(agent_number):
    if agent_number == 1:
        return "Support"    
    else:
        return "Oppose"

agent1_role = ai_debate_agent(1)
agent2_role = ai_debate_agent(2)

topic = input("Enter the debate topic:")
print("*" * 40)
print(f"    THE DEBATE TOPIC IS: {topic}")
print(f"Agent 1: {agent1_role}")
print(f"Agent 2: {agent2_role}")