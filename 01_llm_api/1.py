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
	tools=[get_weather,add],
	system_prompt="""你负责从论文材料中提取信息。
					要求：
					1. 只依据提供的材料，不使用外部知识补充事实。
					2. 提取标题、研究方法和主要贡献。
					3. 研究方法说明采用了什么技术，以及如何组合使用。
					4. 主要贡献逐条列出，保留材料中的关键实验数字。
					5. 缺少的信息写“材料未提供”，不要猜测。
					6. 使用以下格式：

					标题：
					方法：
					贡献：
					- ..."""
)

result=agent.invoke(
	{"messages":[
		{"role":"user","content":"""请提取以下论文材料中的信息：
								<paper>
								本文针对课程问答中语言模型容易生成无依据回答的问题，
								提出一种结合课程文档检索与答案生成的方法。
								系统先使用向量检索查找相关段落，再将段落提供给语言模型生成答案，
								并要求答案标注来源。
								在包含200道问题的内部测试集上，相比直接使用语言模型，
								该方法将有依据回答的比例从65%提高到82%。
								本文还构建了一套用于课程问答的评估数据集。
								</paper>"""}]}
)

for message in result["messages"]:
	print(message.pretty_print())