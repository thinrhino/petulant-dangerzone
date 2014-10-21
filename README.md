petulant-dangerzone
===================

1. Run `python manage.py runserver`, `node myserver.js` & `redis`
2. Access 'http://127.0.0.1:8000' to open socket connection
3. In JS Console make POST request
    ```
    var formPost = document.createElement('form');
    formPost.method = 'POST'; 
    formPost.action = 'http://127.0.0.1:8000/send-message/?message=test'; 
    document.body.appendChild(formPost); 
    formPost.submit();
    ```

The message 'test' should be seen in the console and `OK` in the browser
