# 并未跑通 gpt那边没响应 也还没创建txt文件

# 引入openai的工具包
import openai
# 引入浏览器的工具包
import webbrowser
# 引入画红线处理错误单词的工具包
from redlines import Redlines
# 引入可以让请求暂停20秒的工具包
import time

# OpenAI API key
openai.api_key = 'sk-b95toDwHIXmLM51Vvt111DT3BlbkFJ7pSNdz0jDarg3C1GiP4V'


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


# 读取10篇英语作文
with open('学生英语作文.txt', 'r') as f:
    essays = f.readlines()

# 循环获取 批量修改每篇英语作文
for essay in essays:
    prompt = f"""
            我是一个英语老师，有个学生天天写错别字，真是神烦，教务处还要求我用红笔修改以下作业，
            可是我根本懒得改，请帮我批改以下这个学生的英语作业。学生的英语作业是使用三个单引号括起来的部分：
            '''
            {essay}
            '''
            """

    # 请求gpt
    correct_sentence = gpt(prompt)

    after_red_line = Redlines(essay, correct_sentence)

    # 将Markdown格式的文本转换为HTML格式
    html = after_red_line.output_markdown

    # 将HTML页面写入文件
    with open('output.html', 'w') as f:
        f.write(html)

    # 在浏览器中打开HTML页面
    webbrowser.open('output.html')

    # 让程序暂停 20 秒 以免调用过于频繁导致报警
    time.sleep(20)