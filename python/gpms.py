from requests import session
import urllib, urllib2, cookielib,json
global login, post1, post2
headmeta = {
'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Origin' : 'http://gpms.amritanet.edu',
'X-DevTools-Emulate-Network-Conditions-Client-Id' : '0DC79D48-6BE3-4C15-A1AC-20B46AA6FA25',
'Upgrade-Insecure-Requests' : '1',
'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/47.0.2526.106 Chrome/47.0.2526.106 Safari/537.36',
'Content-Type' : 'application/x-www-form-urlencoded',
'Referer' : 'http://gpms.amritanet.edu/gpis/student/applyleave.php',
'Accept-Encoding' : 'gzip, deflate',
'Accept-Language' : 'en-GB,en-US;q=0.8,en;q=0.6',
}
def login() :
	t_login={}
	t_login['userid']=raw_input("Enter Roll Number : ")
	t_login['passwd']=raw_input("Enter Password : ")
	t_login['submit']=''
	loginf=json.dumps(t_login)
	return loginf


payloader = {
'stregno' : 'CB.EN.U4CSE14240',
'stname' : 'Sachin S Kamath', 
'sthostel' : 'VB',
'passtaken' : '',
'passtype' : 'Day Pass',
'fromdate': '07 Mar 2016',
'fhour':'7',
'fmin':'00',
'applyingto':'Warden',
'occasion':'Regular Academic Semester',
'groundsforleave':'going to city',
'leavesubmit':'Submit Leave',
}

payload2 = {
'regno' : 'CB.EN.U4CSE14240',
'stname' : 'Sachin S Kamath',
'applyingto':'Warden',
'passtype' : 'Day Pass',
'occasion':'Regular Academic Semester',
'groundsforleave':'going to city',
'fromdate': '07 Mar 2016 7:00:00',
'todate': '07 Mar 2016 19:00:00',
'noofdays':'1',
'confirm':'Confirm',
}

print login()
with session() as c:
    c.headers.update(headmeta)
    response=c.post('http://gpms.amritanet.edu/gpis/student/index.php', data=login())
    c.headers.update(headmeta)
    print(response.headers)
    #c.post('http://gpms.amritanet.edu/gpis/student/applyleave.php', data=payloader)
    #c.headers.update(headmeta)
    #c.post('http://gpms.amritanet.edu/gpis/student/applyleave.php', data=payload2)
    #resp2=c.get('http://gpms.amritanet.edu/gpis/student/leavestatus.php')
    #print(resp2.text)





