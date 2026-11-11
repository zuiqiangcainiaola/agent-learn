from langchain.agents import create_agent
from langchain_openai import ChatOpenAI


model = ChatOpenAI(
    api_key="",
    base_url="https://api.deepseek.com",
    model="deepseek-flash",
    extra_body={"thinking": {"type": "disabled"}},
)

def get_weather(city: str) -> str:
    """获取指定城市的天气。"""
    return f"{city} 总是阳光明媚！"

agent = create_agent(
    model=model,
    tools=[get_weather],
    system_prompt="你是一名乐于助人的助手",
)

result = agent.invoke(
    {"messages": [{"role": "user", "content": "旧金山的天气怎么样？"}]}
)
print(result["messages"][-1].content_blocks)
