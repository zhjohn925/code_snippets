import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from flaskblog import mail

# save uploaded image to the specified path
def save_picture(form_picture) :
    random_hex = secrets.token_hex(8)
    # underscore (_) ignoring the value
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    # define the path to store profile image
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)
   
    # save the uploaded image into the specified path

    # do not want to save the original uploaded image, which can be very large
    #form_picture.save(picture_path)

    #resize the image before store
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


# Send email with the link to reset password
# The URL link is specified by url_for(), route to reset_token()
# _external=True tells Flask that it should generate an absolute URL, and not a relative URL. 
def send_reset_email(user) :
    token = user.get_reset_token()
    msg = Message('Password Reset Request', sender='noreply@demo.com', 
                   recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
{url_for('users.reset_token', token=token, _external=True)}

If you did not make this request then simply ignore this email and no changes will be made.
'''
    mail.send(msg)


