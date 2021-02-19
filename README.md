# code_snippets
https://github.com/CoreyMSchafer/code_snippets

# youtube
https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH

- Flask tutorials 
  code_snippets/Python/Flask_Blog/

- git checkout one directory in git repo

$ git clone \
  --depth 1  \
  --filter=blob:none  \
  --sparse \
  https://github.com/zhjohn925/code_snippets \
;
cd test-git-partial-clone
git sparse-checkout init --cone
git sparse-checkout set Python/Flask_Blog
