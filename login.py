import urllib
import urllib2
import cookielib
import hashlib

class Login(object):
    
    def __init__(self, username, password):
        self.username = username
        hash = hashlib.md5()
        hash.update(password)
        md5password = hash.hexdigest()
        self.password = md5password
        
    def monilogin(self):
        #GLOBAL URL
        hosturl = 'http://172.28.18.226:7001/lemis/'
        loginurl = 'http://172.28.18.226:7001/lemis/logonAction.do?method=userLogin'
        
        #GET COOKIE
        cj = cookielib.CookieJar()
        cookie_support = urllib2.HTTPCookieProcessor(cj)
        opener = urllib2.build_opener(cookie_support,urllib2.HTTPHandler)
        urllib2.install_opener(opener)
        h = urllib2.urlopen(hosturl)
        cookie = h.info().get('Set-Cookie').split(';')[0]        
        
        #loginIn
        cname = 'c_name=' + urllib.quote(self.username.encode('utf-8'))
        self.cookie = cookie + '; ' + cname + '; ' + 'c_pass='
        
        loginData = {
       	'bsc011':self.username.encode('gbk') ,
       	'bsc013':self.password,
       	'sys001':'2'
       	}
        loginData = urllib.urlencode(loginData)    
        request = urllib2.Request(loginurl, loginData)
        #add header    
        request.add_header('Cache-Control','max-age=0')
        request.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.94 Safari/537.36')
        request.add_header('Connection','keep-alive')
        request.add_header('Cookie',cookie)
        request.add_header('Content-length',68)
        request.add_header('Content-Type','application/x-www-form-urlencoded')
        request.add_header('Host','172.28.18.226:7001')
        request.add_header('Origin','http://172.28.18.226:7001')
        request.add_header('Referer','http://172.28.18.226:7001/lemis/LogonDialog.jsp')
        #LoginIn
        response = urllib2.urlopen(request)    
        
    def MorningSI(self):
        url = 'http://172.28.18.226:7001/lemis/ad01Action!save_ad01.action?flag=1'
        request = urllib2.Request(url)
        request.add_header('Cookie',self.cookie)
        response = urllib2.urlopen(request)
        
    def MorningSO(self):
        url = 'http://172.28.18.226:7001/lemis/ad01Action!save_ad01.action?flag=3'
        request = urllib2.Request(url)
        request.add_header('Cookie',self.cookie)
        response = urllib2.urlopen(request)
        
    def NoonSI(self):
        url = 'http://172.28.18.226:7001/lemis/ad01Action!save_ad01.action?flag=4'
        request = urllib2.Request(url)
        request.add_header('Cookie',self.cookie)
        response = urllib2.urlopen(request)
        
    def NoonSO(self):
        url = 'http://172.28.18.226:7001/lemis/ad01Action!save_ad01.action?flag=2'
        request = urllib2.Request(url)
        request.add_header('Cookie',self.cookie)
        response = urllib2.urlopen(request)
        
