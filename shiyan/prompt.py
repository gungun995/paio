# 引入openai的包
import openai
# 下面三行是找到的报错解决方案 但还是不行 好像是配额问题 注册三个月后使用api就要付费了
import os
os.environ["http_proxy"] = "http://localhost:7890"
os.environ["https_proxy"] = "http://localhost:7890"

# OpenAI API key
openai.api_key = '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'


# 定义GPT API
def gpt(prompt):
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role': 'user',
             'content': prompt}
        ],
        temperature=0,
    )
    print(response.choices[0].message.content)
    return response.choices[0].message.content

#使用GPT API
gpt("你好请问你可以帮我修改英语试卷吗？")