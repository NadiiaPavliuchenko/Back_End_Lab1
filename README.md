#Інструкція для запуску проекту локально

Активувати віртуальне середовище командою activate.bat

'\Back_End_Lab1\env\Scripts > activate.bat'

Перейти в корінь та запустити застосунок забілдивши та запустивши docker-compose командами:

'docker-compose build'

'docker-compose up'

Для того щоб перевірити роботу запитів на сторінці в рядку після назви домену дописати:

Для виводу всіх категорій:

'https://npavlbackendlab1.herokuapp.com/categories'

Для виводу записів по користувачу окрім шляху потрібно вказати ім'я користувача(наприклад Ann або Andy які присутні в списку):

'https://npavlbackendlab1.herokuapp.com/getNoteByUser/<username>'


Для виводу записів по категорії та користувачу окрім шляху потрібно вказати назву категорії та ім'я користувача(наприклад Ann/health або Andy/bills які присутні у списку):

'https://npavlbackendlab1.herokuapp.com/getNote/<username>/<categoryName>'

Post запити перевіряються за допомогою колекції Postman

