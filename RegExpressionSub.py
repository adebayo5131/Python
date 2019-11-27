import re

subRegex = re.compile(r'Agent (\w)\w+')
Regex = re.compile(r'Agent (\w)\w+')
po = Regex.findall('Agent Adebayo and Agent Eddie are on a mission')
print(po)

mo = subRegex.sub(r'Agent \1*******', 'Agent Adebayo and Agent Eddie are on a mission')
print(mo)
