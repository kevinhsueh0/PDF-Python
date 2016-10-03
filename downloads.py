import urllib

testfile = urllib.URLopener()
for num in range(1, 555):
	testfile.retrieve("http://reader.eblib.com/(S(cdchyh53ejp05mm1zwwimla1))/GetPage.aspx?r=pdf&z=0&pg=%d&s=1467322813096" %num, "%d.pdf" %num)
