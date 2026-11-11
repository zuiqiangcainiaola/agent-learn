from pydantic import BaseModel,ConfigDict,ValidationError

class PaperInfo(BaseModel):
	model_config=ConfigDict(extra="forbid")

	title:str
	method:str
	contribution:list[str]

paper=PaperInfo(
	title="示例论文",
	method="使用注意力机制",
	contribution=["改进信息提取效果","减少计算量"]
)

print(paper.title)
print(paper.model_dump())             # Python 字典
print(paper.model_dump_json(indent=2))  # JSON 字符串