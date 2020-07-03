# Detection (Faster R-CNN)

1)Выбор фреймворка/библиотеки для использования детектора

torchvision.models.detection


2)Запуск детектора на случайных изображениях
Результат в каталоге "2 - Запуск детектора на случайных изображениях"

1 сценарий

3)Выбор фреймворка/библиотеки для разработки веб/мобильного демо

микрофреймворк Flask


4)Разработка демо и 5)Встраивание модели-детектора в демо

6)Тестирование демо
Результат в каталоге "6 - Тестирование".
К слабым сторонам можно отнести то, что один и тот же объект может помечаться несколько раз, как на изображениях airplane3.png (один человек два раза детектировался), boat.png, train.png. К положительным сторонам можно отнести то, что малозаметные и неполные объекты тоже детектируются, как на изображениях airplane3.png (детектор нашёл человека по ногам), bus.png (детектор нашёл людей за окнами транспорта). 
С изображениями train2.png, traffic light2.png, person3.png, person2.png, person.png, boat2.png bicycle3.png, airplane2.png детектор справился хорошо, так как объекты изображёны крупным планом.


7)Оформление демо для показа другим людям
Применение стилей (css), библиотека Bootstrap


Нужно клонировать репозиторий, установить прописанные в requirements.txt модули.
Для запуска демо нужно запустить: python3 скрипт "./run.py".
Не следует использовать браузер Firefox, так как изображения загружаются на страницу искаженные. (В Opera всё выглядит как положено). 
При запуске приложения пользователь попадает на страницу "Загрузить из файла". Нужно выбрать изображение и нажать кнопку "Сохранить", после этого ниже появизьтся результат детектирования. Обработка изображений может длиться минуту.
