unconfirmed = ["alice", "bob", "charlie"]
confirmed = []

for _ in unconfirmed:
	confirmed.append(_)
#	print (confirmed)
	pop = unconfirmed.pop()
	print (pop)
#	print (unconfirmed)
