str1="[a,b,c]"
print(type(str1))
response="[a,b,c]"
res=response.strip('[')
res=res.strip(']')
res=res.split(',')
print(res)
# <class 'str'>
# ['a', 'b', 'c']
# strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。
# split()方法用于通过指定分隔符对字符串进行切片，切片后生成列表。

a = "abcd"
a = [a,]
print(a)
# 输出为['abcd']


