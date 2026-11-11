import sys
from pathlib import Path
config_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(config_dir))

from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from pydantic import SecretStr
from config_local import DEEPSEEK_API_KEY

model=ChatOpenAI(
	api_key=SecretStr(DEEPSEEK_API_KEY),
	base_url="https://api.deepseek.com",
	model="deepseek-flash",
	extra_body={"thinking":{"type":"disabled"}}
)

def get_weather(city:str) -> str:
	"""获取指定城市的天气"""
	return f"{city}天气很好"

def add(a:int,b:int) -> int:
	"""计算两个整数相加"""
	return a+b

agent=create_agent(
	model=model,
	tools=[get_weather],
	system_prompt="你是一个乐于助人的天气助手"
)

result=agent.invoke(
	{"messages":[
		{"role":"system","content":"你也是一个乐于助人的学习助手"},
		{"role":"user","content":"重庆天气怎么样"},
		{"role":"assistant","content":"重庆今天的天气很好哦～😊 适合出门活动，不过具体温度和是否需要防晒、带伞，建议你再看看实时天气详情。需要我帮你查其他城市或更详细的信息吗？"},
		{"role":"user","content":"我刚刚问了你什么"}]}
)

print(result["messages"])