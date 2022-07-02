name = "Steve"
company = "Apple"
post = "CEO"

st = "Good morning {1} It's your time to go to office. You work at {2}. You are {0}".format(name, company, post)
print(st)

st2 = f"Good morning {name}. It's your time to go to office. You work at {company} as a {post}"
print(st2)