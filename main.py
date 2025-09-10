import hashlib
s='nanobridge'
print('short:'+hashlib.md5(s.encode()).hexdigest()[:8])
