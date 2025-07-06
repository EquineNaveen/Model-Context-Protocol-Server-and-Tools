import asyncio
import os
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

async def main():
    client = MultiServerMCPClient(
        {
            "math":{
                "command":"python",
                "args":["mathserver.py"],
                "transport":"stdio"
            }
        })

    os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')

    tools= await client.get_tools()
    model=ChatGroq(model="qwen-qwq-32b")
    agent=create_react_agent(model=model, tools=tools)
    response=await agent.ainvoke(
        {"messages": [{"role": "user", "content": "solve (88*(2+3))/5"}]},
    )
    print(response['messages'][-1].content)

asyncio.run(main())