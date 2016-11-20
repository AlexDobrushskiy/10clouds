# Yet another URL shortener service

 - Root URL - entering URL form. After submitting redirects to URL details page.
 ```
 /
 ```
 
 - URL details page  - shows both original and shortened URL, also provices username of owner.
 ```
 /!<url_shortened_postfix>
 ```
 - URL shortener redirect page - redirect to original URL

```
  /<url_shortened_postfix>
 ```
 
## Creating users

 - ```./manage.py create_fake_users <number_of_users>```
 
 This will ask randomuser.me API for __number_of_user__ users, and will kindly create it in django applicaton.
 
