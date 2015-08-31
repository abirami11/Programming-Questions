def routeChk(Adj, source, dest):
	visited = []
	gnode = [source]
	level = 0
	while gnode:
		level += 1
		next = []
		for enode in gnode :
			for evalue in Adj[enode]:
				if evalue == dest:
					return "Found path of level", level
				else:
					if evalue not in visited:
						next.append(evalue)
						visited.append(evalue)
		gnode = next
	return "Sorry Not Found"

Adj = { 'v1':{'v2','v4'} , 'v2':{'v4','v5'}, 'v3':{'v1','v6'}, 'v4':{'v5'}, 'v5':{'v4'}}
source = 'v1'
dest = 'v3'
print routeChk(Adj, source, dest)
