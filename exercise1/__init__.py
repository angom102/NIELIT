#print("Hello")
import webbrowser as wb
import time as t
url1="https://www.google.com"
url2="www.yahoo.com"
url3="www.msn.com"
i=1
while(i<4):
    print("inside loop")
    t.sleep(5)
    wb.open_new(eval('url%d' % i))
    i=i+1
