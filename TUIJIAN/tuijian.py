from efficient_apriori import apriori
from pageinfo import *
# for i in range(1059, 1270):

transactions = Aplus1.select(Aplus1.aplus)
# transactions = Aplus.select(Aplus.aplus).limit(1059)
output = [tuple(eval(e[0])) for e in transactions.tuples()]
# print(output)
# print(output[i-1])
# print(i)

# eval["aplus-launchpad-company-logo", "aplus-3p-module-b", "aplus-module-4", "aplus-module-8"]
itemsets, rules = apriori(output, min_support=0.01, min_confidence=0.2)
# print(itemsets)
# Print out every rule with 2 items on the left hand side,
# 1 item on the right hand side, sorted by lift
rules_rhs = filter(lambda rule: len(rule.lhs) == 1 and len(rule.rhs) == 1, rules)

class tuijian(Model):

   name1=CharField()
   name2=CharField()
   conf=CharField()
   supp=CharField()
   lift=CharField()
   conv=CharField()

   class Meta:
      database=db
      db_table='tuijian'

tuijian.create_table()

for rule in sorted(rules_rhs, key=lambda rule: rule.lift):
    # print(str(rule))  # Prints the rule and its confidence, support, lift, ...
    i = str(rule)
    i = i.replace("} -> {", ",")
    i = i.replace("} (", ",")
    i = i.replace("{", "")
    i = i.replace(")", "")
    i = i.replace("conf:", "")
    i = i.replace("supp:", "")
    i = i.replace("lift:", "")
    i = i.replace("conv:", "")
    i = i.split(',')
    print(i)

    object = tuijian(
        name1=i[0],
        name2=i[1],
        conf=i[2],
        supp=i[3],
        lift=i[4],
        conv=i[5]
    )
    object.save()
