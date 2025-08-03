#Validate that the domain is not the banned list
domain ="gmail.com"
banned_domains = ["spam.com","fake.org","bot.net"]
print(domain not in banned_domains)