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

cases = [
    # 缺少 method
    {"title": "论文 A", "contribution": ["贡献一"]},

    # contribution 类型错误
    {"title": "论文 A", "method": "方法 A",
     "contribution": "贡献一"},

    # 多了未定义的字段
    {"title": "论文 A", "method": "方法 A",
     "contribution": ["贡献一"], "score": 100},
]

for data in cases:
    try:
        result = PaperInfo.model_validate(data)
        print("通过：", result)
    except ValidationError as e:
        print("校验失败：", e.errors())