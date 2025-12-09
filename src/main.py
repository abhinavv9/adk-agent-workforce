import google
import google.generativeai as genai

from src.agent import GreetingAgent

def create_agent_workforce():
    """Creates and returns a simple agent workforce."""
    # Configure the generative AI model
    genai.configure(api_key="YOUR_API_KEY") # Replace with your actual API key

    # Initialize the GreetingAgent
    greeting_agent = GreetingAgent()

    # Define the tools (capabilities) for the workforce
    tools = [
        {
            "function": {
                "name": "greet",
                "description": "Greets the user by name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string", "description": "The name of the person to greet."}
                    },
                    "required": ["name"],
                },
            }
        }
    ]

    # Create the agent workforce with the defined tools and agents
    workforce = genai.GenerativeAgent(
        tools=tools,
        functions={"greet": greeting_agent.greet},
        name="GreetingWorkforce",
        description="A workforce that can greet users.",
    )
    return workforce

if __name__ == "__main__":
    workforce = create_agent_workforce()
    response = workforce.invoke("Greet John Doe.")
    print(response.text)
