# bounce.py
#
# Exercise 1.5

top_height = 100
backup_height = 3/5
total_bounces = 10
start_bounce=0

while start_bounce < total_bounces:
	start_bounce += 1
	top_height = top_height*backup_height
	print(start_bounce, round(top_height,4))
