
1. Update UpdateAccountForm in forms.py
      - import FileField, FileAllowed
            FileAllowed acts as validator to tell what types of files 
            can be uploaded

      - add picture property
            picture = FileField('Update profile picture', validators=[FileAllowed(['jpg','png'])])

2. Add picture field in the account template/view
      - add picture field
            {{ form.picture.label() }}
            {{ form.picture(class="form-control-file") }}
            This is file field. so the errors view can be different from other fields 
      
      - add encoding type ! in order to submit image data properly
            <form action="" method="post" enctype="multipart/form-data">


3. test website
      http://127.0.0.1:5000/
      http://127.0.0.1:5000/account

      Try to upload a text file to validate the errors. ie. 
            "File does not have an approved extension: jpg, png"

4. Create a function to save the pictures in the specific directory in routes.py
      - import os, secrets
      - create 
            def save_picture(form_picture):

5. Update account() route in routes.py to save the uploaded pictures 
      in the specific directory, and store the file name in the database

      !!! Only the file name is stored in database. (current_user.image_file)

        if form.picture.data :
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file

6. update save_picture() in routes.py to resize the images before save

      - $ pip3 intall Pillow
      - from PIL import Image
      - update save_picture()
            output_size = (125, 125)
            i = Image.open(form_picture)
            i.thumbnail(output_size)
            i.save(picture_path)


7. test website
      http://127.0.0.1:5000/
      http://127.0.0.1:5000/account

      Try to upload a new picture