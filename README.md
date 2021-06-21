# Django Rocket Data Test
## Запуск проекта

Чтобы запустить этот проект, вы должны начать с установки Python на вашем компьютере. Рекомендуется создать виртуальную среду для хранения зависимостей ваших проектов отдельно. 

  ```
  pip install virtualenv
  ```

Клонируйте или загрузите этот репозиторий и откройте его в выбранном вами редакторе. В терминале (mac/linux) или терминале Windows выполните следующую команду в базовом каталоге этого проекта

  ```
  virtualenv env
  ```

Это создаст новую папку env в каталоге вашего проекта. Затем активируйте его с помощью этой команды на mac/linux:

  ```
  source env/bin/active
  ```

Затем установите зависимости проекта с помощью:

  ```
  cd your_disk_name:\Test_Rocket_Data\Test_Rocket
  pip install -r requirements.txt
  python manage.py create_superuser
  python manage.py makemigrations
  python manage.py migrate
  python manage.py runserver
  ```
Команда python manage.py create_superuser создат суперпользователя(login=admin, password=admin)

Для добавления новых работников выполните команды:

  ```
  python manage.py fake
  ```

Что бы запустить celery задачи Вам требуется запустить Redis и выполнить команды:

  ```
  celery -A Test_Rocket beat -l INFO
  celery -A Test_Rocekt worker -l INFO --pool=solo
  ```

Что бы зайти в админ панель перейдите в браузере

  ```
  http://127.0.0.1:8000/admin
  ```
и войдите под данными superuser.

Что бы просмотреть все данные о сотрудниках используя API перейдите в браузере:

  ```
  http://127.0.0.1:8000/api
  ```

Для просмотра сотрудников одного уровня перейдите

  ```
  http://127.0.0.1:8000/api/<level>
  ```

<level> Может быть Level_1, Level_2, Level_3, Level_4, Level_5.

Что бы испоьзовать аутентификацию через api перейдите 

  ```
  http://127.0.0.1:8000/api-auth/login/
  ```
Так же доступна аутентификация через api-key.
Что бы получить ключ требуется выполнить запрос :
  
  ```
  http://127.0.0.1:8000/api-auth/get-token/
  ```
  
## Запуск проекта при помощи  docker-compose
  
Выполните команды:
  
  ```
  cd your_disk_name:\Test_Rocket_Data\Test_Rocket
  docker-compose build
  docker-compose up
  ```
___________________________________________________________  
# Примечание

Данный проект является тестовым заданием.


