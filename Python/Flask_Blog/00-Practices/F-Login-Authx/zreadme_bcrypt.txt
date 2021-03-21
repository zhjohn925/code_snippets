$ python
>>> bcrypt = Bcrypt()

# b means hashed password in byte format
>>> bcrypt.generate_password_hash('your_password')
    b'$2b$12$nan0ZhknpdPHUgTPKx27geXaCyrCtBFClk.0YSz9D0BVNOKcybOhW'

# hashed password in character format
# we can see hash are different based on the same password 
>>> bcrypt.generate_password_hash('your_password').decode('utf-8')
    '$2b$12$080.AL.nqdj4wTYu.Ae02.B/lc77HygugUT1Rqf.0Bcbe1d1ISg6a'
>>> bcrypt.generate_password_hash('your_password').decode('utf-8')
    '$2b$12$p4cmYDJKoBRxhtnPxpdDU.BnOWBy8R89asbsVKI8Df.D72DtcB6Ya'
>>> bcrypt.generate_password_hash('your_password').decode('utf-8')
    '$2b$12$uKctg3caQeZ7v96DzHImh.PJvwufhUiJwFogsrHOVGWi0oDJCUAO2'

# use check_password_hash() to compare password with hash
>>> hashed_pwd=bcrypt.generate_password_hash('your_password').decode('utf-8')
>>> bcrypt.check_password_hash(hashed_pwd, 'your_password')
True
>>> bcrypt.check_password_hash(hashed_pwd, 'my_password')
False
>>> pwd='$2b$12$080.AL.nqdj4wTYu.Ae02.B/lc77HygugUT1Rqf.0Bcbe1d1ISg6a'
>>> bcrypt.check_password_hash(pwd, 'your_password')
True
>>>