Ядед (@ya_xyecoc) создал таблицу эхо-ботов, которую я затем преобразовал в приложение на Flet. Вы можете ознакомиться с этой таблицей на его канале: [dedtab](https://t.me/dedtab).

Инструкции по сборке приложения доступны на сайте: [flet.dev](https://flet.dev/).

Все, что вам нужно для успешного запуска, находится в папке webapp. 
1. Загрузите исходный код.
2. Убедитесь, что у вас установлены все необходимые библиотеки, запустив команду: pip install -r requirements.txt
3. Для удобства рекомендуется создать отдельную виртуальную среду.

Папка images АБСОЛЮТНО не нужна для работы сайта, все изображения загружаются с гугл диска(смотрите main.json)

Файл main.json частично сгенерирован с помощью Python (файл extract from xlsx copy 5.py в папке extras) и был дополнен вручную.

Все файлы содержат подробные комментарии, поэтому разобраться в коде не составит труда.

В ветке build-site находится тестовый(пока что) файл для его деплоя. Как только доделаю его, выдачу полноценный гайд. 
