import os 
import asyncio
from pydantic_ai import Agent
from pydantic_ai.mcp import MCPServerStdio


mcp_fetc_server = MCPServerStdio(
    command = "python",
    args = ["-m","mcp_server_fetch"]
)
os.environ["GROQ_API_KEY"]="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"

agent = Agent(
    model="groq:llama-3.3-70b-versatile",
    mcp_server=[mcp_fetc_server]
)

async def main():
    async with agent.run_mcp_servers():
        result = await agent.run("extract the content and summarize it:https://indiankanoon.org/doc/666119/")
        output = result.output
        return output
    
if __name__ == "__main__":
    output = asyncio.run(main())
    print(output)