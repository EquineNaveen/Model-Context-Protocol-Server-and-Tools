import asyncio
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from mcp_use import MCPAgent,MCPClient

async def run_memory_chat():
    """Run a chat using mcpagent's built in conversation history"""
    load_dotenv()
    os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')  
    config_file="mcpconfig.json"
    print(f"Using config file: {config_file}")
    client = MCPClient.from_config_file(config_file)
    llm = ChatGroq(model="qwen-qwq-32b")
    agent = MCPAgent(llm=llm, client=client,max_steps=15,memory_enabled=True)
    print("Starting chat with memory enabled...")
    try:
        while True:
            user_input = input("You: ")
            if user_input.lower() in ["exit", "quit"]:
                print("Exiting chat.")
                break

            if user_input.lower()=="clear":
                agent.clear_conversation_history()
                print("Conversation history cleared.")
                continue
            print("Assistant:",end="",flush=True)

            try:
                response=await agent.run(user_input)
                print(response)
            except Exception as e:
                print(f"Error during chat: {e}")

    finally:
        if client and client.sessions:
            await client.close_all_sessions()
if __name__ == "__main__":  
    asyncio.run(run_memory_chat())