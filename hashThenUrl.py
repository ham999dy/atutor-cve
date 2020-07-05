import hashlib, time
host = 'www.google.com'
password2 = '$2y$12$yO.G1CFZR/WJqOjSoxzCKO92hd9RbvbcvzfG1.g3wAY3ZZJZ0gvAG'

_time = int(time.time())
userid = 1
_hash = str(userid+_time)+str(password2)
m = hashlib.sha256()
_hash2=_hash.encode('utf-8')
m.update(_hash2)
phash = m.hexdigest()
pwhash = phash[5:30]

url5 = "http://%s/reset/%s/%s/%s"%(host,userid,_time,pwhash)