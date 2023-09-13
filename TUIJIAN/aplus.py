from efficient_apriori import apriori
from pageinfo import *
# for i in range(1059, 1270):

c = Aplus.select(Aplus.aplus) # 用确实可以用，但这种方法更适合选中多个列，如果只想使用单列只使用Aplus.aplus即可
# transactions = Aplus.select(Aplus.aplus).limit(1059)
output = [tuple(eval(e[0])) for e in c.tuples()] # 这种方法挺奇怪的 好像只用这种方式去获取其中的数据
# print(output[i-1])
# print(i)

# eval["aplus-launchpad-company-logo", "aplus-3p-module-b", "aplus-module-4", "aplus-module-8"]
itemsets, rules = apriori(output, min_support=0.3, min_confidence=0.3)

# Print out every rule with 2 items on the left hand side,
# 1 item on the right hand side, sorted by lift
rules_rhs = filter(lambda rule: len(rule.lhs) == 1 and len(rule.rhs) == 1, rules)
for rule in sorted(rules_rhs, key=lambda rule: rule.lift):
    print(rule)  # Prints the rule and its confidence, support, lift, ...
    print(type(rule))