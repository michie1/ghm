from github import Github
import shelve

ACCESS_TOKEN = '387fd2ef4494b1c5f10f931bde5b28362c1443b1'

def loadRepos(client, data, data2, amount):
	r = client.get_repos(s['rep_last_id'])
	for i in range(amount):
		print r[i].full_name
		s['rep_last_id'] = r[i].id
		contributors = []
		for c in r[i].get_contributors():
			data.append( (c.id, c.login, r[i].id, r[i].full_name) )
			contributors.append(c.id)
		data2.insert(r[i].id, contributors)

client = Github(ACCESS_TOKEN, per_page=100)
s = shelve.open('storage')
data = s['data'] # (user_id, user_login, repo_id, repo_full_name)
data2 = s['data2']

print client.rate_limiting

loadRepos(client, data, data2, 10)

print client.rate_limiting

s['data'] = data
s['data2'] = data2
print len(s['data'])
s.close()

#print r[0].id

#stargazers = [ s for s in repo.get_collaborators() ]
#print stargazers[0].id, stargazers[0].login
#print stargazers[0].get_repos()[0].id, stargazers[0].get_repos()[0].name


