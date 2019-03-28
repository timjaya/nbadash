from passlib.hash import sha256_crypt
print(sha256_crypt.hash('timisgreat'))
print(type(sha256_crypt.hash('hammaadisnot')))

print(sha256_crypt.verify("hammaadisnot", sha256_crypt.hash('hammaadisnot')))