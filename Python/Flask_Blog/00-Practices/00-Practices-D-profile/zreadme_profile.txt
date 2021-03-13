email: C@demo.com
password: password

- update account02.html with profile image
- copy profile_pics into static/
- update rountes02.py to pass the profile images into account.html
- change rountes to rountes02 in __init__.py
- test website
- add UpdateAccountForm() in forms02.py
- pass UpdateAccountForm to account.html in rountes02.py
- add update account form in account02.html
- test website

Update the account profile
- update account route in routes03.py to enable profile update into database
- change rountes to rountes03 in __init__.py
- test website

upload the profile image
- update UpdateAccountForm in forms04.py 
  ie. add picture property 
- add upload picture in account04.html template
  do not forget to put enctype="multipart/form-data" in form tag
- add save_picture() in routes04.py
- change rountes to rountes04 in __init__.py
- test website (to upload profile image)
- install Pillow (Use to reduce the image size)
  $ pip3 install Pillow
- resize image with Pillow package

