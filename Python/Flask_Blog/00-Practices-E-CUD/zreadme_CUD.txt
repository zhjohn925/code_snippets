email: C@demo.com
password: password

Create, Update, Delete posts

- add post/new in routes05.py
- create template create_post.html
- add PostForm class in form05.py
- pass form into template in route05.py
- update create_post.html, ie. copy login.html then modify
- add "New Post" navbar in layout11_flash.html
- update __init__.py with routes05
- test website
- add post into database in routes06.py
- remove the dummy posts in routes06.py
- update posts from database in home() route in routes06.py
- update home12_post.html to display the post
- update route06 with home12_post.html
- test website

Edit a single post
- Add /post/<int:post_id> in route06.py
- create post.html  (copy home.html and modify)
- update home12_post.html post link with post_id
- Add /post/<int:post_id>/update in route06.py
  add legend in "Update Post" and "New Post"
- Use the same template(create_post.html) as "/post/new" by adding legend
- Update /post/<int:post_id>/update in route06.py to store post into database
- test website
  http://localhost:5000/post/1
  http://localhost:5000/post/1/update

- add "Update" button in  post01.html  
- Add "Delete" button in post01.html with bootstrap modal
  https://getbootstrap.com/docs/4.0/components/modal/
  Look for "Live demo"
  Change "exampleModal" to "deleteModal"
- Edit Model block in post02.html for delete post
  "Delete" button route to delete_post(), and pass post_id
  "Delete" sends "POST" request to delete the post
- Add delete_post route in route06.py



  


