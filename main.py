import hashlib
s='minilab'
print('short:'+hashlib.md5(s.encode()).hexdigest()[:8])
