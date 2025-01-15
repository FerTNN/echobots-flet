import flet as ft
import json
import os
from dataclasses import dataclass
from typing import Optional, Dict, Any

DATA = [
    {
        "Бот": {
            "text": "ECHO TO ALL BOT",
            "link": "https://drive.google.com/u/0/drive-viewer/AKGpihbPTH1AisPFQ_xiG6yL-OghHmq8SPAVpJR83ofg2-MdE0QzOBOfM2Tf3WQZs3E_MTC_fk7y07v0jWeU5yZE80yvSEJRNucWa8A=s1600-rw-v1",
            "image_path": " webapp\\images\\image_0_1xEXiyoJrI4jn_em29cSmmomQdXdHygwH.jpg"
        },
        "Нынешний юз": "@echoall_mv_bot",
        "Первый запуск": "17 апреля 2021",
        "Второй запуск": "10 Октября 2021 С @echoallbot бот был перемещен на @allechobot перейдя в режим NORULES.",
        "Старый юз": "@echoallbot",
        "Кд": "1 час",
        "Примечания": {
            "text": "Первый бот Лукаша. Был закрыт из-за проблем с хостом.",
            "link": "https://drive.google.com/u/0/drive-viewer/AKGpihYKm6FAwp7wKi606liYlBeavt8racI7WDeUS0xuM7MaHhojRWddxMIw3-IOFp5gjUqIH5cVXi09cNzBB5ZupdVaxh5mezn3VPI=s2560",
            "image_path": " webapp\\images\\image_0_1SGrzx7-ggAfN37AJv_ONsgQTiBIVOwIH.jpg"
        },
        "Дата смерти": "17 февраля 2022 (деление ботов)",
        "Владелец": "Łukasempaiz 🇺🇿",
        "Функционал (команды)": "Пустая ячейка",
        "Кол-во юзеров": "Пустая ячейка",
        "Статус": "Не работает",
        "Каналы Ботов": "https://t.me/tshelter",
        "Сурсы": "Свои",
        "Айди": 1710715334
    },
    {
        "Бот": {
            "text": "ECHO TO ALL BOT [NORULES]",
            "link": "https://drive.google.com/u/0/drive-viewer/AKGpihZv8l88cAFB7xqh4fd7H2lLX7MSrtyo09b_VjOL6jxibmVtFkjXnPt1Mr_FhV_ZqDTK0qmruYT5c8CdWnTXXxshtlOM4Jfnzw8=s1600-rw-v1",
            "image_path": " webapp\\images\\image_1_1sfZBk59cjyURHL5rB28iBbxIVn26Ddnr.jpg"
        },
        "Нынешний юз": "@AllEchaBot",
        "Первый запуск": "17 февраля 2022",
        "Второй запуск": "-",
        "Старый юз": "-",
        "Кд": "5 минут",
        "Примечания": "17 Февраля бот перешёл в режим NORULES.",
        "Дата смерти": "17 апреля 2023",
        "Владелец": "Łukasempaiz 🇺🇿 Gogopro",
        "Функционал (команды)": "Пустая ячейка",
        "Кол-во юзеров": "Пустая ячейка",
        "Статус": "Не работает",
        "Каналы Ботов": "https://t.me/EchoAllChannel",
        "Сурсы": "Свои",
        "Айди": 2095178671
    },
    {
        "Бот": {
            "text": "ECHO TO ALL BOT [ATOM⚛️]",
            "link": "https://drive.google.com/u/0/drive-viewer/AKGpihY3r5Q51IJq8QrzedDylNQo86HRArWk5mg7uUx6cBv21xRvC_ZHpUss-a0mcV3XO2iB3k1T5rVlZMqlwS5e0DQc3Olx4QrNTPU=s1600-rw-v1",
            "image_path": " webapp\\images\\image_2_1quNxADXYzIJ1UeNyQDYlcB2-C8mO3fh8.jpg"
        },
        "Нынешний юз": "Бот удалён",
        "Первый запуск": "17 февраля 2022",
        "Второй запуск": "-",
        "Старый юз": "@echo2allbot",
        "Кд": {
            "text": "5 минут > 2 минуты > 5 минут",
            "link": "https://drive.google.com/u/0/drive-viewer/AKGpihZLj70jKOf2pJ_ZkrCv42odvN0_S6DETqSzLzQpgErx5dT-H0lMBpVV14Al6zk27r7fy1f3a4s0bIK7wANRDhYJavMlt1DLfwo=s1600-rw-v1",
            "image_path": " webapp\\images\\image_2_15p7bjfRYTP7SwxdY0GLgB3jgmQ-UNn7R.jpg"
        },
        "Примечания": "АТОМ появился в результате перехода первого бота в NORULES, как альтернатива С правилами.",
        "Дата смерти": "1 апреля 2023",
        "Владелец": "Łukasempaiz 🇺🇿 Kreazot Fiesti (?)",
        "Функционал (команды)": "Пустая ячейка",
        "Кол-во юзеров": "Пустая ячейка",
        "Статус": "Снесён",
        "Каналы Ботов": "https://t.me/EchoAllChannel",
        "Сурсы": "Свои",
        "Айди": 5175007996
    },
    {
        "Бот": {
            "text": "Echo to all 2 (Государство котов)",
            "link": "https://drive.google.com/u/0/drive-viewer/AKGpihajQ3Ru0urmowxDmIhR4m-DlRUfSXYzAi3m7hXKyhWOklG-VfTAhC6vaJC4buWr2veJ--I72qPTaWrqh1FCmUZ-ac4yO9vn9w=s1600-rw-v1",
            "image_path": " webapp\\images\\image_3_1WMxxWzfriRAns5DnnN7f643GdUYa-Y6L.jpg"
        },
        "Нынешний юз": "@echoall2bot",
        "Первый запуск": "30 арпеля 2021",
        "Второй запуск": "-",
        "Старый юз": "-",
        "Кд": "30 секунд",
        "Примечания": "КД постоянно менялось. На момент написания эта строка валидна",
        "Дата смерти": "-",
        "Владелец": "mak aka (Error_mak25)",
        "Функционал (команды)": "Пустая ячейка",
        "Кол-во юзеров": "Пустая ячейка",
        "Статус": "Работает",
        "Каналы Ботов": "https://t.me/MaMush_blog",
        "Сурсы": "https://gitlab.com/Ma-Mush/echoall",
        "Айди": 1658709401
    },
    {
        "Бот": {
            "text": "Дрочаг | PRIVATE | 🔞",
            "link": "https://drive.google.com/u/0/drive-viewer/AKGpihZSFjGE9PHl8n_aW1khSJNyEjyqgFo_MhwKeWMPspDahh4zejYSmhOu73GQSGS7PirnK6bFzQPsiyKzIoXvrajsvr8TAdaXiio=s1600-rw-v1",
            "image_path": " webapp\\images\\image_4_1G2o3Pl09bXh1A4brF_x5gqnt_YnJPyHY.jpg"
        },
        "Нынешний юз": "@dr04bot",
        "Первый запуск": "13 июня 2021",
        "Второй запуск": "-",
        "Старый юз": "-",
        "Кд": "10 секунд",
        "Примечания": "\"он был прородителем атома/норулса\" – a9fm [RT/FOXY]:~$",
        "Дата смерти": "24 августа 2021",
        "Владелец": "ra1n",
        "Функционал (команды)": "Пустая ячейка",
        "Кол-во юзеров": "Пустая ячейка",
        "Статус": "Не работает",
        "Каналы Ботов": "?",
        "Сурсы": "Свои",
        "Айди": 1822321755
    },
    {
        "Бот": {
            "text": "Дрочаг | PRIVATE | 🔞",
            "link": "https://drive.google.com/u/0/drive-viewer/AKGpihZSFjGE9PHl8n_aW1khSJNyEjyqgFo_MhwKeWMPspDahh4zejYSmhOu73GQSGS7PirnK6bFzQPsiyKzIoXvrajsvr8TAdaXiio=s1600-rw-v1",
            "image_path": " webapp\\images\\image_4_1G2o3Pl09bXh1A4brF_x5gqnt_YnJPyHY.jpg"
        },
        "Нынешний юз": "@DR04_bot",
        "Первый запуск": "13 июня 2021",
        "Второй запуск": "-",
        "Старый юз": "-",
        "Кд": "10 секунд",
        "Примечания": "\"Так же просьба в примечаниях дописать, что а9фм х*есос\" – ra1n",
        "Дата смерти": "29 августа 2022",
        "Владелец": "",
        "Функционал (команды)": "Пустая ячейка",
        "Кол-во юзеров": "Пустая ячейка",
        "Статус": "Не работает",
        "Каналы Ботов": "",
        "Сурсы": "",
        "Айди": 5055703220
    },
    {
        "Бот": {
            "text": "EchoAll – 1984.",
            "link": "https://drive.google.com/u/0/drive-viewer/AKGpihYUOA-xbmpC5zCa5dLNdqqAvFdk96gH0nz6hbv9G2qkay6ISjyLLjCfPZTKO2r0GyMEDKkOgxc4KPWfyGIpX29CEf9zpnRG9A=s1600-rw-v1",
            "image_path": " webapp\\images\\image_6_1-Rz9q6t5CYfZhZcwnNOBu14x-wIOQD2z.jpg"
        },
        "Нынешний юз": "@echoall_robot",
        "Первый запуск": "14 июня 2021 года",
        "Второй запуск": "-",
        "Старый юз": "-",
        "Кд": "0 секунд",
        "Примечания": "\"я его три раза переписывал, ибо каждый раз ловил тильт из-за отсутствия актива\" – ️ саьчиу ☺️ \"мы просто кодили, понимали что людей нет и все бросали\" – ️ саьчиу ☺️ \"со временем ты открываешь что-то новое или иначе смотришь на старые вещи, и переписать код будет лучшим вариантом, чтоб не тащить старое говно в новый проект\" – ️ саьчиу ☺️ \" только надо ещё добавить, что наш бот трахал все остальные боты по функционалу и чистоте кода, а ещё наш бот ебал всех, потому что у нас webapp профили появился ещё как только его в телеграм добавили\" – Eugene Conrad [ЧЕК БИО]",
        "Дата смерти": "-",
        "Владелец": "саьчиу ☺️ Eugene Conrad [ЧЕК БИО]",
        "Функционал (команды)": "Пустая ячейка",
        "Кол-во юзеров": "Пустая ячейка",
        "Статус": "Работает с перебоями",
        "Каналы Ботов": "https://t.me/ca4tuk_krytoi",
        "Сурсы": "Свои",
        "Айди": 1856938356
    },
    {
        "Бот": {
            "text": "Echogram",
            "link": "https://drive.google.com/u/0/drive-viewer/AKGpihasptwgAs8T17f5-z4MOeO4BDwinD-uYIbhVDDlImVKqnEBHn8ZX6l7pBmKJo5kNZkIH5A6ZZc-1DlgNen3TUQjJrivGEi7tg=s1600-rw-v1",
            "image_path": " webapp\\images\\image_7_1mYb19Yb_Ib337j-HYQWk7pVudkBXPqD7.jpg"
        },
        "Нынешний юз": "@EchogramBot",
        "Первый запуск": "февраль 2022",
        "Второй запуск": "-",
        "Старый юз": "-",
        "Кд": "0 секунд",
        "Примечания": "– А владелец бота ты или кто то другой? – ну онилух был а потом мне передал – я забил х*й и все – beevil",
        "Дата смерти": "18 ноября 2023",
        "Владелец": "onilyxe > beevil",
        "Функционал (команды)": "Пустая ячейка",
        "Кол-во юзеров": "Пустая ячейка",
        "Статус": "Не работает",
        "Каналы Ботов": "Зв'язок з адміном: @OnilyxeBot",
        "Сурсы": "\"первое время чужие потом я для **** с нуля все написал\" – beevil",
        "Айди": 5786275695
    },
    {
        "Бот": {
            "text": "ECHO TO ALL [milfa]",
            "link": "https://drive.google.com/u/0/drive-viewer/AKGpihaoeQtR_Wlt0vHlodVKnpgp-EFhF0UbowzdGMJH3X7Bw8qmks6tEzr3N3tR7Jn0l6HpBFTSbrOZXrG1BltnjDK7bwBCCTrzOA=s1600-rw-v1",
            "image_path": " webapp\\images\\image_8_1w0iacnQ8S1GPFsoG67n2qXFOVBd1rLpD.jpg"
        },
        "Нынешний юз": "@echo_all_bot",
        "Первый запуск": "март 2022",
        "Второй запуск": "-",
        "Старый юз": "-",
        "Кд": "0 секунд",
        "Примечания": "\"инфы никакой нету. он существовал наверное неделю, а кд в нём не было\" – Дмитрий",
        "Дата смерти": "март 2022",
        "Владелец": "@milfaboy (неактуальный юз)",
        "Функционал (команды)": "Пустая ячейка",
        "Кол-во юзеров": "Пустая ячейка",
        "Статус": "Не работает",
        "Каналы Ботов": "Нету информации.",
        "Сурсы": "Нету информации.",
        "Айди": 2031220062
    },
    {
        "Бот": {
            "text": "Echo To All [No Rules / No Cooldown]",
            "link": "https://drive.google.com/u/0/drive-viewer/AKGpihaOPXKvirPjyv2p4i5M0nSVc6d63kuBaNkPkVir3QZaZSPGHe-ROqD9ZNz6sccTlrjxLtQRPt821IH9TgVTCWXuxkH5Spo2HKk=s1600-rw-v1",
            "image_path": " webapp\\images\\image_9_1uuEUex3wE4Ng8xWYbt0QEBBsc0jU_lDM.jpg"
        },
        "Нынешний юз": "@Echo_To_All_Chatbot",
        "Первый запуск": "ноябрь 2022",
        "Второй запуск": "-",
        "Старый юз": "@Echo_In_Telegram_Chatbot, @Echo_Of_Telegram_Chatbot",
        "Кд": "0 секунд",
        "Примечания": "\"Его снесли за то, что в последствии я подключил к нему API ГБ\" – ＧＲＯ＄＄ＭＡＮ \"Старый тег уже не помню, а истории за ним не было как таковой. На основе Эха я планировал запилить анонимный многопользовательский теневой чат, с тотальной модерацией и плюшками, недоступными в стандартных групповых чатах. Стандартный же Эхо был как просто песочница и испытательный полигон, для настройки всего кода, а еще, так, по фану\" – ＧＲＯ＄＄ＭＡＮ Старый юз – \"@Echo_In_Telegram_Chatbot Но ты используй @Echo_Of_Telegram_Chatbot Изначально задумывалось именно так, но я грамотей дхо*я и поздно заметил ошибку в теге. Посему, чтобы не позориться.\" – ＧＲＯ＄＄ＭＡＮ",
        "Дата смерти": "осень 2023",
        "Владелец": "ＧＲＯ＄＄ＭＡＮ",
        "Функционал (команды)": "Пустая ячейка",
        "Кол-во юзеров": "Пустая ячейка",
        "Статус": "Не работает",
        "Каналы Ботов": "?",
        "Сурсы": "Подгон от другого разраба",
        "Айди": 5660105172
    },
    {
        "Бот": {
            "text": "hydra - echo to all",
            "link": "https://drive.google.com/u/0/drive-viewer/AKGpihbp3uCidkIt6ZaCpvgH_JtWur1n3DdqrrrZG7JCYh4LW0TAhhvvlbsK9I8EDl5yQB4Y-vYndSitvLH3DYSAP59CTqWUXtN0EA=s1600-rw-v1",
            "image_path": " webapp\\images\\image_10_1LbhreFOi6zWyCaaqSeLv5C7t4IitIARJ.jpg"
        },
        "Нынешний юз": "",
        "Первый запуск": "2022-2023",
        "Второй запуск": "11 июня 2024",
        "Старый юз": "-",
        "Кд": "3 секунды",
        "Примечания": "\"Кд секунд 20 из-за очень низкой оптимизации и отправки сообщений на 30 пользователей по 3 секунды\" – Кугона",
        "Дата смерти": "Перезапуск бота я не буду считать за смерть.",
        "Владелец": "Кугона",
        "Функционал (команды)": "Пустая ячейка",
        "Кол-во юзеров": "Пустая ячейка",
        "Статус": "Не работает",
        "Каналы Ботов": "https://t.me/dragon_echo_all",
        "Сурсы": "Свои",
        "Айди": 5413178057
    },
    {
        "Бот": {
            "text": "Dragon Echo All (hydra)",
            "link": "https://drive.google.com/u/0/drive-viewer/AKGpihZ-dedBUreu45eBVZSJ4vKr6VHIiIH7nLwA697hG-E6i7PkIORTlzUwyWe186f1bbkxZLt42mWQ9mmLXBUZZl8jV5ooVOLqxA=s1600-rw-v1",
            "image_path": " webapp\\images\\image_11_15ESOHTVMN-ZPWP1s2kAsexyHGHIYvq4K.jpg"
        },
        "Нынешний юз": "@hydraechoall_bot",
        "Первый запуск": "11 июня 2024",
        "Второй запуск": "-",
        "Старый юз": "",
        "Кд": "3 секунды",
        "Примечания": "\"гидра закрылась из-за проблем, о которых я не могу поведать, было решение сделать ребрендинг и продолжить работу, но эхо не получил такого обновления, потому что я не верил в его жизнь\" – Кугона",
        "Дата смерти": "4 сентябр 2024",
        "Владелец": "",
        "Функционал (команды)": "Пустая ячейка",
        "Кол-во юзеров": "Пустая ячейка",
        "Статус": "Не работает",
        "Каналы Ботов": "https://t.me/dragon_echo_all",
        "Сурсы": "Свои",
        "Айди": "5413178057"
    },
    {
        "Бот": {
            "text": "Lukasz's FTG bot",
            "link": "https://drive.google.com/u/0/drive-viewer/AKGpihbDWFMtTQpB10b0i8H4FFhRVfid7RbwYroz8usjYjxKzaKzQ-mxek50XIeqN08FpM89VKQ4zgRAQzpBvbjUwDwB_com-zn-2L4=s1600-rw-v1",
            "image_path": " webapp\\images\\image_12_1W2TZ4aOzsPzoGLzSPAL44zRhQ7WBd5zV.jpg"
        },
        "Нынешний юз": "@ftg4bot",
        "Первый запуск": "январь 2023",
        "Второй запуск": "-",
        "Старый юз": "-",
        "Кд": "1 секунда",
        "Примечания": "Точных дат запуска фтг я не нашёл. В строке даты запуска указана дата моего появления в боте. Бота переодически ложили, КД было 10 секунд. \"@ftg4bot изначально был тестовым ботом для @ftg2bot А потом я его использовал для других тестов В том числе для теста альфа версии ремастера эхобота Мне нужно было проверить, работает ли там вообще очередь нормально Поэтому я оставил его включенным, а отключать стало жалко\" – Łukasempaiz",
        "Дата смерти": "24 декабря 2023",
        "Владелец": "Łukasempaiz 🇺🇿",
        "Функционал (команды)": "Пустая ячейка",
        "Кол-во юзеров": "Пустая ячейка",
        "Статус": "Не работает",
        "Каналы Ботов": "? https://t.me/tshelter",
        "Сурсы": "Свои",
        "Айди": 1996941754
    },
    {
        "Бот": {
            "text": "Echo To All No Rules [No Cooldown]",
            "link": "https://drive.google.com/u/0/drive-viewer/AKGpihYe8I_Jx3l4tu4H7sWvKHmXvnYYhSLBrTihyLWlHAIC5CeOJiJ6bFjo1DiU1YCfdCw8mdK9pHoh3KJvabIYgnZWAEI1z0-0gtE=s1600-rw-v1",
            "image_path": " webapp\\images\\image_13_19JI_r9CjVHvRLFZ2OjGa3Ue7F1zKoqIq.jpg"
        },
        "Нынешний юз": "@echotoall_bot",
        "Первый запуск": "9 апреля 2023",
        "Второй запуск": "-",
        "Старый юз": "-",
        "Кд": "0 секунд",
        "Примечания": "О боте нет никакой информации. О Владельце тем более, действительность владения этим пользователем под сомнением. \"это бот редановца который работал на коде , код сломанный то-то он и бота закрыл, а нах*я и почему не включает бота х*й знает\" – Анон из зоряны",
        "Дата смерти": "31 августа 2023",
        "Владелец": "reysuxs (@ALPHVV актуальный юз)",
        "Функционал (команды)": "Пустая ячейка",
        "Кол-во юзеров": "Пустая ячейка",
        "Статус": "Не работает",
        "Каналы Ботов": "утерян.",
        "Сурсы": "Нету информации",
        "Айди": 6241986163
    },
    {
        "Бот": {
            "text": "untitled",
            "link": "https://drive.google.com/u/0/drive-viewer/AKGpihaDX50Yvb37HYZPwsO6fuWhFSRYqJb9MounBSY2jLB-ch1xc0oBOqRF5QxLtXciEylwWy4Z9XauRzB6GBP4_3Ao7RSOoYm52A=s1600-rw-v1",
            "image_path": " webapp\\images\\image_14_1mHtc9Qhm9cW6mhZQVJvBe7Hu-PBj-K-v.jpg"
        },
        "Нынешний юз": "@untitled7bot",
        "Первый запуск": "15 апреля 2023",
        "Второй запуск": "-",
        "Старый юз": "-",
        "Кд": "0 секунд",
        "Примечания": "untitled: 18.07.24 21:20: untitled is startup now. 18.07.24 21:20: untitled is shutdown now.",
        "Дата смерти": "-",
        "Владелец": "минч",
        "Функционал (команды)": "Пустая ячейка",
        "Кол-во юзеров": "Пустая ячейка",
        "Статус": "Работает с перебоями",
        "Каналы Ботов": "-",
        "Сурсы": "https://github.com/hoangpungnyuga/Echo",
        "Айди": 6110017353
    },
    {
        "Бот": {
            "text": "ECHO TO ALL BMW",
            "link": "https://drive.google.com/u/0/drive-viewer/AKGpihY06QIq4xLar52pvxM49nyV022A-VITlFsvz9av84comhUWL7pmAW9MddJG1shDWCq52uhIoL19FmtgFlg7Y-6UdySzdtceOE8=s1600-rw-v1",
            "image_path": " webapp\\images\\image_15_1f0l4h9pSWL46cnU0F4Gfb2aWP5RaJ49e.jpg"
        },
        "Нынешний юз": "@ECHO_TO_ALL_BMW_BOT",
        "Первый запуск": "сентябрь 2023",
        "Второй запуск": "1 июля 2024",
        "Старый юз": "@ECHO_BMW_BOT_TEST_BOT",
        "Кд": "1 секунда",
        "Примечания": "\"был временно закрыт из-за проблем с хостом\" – lilpool 6 июля бот был перемещён на новый юзернейм – @ECHO_TO_ALL_BMW_BOT.",
        "Дата смерти": "26 января 2024",
        "Владелец": "Элитарная личность",
        "Функционал (команды)": "Пустая ячейка",
        "Кол-во юзеров": "Пустая ячейка",
        "Статус": "Не работает",
        "Каналы Ботов": "-",
        "Сурсы": "https://github.com/hoangpungnyuga/Echo",
        "Айди": 6518351898
    },
    {
        "Бот": {
            "text": "ECHO EB*L BOT",
            "link": "https://drive.google.com/u/0/drive-viewer/AKGpihad8hz4s60CVH0WgtxRwuPKTIsVgNJrIOr0OtSmbbO_8mVj-CW8VS-6KOO5gPvgHPnyDZ_HBp12nYq8_OC4zaTkGb1Fac4I2as=s1600-rw-v1",
            "image_path": " webapp\\images\\image_16_19WDikFHVAMAnjg15vDVFuvJ_P8vPh8zE.jpg"
        },
        "Нынешний юз": "@echoebalbot",
        "Первый запуск": "август 2022",
        "Второй запуск": "-",
        "Старый юз": "-",
        "Кд": "10 секунд 1 секунда между соо",
        "Примечания": "-А что с эхо еб*л? Его снесли? -на него х*й положили, говорили \"хоста нет\" а потом никому н*хуй не нужный эхо рум сделали и хост нашелся, а вот эхо еб*л так и не ожил – DOBRODELOV и Анон",
        "Дата смерти": "28 января 2024",
        "Владелец": "lord",
        "Функционал (команды)": "Пустая ячейка",
        "Кол-во юзеров": "Пустая ячейка",
        "Статус": "Не работает",
        "Каналы Ботов": "https://t.me/tonfsociety",
        "Сурсы": "Нету информации",
        "Айди": 5144253617
    },
    {
        "Бот": {
            "text": "🏳️‍🌈Gayecho [MAIN]",
            "link": "https://drive.google.com/u/0/drive-viewer/AKGpihZVHW0vD8dY15X9NTumV324WuKEiGK3Ca9FqXdQcVe7J_C0Ls0OOvXdW4m1fR-E41lK06HvWdcB8qg7pMTExtMzJ4qXgbCtGmA=s1600-rw-v1",
            "image_path": " webapp\\images\\image_17_1Z-bnEkU-euPvcDeVfrqTwNziTO-07Vd2.jpg"
        },
        "Нынешний юз": "@gayechobot",
        "Первый запуск": "1 января 2024",
        "Второй запуск": "14 августа 2024",
        "Старый юз": "-",
        "Кд": "3 секунды",
        "Примечания": "\"Ещё, гей эхо не будет. Вместо него альт. версия Зоряны\" – Blessed!! [4 декабря 2024]",
        "Дата смерти": "13 августа 2024, 13 ноября 2024",
        "Владелец": "Blessed!! id6440397991",
        "Функционал (команды)": "Пустая ячейка",
        "Кол-во юзеров": "Пустая ячейка",
        "Статус": "Не работает",
        "Каналы Ботов": "https://t.me/GayAnonEcho_XXX",
        "Сурсы": "Блесс утверждает, что использует собственные сурсы, однако он позаимствовал их из Эхокима и полностью переделал этих сурсов эхокима нету они очень древние",
        "Айди": 6979673544
    },
    {
        "Бот": {
            "text": "Зоряна - Київстар [NORULES]",
            "link": "https://drive.google.com/u/0/drive-viewer/AKGpihbgxN8bOWaNlpSIlCJwsiGNzxeSzOMNAbKioQcXaELJAStd-llW6Sha0Z9mRFe38S8LbZMxElC2uDXorNfRsHg-hazKZjdeUf0=s1600-rw-v1",
            "image_path": " webapp\\images\\image_18_1jfzmdBXOyrFhi28fuhpWKZxIZrSPTr7H.jpg"
        },
        "Нынешний юз": "@Zorlana_Kyivstar_Bot",
        "Первый запуск": "28 февраля 2024",
        "Второй запуск": "15 августа 2024, 4 декабя 2024",
        "Старый юз": "-",
        "Кд": "5 секунд",
        "Примечания": "8 июля КД увеличилось с 3 секунд до 7 из-за флудвейтов. \"Пропадает желание поддерживать ботов, а также, скорее всего, ботам осталось жить 48 дней (до 14 ноября) [отсчет деда] С пониманием.\" – Blessed!! [26 сентября 2024] \"Зоряна поднята. На сколько? Месяц точно. А дальше зависит от моего кошелька\" – Blessed!! [4 декабря 2024] \"В течение дня-двух Зоряна NORULES будет отключена по нескольким причинам.Одна из них: противно осознавать, что в твоём боте распространяют педофилию.Навсегда? Возможно.\" – Blessed!! [3 января 2025]",
        "Дата смерти": "13 августа 2024, 14 ноября 2024, 3 января 2025",
        "Владелец": "Blessed!! id6440397991",
        "Функционал (команды)": "Пустая ячейка",
        "Кол-во юзеров": "Пустая ячейка",
        "Статус": "Временно отключен",
        "Каналы Ботов": "https://t.me/GayAnonEcho_XXX",
        "Сурсы": "Блесс утверждает, что использует собственные сурсы, однако он позаимствовал их из Эхокима и полностью переделал. Этих сурсов эхокима нету, они очень древние",
        "Айди": 6888864677
    },
    {
        "Бот": {
            "text": "Зоряна - Київстар [ЗЕРКАЛО]",
            "link": "https://drive.google.com/u/0/drive-viewer/AKGpihaHJjgHtQnL8hSgRG6dIkQYyw4r6cLwp51C4QqyAEcjpvZTbxIAyEMazVKgXXpQpRX0Nr6I1rdn0HsxVUt7y2WZns-bk7KWp48=s1600-rw-v1",
            "image_path": "None"
        },
        "Нынешний юз": "@Zoriana_Kylvstar_Bot",
        "Первый запуск": "5 ноября 2024",
        "Второй запуск": "-",
        "Старый юз": "@Zorlana_Kyivstar_Bot",
        "Кд": "2 секунды",
        "Примечания": "\"Возможно временно, создана (копия) Зоряны Стоит отметить, бот находится на serv00 (free-hosting), поэтому за целостность базы данных не ручаюсь, поэтому бот будет жить даже после смерти актуальной Зоряны — @Zoriana_Kylvstar_Bot Это конкретно не переезд, возможно вам поможет.\" – Blessed!!",
        "Дата смерти": "",
        "Владелец": "Blessed!! id6440397991",
        "Функционал (команды)": "Пустая ячейка",
        "Кол-во юзеров": "Пустая ячейка",
        "Статус": "Работает с перебоями",
        "Каналы Ботов": "https://t.me/GayAnonEcho_XXX",
        "Сурсы": "Блесс утверждает, что использует собственные сурсы, однако он позаимствовал их из Эхокима и полностью переделал. Этих сурсов эхокима нету, они очень древние",
        "Айди": 7459295805
    },
    {
        "Бот": {
            "text": "ECHO ROOM [BETA]",
            "link": "https://drive.google.com/u/0/drive-viewer/AKGpihbNhwXm8ylBzy-2OpbW-eF_8R2ft5ZVwLwN-bWfQuoqc2bRN8xRjaqnatY2Q4Mlxh7RghGfOvIAEcoJzme5NLeCOaUiboPsFkc=s1600-rw-v1",
            "image_path": " webapp\\images\\image_20_1NI_YZyRcBCVB_fl-Fn495spLR_CLk_3L.jpg"
        },
        "Нынешний юз": "@echoroombot",
        "Первый запуск": "26 мая 2024",
        "Второй запуск": "-",
        "Старый юз": "-",
        "Кд": "-",
        "Примечания": "*Можно кстати было в другие комнаты как то писать по частотам* – Аноним",
        "Дата смерти": "10 июня 2024",
        "Владелец": "lord ?",
        "Функционал (команды)": "Пустая ячейка",
        "Кол-во юзеров": "Пустая ячейка",
        "Статус": "Не работает",
        "Каналы Ботов": "https://t.me/tonfsociety",
        "Сурсы": "Свои",
        "Айди": 7133491097
    },
    {
        "Бот": {
            "text": "MASS Echo [No Rules]",
            "link": "https://drive.google.com/u/0/drive-viewer/AKGpihbQoRQB10ns90po1knaQhM5wPmukI3lXKMlJKfYZ49uObS0Vz79t2V_FDR6GPVpNLVO0Ur1hkPNz9thW72R2OfoBL4NLgeky1Q=s1600-rw-v1",
            "image_path": " webapp\\images\\image_21_1q8Cz4etojQabUpDCmDzOCvidi4bnK-Rm.jpg"
        },
        "Нынешний юз": "@MassEcho_bot",
        "Первый запуск": "29 мая 2024",
        "Второй запуск": "16 июня 2024, 17 ноября 2024",
        "Старый юз": "-",
        "Кд": "3 секунды",
        "Примечания": "Бот умер в один день, но был восстановлен сразу после.",
        "Дата смерти": "12 августа 2024",
        "Владелец": "Garfy tar -xf tsetup.5.2.3.tar.xz 🦶 id7062635655",
        "Функционал (команды)": "Пустая ячейка",
        "Кол-во юзеров": "Пустая ячейка",
        "Статус": "Временно отключен",
        "Каналы Ботов": "https://t.me/MassCommunityy",
        "Сурсы": "https://github.com/tarxzf/echotoallbot",
        "Айди": 7441437502
    },
    {
        "Бот": {
            "text": "РейнЭхо",
            "link": "https://drive.google.com/u/0/drive-viewer/AKGpihY2ol3hvySfS1tFvUOPAy0Qe6D0mWdPakJMSs4LarXkXDFkqjCfWn6A9A1RVrP6DIvAokRNtZ_WV3UC0a4sHI7sDyQzjJUzOw=s1600-rw-v1",
            "image_path": ""
        },
        "Нынешний юз": "@EchoRhine_bot",
        "Первый запуск": "9 декабря 2023",
        "Второй запуск": "-",
        "Старый юз": "-",
        "Кд": "-",
        "Примечания": "\"/start был прописан 9 декабря, и до 21 декабря ничего абсолютно не происходило\" – ауссоис Умер в день запуска. причина неизвестна",
        "Дата смерти": "21 декабря 2023",
        "Владелец": "ауссоис [соус , соус барбекю , asocitality]",
        "Функционал (команды)": "Пустая ячейка",
        "Кол-во юзеров": "Пустая ячейка",
        "Статус": "Не работает",
        "Каналы Ботов": "https://t.me/AssEcho",
        "Сурсы": "Свои написанные ии. или чужие",
        "Айди": 6716765894
    },
    {
        "Бот": {
            "text": "EchoIrina",
            "link": "https://drive.google.com/u/0/drive-viewer/AKGpihbXwJvkR7Gcu5Ew5Cr6r6v3gJTAJBLoC0DI8LC97L6qZM7IUE6AoPp4-kzVoonEmZHoUdGGhkOz2NzTMAINxsef3BDRL98m95g=s1600-rw-v1",
            "image_path": ""
        },
        "Нынешний юз": "@EchoIrina_bot",
        "Первый запуск": "октябрь 2024",
        "Второй запуск": "-",
        "Старый юз": "-",
        "Кд": "-",
        "Примечания": "\"в эхо ирине заспамили гей п*рно потом бота снесло\" – Аноним",
        "Дата смерти": "",
        "Владелец": "ауссоис [соус , соус барбекю , asocitality]",
        "Функционал (команды)": "Пустая ячейка",
        "Кол-во юзеров": "Пустая ячейка",
        "Статус": "Снесён",
        "Каналы Ботов": "https://t.me/AssEcho",
        "Сурсы": "Свои написанные ии. или чужие",
        "Айди": "-"
    },
    {
        "Бот": {
            "text": "EchoIrina",
            "link": "https://drive.google.com/u/0/drive-viewer/AKGpihb4ksUH651Ds5PDJcrjd5I0qfBIkNJUCr5mBisuWEl7CJpTH9JLJ3jVbMIpTCHkHoKUHsx0bK1FDpgyQQwvlbAOttXEaPBKRM4=s1600-rw-v1",
            "image_path": " webapp\\images\\image_24_1-l9049sK7rp7x-ZqEv-Tv93G-ggQWhhb.jpg"
        },
        "Нынешний юз": "@IrinaEcho_bot",
        "Первый запуск": "4 ноября 2024",
        "Второй запуск": "-",
        "Старый юз": "-",
        "Кд": "0 секунд",
        "Примечания": "Да, бот прожил 1 день",
        "Дата смерти": "5 ноября",
        "Владелец": "ауссоис [соус , соус барбекю , asocitality]",
        "Функционал (команды)": "Пустая ячейка",
        "Кол-во юзеров": "Пустая ячейка",
        "Статус": "Не работает",
        "Каналы Ботов": "https://t.me/AssEcho",
        "Сурсы": "Свои написанные ии. или чужие",
        "Айди": 6789752959
    },
    {
        "Бот": {
            "text": "AssEcho [MAIN] - удалён",
            "link": "https://drive.google.com/u/0/drive-viewer/AKGpihZ8em6s-isxPbA7Vzd3YCweaMMvCsLXZ84g_59Xe4EefCvx62l3UGRWHLfhWM63XLUp86QuNTzFcLKTPs5yBvtJaLpmthFP7IQ=s1600-rw-v1",
            "image_path": ""
        },
        "Нынешний юз": "Бот удалён",
        "Первый запуск": "23 мая 2024",
        "Второй запуск": "13 июня 2024",
        "Старый юз": "-",
        "Кд": "3 секунды",
        "Примечания": "\"удалил его, потому что психанул сильно из за \"докса\", успокоился, и решил сделать реборн @AssEcho_bot\" – ауссоис \"Соус пед*фил\" – Аноним",
        "Дата смерти": "29 мая 2024 22 июля 2024",
        "Владелец": "ауссоис [соус , соус барбекю , asocitality]",
        "Функционал (команды)": "Пустая ячейка",
        "Кол-во юзеров": "Пустая ячейка",
        "Статус": "Снесён",
        "Каналы Ботов": "https://t.me/AssEcho",
        "Сурсы": "Свои написанные ии. или чужие",
        "Айди": "-"
    },
    {
        "Бот": {
            "text": "AssEcho [MAIN]",
            "link": "https://drive.google.com/u/0/drive-viewer/AKGpihZ8em6s-isxPbA7Vzd3YCweaMMvCsLXZ84g_59Xe4EefCvx62l3UGRWHLfhWM63XLUp86QuNTzFcLKTPs5yBvtJaLpmthFP7IQ=s1600-rw-v1",
            "image_path": ""
        },
        "Нынешний юз": "@AssEcho_bot",
        "Первый запуск": "13 июня 2024",
        "Второй запуск": "-",
        "Старый юз": "-",
        "Кд": "3 секунды",
        "Примечания": "я принял(скорее всего не окончательное) решение, закрыть ботов. почему? в ботах нет актива, актив строится на том, что мне ебут мозги вопросом \"зачем брата ебал?\" – @AssEcho [8 июля 2024] Бот окончательно выключен. Я покидаю ECHO комьюнити. -Почему? На то есть свои причины, но раскрою только: Неадекватное комьюнити, пропал актив во всех эхо ботах. не вижу смысла держать ноут включённым 24 часа в сутки ради 3х сообщений в день. Всем удачи. – @AssEcho [22 июля 2024] Всё, если что, буду чет писать в https://t.me/backroomalley, https://t.me/aussoisofftop А щас, эхо мои выключаются, я буду придумывать новые ненужные проектв – asociallity [17 августа 2024]",
        "Дата смерти": "22 июля 2024",
        "Владелец": "ауссоис [соус , соус барбекю , asocitality]",
        "Функционал (команды)": "Пустая ячейка",
        "Кол-во юзеров": "Пустая ячейка",
        "Статус": "Не работает",
        "Каналы Ботов": "https://t.me/AssEcho",
        "Сурсы": "Свои написанные ии. или чужие",
        "Айди": 7348517743
    },
    {
        "Бот": {
            "text": "NoRules Echo",
            "link": "https://drive.google.com/u/0/drive-viewer/AKGpihZHQ7faTzxiS1MGltRPmMZ9E6KdW0M6cqEtC33wYxmzop94igTXDhq6gCesE0O4bHSFsbb5ze9MPD80nV2ouciNpIoUl8IPeL0=s1600-rw-v1",
            "image_path": ""
        },
        "Нынешний юз": "@NoRulesEcho_bot",
        "Первый запуск": "15 июня 2024",
        "Второй запуск": "-",
        "Старый юз": "-",
        "Кд": "2 секунды",
        "Примечания": "",
        "Дата смерти": "8 июля 2024 22 июля 2024 17 августа 2024",
        "Владелец": "ауссоис [соус , соус барбекю , asocitality]",
        "Функционал (команды)": "Пустая ячейка",
        "Кол-во юзеров": "Пустая ячейка",
        "Статус": "Не работает",
        "Каналы Ботов": "https://t.me/AssEcho",
        "Сурсы": "Свои написанные ии. или чужие",
        "Айди": 7261808268
    },
    {
        "Бот": {
            "text": "RhineEcho",
            "link": "https://drive.google.com/u/0/drive-viewer/AKGpihaEbzJXhZug3LqT5JEP9i7yQCSjHCUMQZFU2qxZHFJ6UBn89tKyie5QmhDfO9ZupbCDx-G9ZIL00k9F2lzeaHuieAjDmOJ414U=s1600-rw-v1",
            "image_path": ""
        },
        "Нынешний юз": "@rhineecho_bot",
        "Первый запуск": "ноябрь 2023",
        "Второй запуск": "-",
        "Старый юз": "-",
        "Кд": "5 секунд",
        "Примечания": "\" (бот) снесся вместе с акком\" – ауссоис",
        "Дата смерти": "январь 2024",
        "Владелец": "ауссоис [соус , соус барбекю , asocitality]",
        "Функционал (команды)": "Пустая ячейка",
        "Кол-во юзеров": "Пустая ячейка",
        "Статус": "Снесён",
        "Каналы Ботов": "https://t.me/AssEcho",
        "Сурсы": "Свои написанные ии. или чужие",
        "Айди": "-"
    },
    {
        "Бот": {
            "text": "Lifecell Echo",
            "link": "https://drive.google.com/u/0/drive-viewer/AKGpihbU-N7cGU6gCxVJoywEDnMlgSYrnOiMz9FH4xD30lf5MkyNYnBMHLUKXcuNY-NGpfzCGXeisEhnINaRUYndp7Qda9tG5Qm8aqM=s1600-rw-v1",
            "image_path": ""
        },
        "Нынешний юз": "@lifecellukrainebot",
        "Первый запуск": "24 декабря 2024",
        "Второй запуск": "-",
        "Старый юз": "-",
        "Кд": "2 секунды",
        "Примечания": "",
        "Дата смерти": "-",
        "Владелец": "ауссоис [соус , соус барбекю , asocitality]",
        "Функционал (команды)": "Пустая ячейка",
        "Кол-во юзеров": "Пустая ячейка",
        "Статус": "Временно отключен",
        "Каналы Ботов": "https://t.me/lifecellecho",
        "Сурсы": "Эхо ким(https://github.com/tarxzf/echotoallbot) + Свои",
        "Айди": 7768915804
    },
    {
        "Бот": {
            "text": "ECHO - НАСРАЛ | #NORULES 1",
            "link": "https://drive.google.com/u/0/drive-viewer/AKGpihaNo-Gc-ZutC88stC1Sbpt5-uETsp2QM6rLxkpZBDG6G2JnlYBEeG5on8yCma07q5LIII3lvq-x_XSv6Ve-l1S0fg7Z0-tgfFk=s1600-rw-v1",
            "image_path": ""
        },
        "Нынешний юз": "@echonasral_bot",
        "Первый запуск": "11 августа 2024",
        "Второй запуск": "12 августа 2024",
        "Старый юз": "-",
        "Кд": "10 секунд",
        "Примечания": "\"@echonasral_bot - копия Dragon EA без правил!\" – Dragon EA | DEV Альтернатива по просьбе блесса, создан на базе г идры/драгон бота, но не имеет фильтров (кроме капчи)",
        "Дата смерти": "12 августа",
        "Владелец": "кугона id5715731957",
        "Функционал (команды)": "Пустая ячейка",
        "Кол-во юзеров": "Пустая ячейка",
        "Статус": "Снесён",
        "Каналы Ботов": "https://t.me/dragon_echo_all",
        "Сурсы": "Свои",
        "Айди": 7487176708
    },
    {
        "Бот": {
            "text": "ECHO - НАСРАЛ | #NORULES 2",
            "link": "https://drive.google.com/u/0/drive-viewer/AKGpihYDZVErZffhve0owZ7dG6Ji1o0HtChgXb3uGEV_exjJss4Kav5PWF9wVCosu2H1KijFjZVNZ9EyWixIgAk-9BnpZNXNjwGDMOI=s1600-rw-v1",
            "image_path": ""
        },
        "Нынешний юз": "@echonasraltwo_bot",
        "Первый запуск": "12 августа 2024 13:40",
        "Второй запуск": "12 августа 2024 22:10",
        "Старый юз": "@echonasral_bot",
        "Кд": "3 секунды",
        "Примечания": "\" Бот заблокирован. В течение недели появится 2-ая копия «ЭХО НАСРАЛ» \" – Dragon EA | DEV",
        "Дата смерти": "12 августа 2024 22:05",
        "Владелец": "кугона id5715731957",
        "Функционал (команды)": "Пустая ячейка",
        "Кол-во юзеров": "Пустая ячейка",
        "Статус": "Снесён",
        "Каналы Ботов": "",
        "Сурсы": "Свои",
        "Айди": 7377453406
    },
    {
        "Бот": {
            "text": "ECHO - НАСРАЛ | #NORULES 3",
            "link": "https://drive.google.com/u/0/drive-viewer/AKGpihZG4WjV1b5Q7iUif0a9gC51r19PnJkuGMilqnntnlk6MZG36pQ3uYFFO0xoQuqRm1lyZR90Ovun0DQ9NOKYKKc-I_Lt1CPjhJI=s1600-rw-v1",
            "image_path": ""
        },
        "Нынешний юз": "@echonasral3_bot",
        "Первый запуск": "12 августа 2024 22:10",
        "Второй запуск": "-",
        "Старый юз": "@echonasraltwo_bot",
        "Кд": "3 секунды",
        "Примечания": "",
        "Дата смерти": "4 сентября",
        "Владелец": "кугона id5715731957",
        "Функционал (команды)": "Пустая ячейка",
        "Кол-во юзеров": "Пустая ячейка",
        "Статус": "Не работает",
        "Каналы Ботов": "https://t.me/dragon_echo_all",
        "Сурсы": "Свои",
        "Айди": 7493160591
    },
    {
        "Бот": {
            "text": "Rase EA",
            "link": "https://drive.google.com/u/0/drive-viewer/AKGpihbXiD9W1ec5LteOF7DyGzOFQcrrY56rQUvfSnzkZVDC-lay-N5J9c2s-SyONJfALUBrN9bGmpzWKRalK-YvRtwZHNiWHHFDzGg=s1600-rw-v1",
            "image_path": ""
        },
        "Нынешний юз": "@raseechoall_bot",
        "Первый запуск": "26 августа 2024",
        "Второй запуск": "-",
        "Старый юз": "-",
        "Кд": "0.5 секунд",
        "Примечания": "",
        "Дата смерти": "-",
        "Владелец": "🔥VAnulkin🔥 #java_develop id5702630185",
        "Функционал (команды)": "Пустая ячейка",
        "Кол-во юзеров": "Пустая ячейка",
        "Статус": "Не работает",
        "Каналы Ботов": "-",
        "Сурсы": "Свои",
        "Айди": 7066970856
    },
    {
        "Бот": {
            "text": "P*nisDestroyer [TEST] Echo",
            "link": "https://drive.google.com/u/0/drive-viewer/AKGpihbH_FxlU5V79ehW6SZVK6urZvX71Q4ji5irVN80mViCAJ1FR74kN5fbrdzZpDNl8c1x08MTPykB0AxKNc1wvL4leKPJCqUXssc=s1600-rw-v1",
            "image_path": ""
        },
        "Нынешний юз": "@PenisDestroyerRobot",
        "Первый запуск": "4 сентября 2024",
        "Второй запуск": "-",
        "Старый юз": "-",
        "Кд": "0 секунд анти-спам система",
        "Примечания": {
            "text": "\"4 сентября первый тест капчи был,там она голая была, щас может найду\" *фото* – 🍺 Баклаха",
            "link": "https://drive.google.com/u/0/drive-viewer/AKGpihYqNPH9lzD_grYcHTT6W4Zxe4N-AHYl2cBa5RP0XFN5xXtQHn9pQ5P8UTkZMIVDPS2OlSnRWRubFvmQr5l_h48sfrobIGA4DFI=s2560",
            "image_path": " webapp\\images\\image_34_1dNpEkiAtjzvGMFoCdJ8bGncRdbqa4TB5.jpg"
        },
        "Дата смерти": "-",
        "Владелец": "🍺 Баклаха id8033731524",
        "Функционал (команды)": "Пустая ячейка",
        "Кол-во юзеров": "Пустая ячейка",
        "Статус": "Временно отключен",
        "Каналы Ботов": "утерян.",
        "Сурсы": "Свои",
        "Айди": 7533028817
    },
    {
        "Бот": {
            "text": "EchoPines",
            "link": "https://drive.google.com/u/0/drive-viewer/AKGpihY5nv3iROwASm3XT9PNROn_a1veWK1Uo9PjGYWQ9Hr0e1yvrRwZ_JJ33W7MBGGtc0GGMV4u7EdfUzxZ8YwY0fYqQ4jcYXlnl9E=s1600-rw-v1",
            "image_path": ""
        },
        "Нынешний юз": "@PenisEcho_bot",
        "Первый запуск": "28 августа 2024",
        "Второй запуск": "-",
        "Старый юз": "-",
        "Кд": "3 секунды",
        "Примечания": "\"п*нис эхо это же бот соуса\" – Claym \"когда п\"нис эхо появился,то соус в зоряне активничать стал\" – 🍺 Баклаха",
        "Дата смерти": "-",
        "Владелец": "п*нис (возможно соус) d3velo / соус id6967004268",
        "Функционал (команды)": "Пустая ячейка",
        "Кол-во юзеров": "Пустая ячейка",
        "Статус": "Не работает",
        "Каналы Ботов": "https://t.me/PenisEcho",
        "Сурсы": "Нейронка",
        "Айди": 8113587776
    },
    {
        "Бот": {
            "text": "EchoBal",
            "link": "https://drive.google.com/u/0/drive-viewer/AKGpihbdJwx1kT6Rrc8JmZG6FKGSrSYKePtDxRvz2nDC1iZmUhiGL0_uDYsYeY9RkhAqdtydPK7cfFxQ8q3oMnFUAWgUZaEnG8O4Q4I=s1600-rw-v1",
            "image_path": ""
        },
        "Нынешний юз": "@EchoBalBot",
        "Первый запуск": "май 2024",
        "Второй запуск": "-",
        "Старый юз": "-",
        "Кд": "0 секунд",
        "Примечания": "-Зачем бота создал -Ну может потролится – hewin",
        "Дата смерти": "-",
        "Владелец": "hewin id6562216884",
        "Функционал (команды)": "Пустая ячейка",
        "Кол-во юзеров": "Пустая ячейка",
        "Статус": "Работает",
        "Каналы Ботов": "https://t.me/infenixchat",
        "Сурсы": "ждем",
        "Айди": 7067807588
    },
    {
        "Бот": {
            "text": "Секретный чат",
            "link": "https://drive.google.com/u/0/drive-viewer/AKGpihYfuQXok72hfrOtY4-dS_Nlmrp0DTb-gMo7o1_Zdv2Mqpu9bJAgik9xmEOzJA3hfbPGcPrHlnFx_J_yx6fatMtYlSMNhLhBlww=s1600-rw-v1",
            "image_path": ""
        },
        "Нынешний юз": "@SecretEchoBalBot",
        "Первый запуск": "19 октября 2024",
        "Второй запуск": "-",
        "Старый юз": "-",
        "Кд": "0 секунд",
        "Примечания": "\"Начал пробовать создавать аналАгичный бот чат. Залетайте\" – hewin",
        "Дата смерти": "-",
        "Владелец": "hewin id6562216884",
        "Функционал (команды)": "Пустая ячейка",
        "Кол-во юзеров": "Пустая ячейка",
        "Статус": "Не работает",
        "Каналы Ботов": "https://t.me/infenixchat",
        "Сурсы": "ждем",
        "Айди": 7884459903
    },
    {
        "Бот": {
            "text": "EchoToAll",
            "link": "https://drive.google.com/u/0/drive-viewer/AKGpiha_sIS7ZetivgcIjCftZKpL7ARIqCQ1DzxSRF9Yv0Ch7EsrRshffXZ5zPG8PBNbeU1l8YNWZQPY876Gk4fY57XqhNnshbZ2q4g=s1600-rw-v1",
            "image_path": ""
        },
        "Нынешний юз": "?",
        "Первый запуск": "?",
        "Второй запуск": "-",
        "Старый юз": "-",
        "Кд": "3 секунды",
        "Примечания": "У Марка было 2-3 бота информация про них утеряна.",
        "Дата смерти": "??",
        "Владелец": "mark",
        "Функционал (команды)": "Пустая ячейка",
        "Кол-во юзеров": "Пустая ячейка",
        "Статус": "Снесён",
        "Каналы Ботов": "-",
        "Сурсы": "Свои",
        "Айди": "-"
    },
    {
        "Бот": {
            "text": "Echo All",
            "link": "https://drive.google.com/u/0/drive-viewer/AKGpihYe3zTiONuXneWNxtRBzk5WaXe8ko2Hz5giJBQQ16FsNemKFz1EPkKxOyTiDJ_U2eBiu6eAl_q9bXbfr4VcHS7JOmUmGm42uww=s1600-rw-v1",
            "image_path": ""
        },
        "Нынешний юз": "@ekhoallbott",
        "Первый запуск": "1 декабря 2024",
        "Второй запуск": "-",
        "Старый юз": "-",
        "Кд": "13 секунд",
        "Примечания": "Админ Echo All изначально высказался против пользователей Зоряны, что вызвало неприязнь к его боту. Пользователи посчитали его неудобным и слишком строгим, так как привыкли к анархии и ботам без ограничений.",
        "Дата смерти": "-",
        "Владелец": "Я думал, ты хотела в сказку.. id7827802903",
        "Функционал (команды)": "Пустая ячейка",
        "Кол-во юзеров": "Пустая ячейка",
        "Статус": "Работает",
        "Каналы Ботов": "https://t.me/ekhoall",
        "Сурсы": "Свои",
        "Айди": 7833796374
    }
]

@dataclass
class Bot:
    name: str
    image_url: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    raw_data: Dict[str, Any] = None

    @classmethod
    def from_json(cls, data: Dict[str, Any]) -> 'Bot':
        bot_info = data.get('Бот', {})
        if isinstance(bot_info, dict):
            # На всякий случай проверка link
            image_url = bot_info.get('link')
            if image_url and not image_url.startswith(('http://', 'https://')):
                image_url = None 
                
            return cls(
                name=bot_info.get('text', 'Unknown'),
                image_url=image_url,
                description=bot_info.get('text'),
                status=data.get('Статус'),
                raw_data=data
            )
        return cls(
            name=str(bot_info),
            description=str(bot_info),
            status=data.get('Статус'),
            raw_data=data
        )

class BotCatalog:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Каталог ботов"
        self.page.theme_mode = ft.ThemeMode.SYSTEM
        self.page.padding = 20
        self.bots = []
        self.filtered_bots = []
        self.selected_status = None

        # Тема
        def change_theme(e):
            """Смена темы"""
            page.theme_mode = 'light' if page.theme_mode == 'dark' else 'dark'
            page.update()
            e.control.selected = not e.control.selected
            e.control.update()
        theme = ft.IconButton(
            icon=ft.Icons.SUNNY,
            selected_icon=ft.Icons.WB_SUNNY_OUTLINED,
            on_click=change_theme,
            selected=False,
            tooltip='Сменить тему')
        
        # Поле поиска        
        search = ft.TextField(
            label="Поиск ботов",
            prefix_icon=ft.Icons.SEARCH,
            on_change=self.filter_bots,
            expand=False)
        self.search_field = search # Это не обязятельно, но мне так удобнее
        self.search_theme = ft.Row([search, theme])

        # Container для фильтров статуса
        self.status_filters = ft.Container(
            content=ft.Row(
                controls=[],
                spacing=10,
                wrap=True,
                scroll=ft.ScrollMode.AUTO
            ),
            height=35,  # Установите фиксированную высоту
            margin=ft.margin.only(top=10, bottom=10)
        )

        # Сетка для отображения ботов
        self.grid_view = ft.GridView(
            expand=True,
            runs_count=3,
            max_extent=300,
            spacing=20,
            run_spacing=20,
            clip_behavior=ft.ClipBehavior.HARD_EDGE
        )

        # Компоновка элементов через Column
        self.page.add(
            ft.Column(
                [
                    self.search_theme,
                    self.status_filters,
                    self.grid_view
                ],
                expand=True
            )
        )

        # Загрузка данных
        self.load_data()

    # Создание фильра по статусам
    def create_status_filters(self, statuses: set[str]):
        """Создание фильра по статусам"""
        status_row = self.status_filters.content
        status_row.controls.clear()
        
        # Кнопка "Все"
        all_button = ft.ElevatedButton(
            text="Все боты",
            on_click=lambda e: self.update_status_filter(None, e.control),
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=8),
                bgcolor=ft.Colors.BLUE,
                color=ft.Colors.WHITE,
            ),
        )
        status_row.controls.append(all_button)
        
        # Кнопки для каждого статуса
        for status in sorted(statuses):
            if status and status != "Пустая ячейка":
                button = ft.ElevatedButton(
                    text=status,
                    on_click=lambda e, s=status: self.update_status_filter(s, e.control),
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=8),
                        bgcolor=ft.Colors.BLUE_100,
                        color=ft.Colors.BLACK,
                    ),
                )
                status_row.controls.append(button)
        
        self.page.update()

    # Переключение кнопок статуса
    def update_status_filter(self, status: Optional[str], clicked_button: ft.ElevatedButton):
        """Переключение кнопок фильтра по статусу"""
        self.selected_status = status
        
        # Обновляем внешний вид кнопок
        for button in self.status_filters.content.controls:
            if button == clicked_button:
                button.style.bgcolor = ft.Colors.BLUE
                button.style.color = ft.Colors.WHITE
            else:
                button.style.bgcolor = ft.Colors.BLUE_100
                button.style.color = ft.Colors.BLACK
            button.update()
        
        self.apply_filters()

    def apply_filters(self):
        search_query = self.search_field.value.lower() if self.search_field.value else ""
        
        # Применяем оба фильтра
        self.filtered_bots = [
            bot for bot in self.bots
            if (not search_query or 
                search_query in bot.name.lower() or 
                (bot.description and search_query in bot.description.lower())) and
            (not self.selected_status or bot.status == self.selected_status)
        ]
        self.update_grid()
        # Показываем количество найденных ботов
        total = len(self.filtered_bots)
        snack = ft.SnackBar(
            content=ft.Text(f"Найдено ботов: {total}"),
            show_close_icon=True,
            duration=300)
        self.page.overlay.append(snack)
        snack.open = True
        self.page.update()

    def filter_bots(self, e):
        self.apply_filters()

    # Загрузка данных
    def load_data(self):
        try:            
            self.bots = [Bot.from_json(item) for item in DATA]
            self.filtered_bots = self.bots.copy()
            self.update_grid()
            
            # Получаем уникальные статусы
            statuses = {bot.status for bot in self.bots if bot.status and bot.status != "Пустая ячейка"}
            self.create_status_filters(statuses)
            
            # Уведомление о загрузке ботов
            snack = ft.SnackBar(content=ft.Text(f"Успешно загружено {len(self.bots)} ботов"), show_close_icon=True, duration=200)
            self.page.overlay.append(snack)
            snack.open = True
            self.page.update()
            
        except Exception as ex:
            print(f"Ошибка при загрузке файла: {ex}")
            snack = ft.SnackBar(content=ft.Text(f"Ошибка при загрузке файла: {str(ex)}"), show_close_icon=True)
            self.page.overlay.append(snack)
            snack.open = True
            self.page.update()

    # Фильтр через поиск
    def filter_bots(self, e):
        query = self.search_field.value.lower()
        self.filtered_bots = [
            bot for bot in self.bots
            if query in bot.name.lower() or
               (bot.description and query in bot.description.lower())
        ]
        self.update_grid()

    # Создание карточки бота
    def create_bot_card(self, bot: Bot) -> ft.Card:
        return ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.Container(
                            content=ft.Image(
                                src=bot.image_url,
                                fit=ft.ImageFit.CONTAIN,
                                width=200,
                                height=300,
                                filter_quality=ft.FilterQuality.HIGH
                            ) if bot.image_url else ft.Icon(
                                name=ft.Icons.PERSON,
                                size=64,
                                color=ft.Colors.BLUE_400,
                            ),
                            alignment=ft.alignment.center,
                            height=200,
                        ),
                        ft.Container(
                            content=ft.Text(
                                bot.name,
                                size=16,
                                weight=ft.FontWeight.W_500,
                                text_align=ft.TextAlign.CENTER,
                            ),
                            padding=10,
                        ),
                    ],
                    spacing=5,
                ),
                on_click=lambda e: self.show_bot_details(bot),
            ),
        )

    # Обновление сетки карточек
    def update_grid(self):
        self.grid_view.controls = [
            self.create_bot_card(bot)
            for bot in self.filtered_bots
        ]
        self.page.update()

    # Отрытие карточки
    def show_bot_details(self, bot: Bot):
        details = []
        raw_data = bot.raw_data
        bot.image_url

        # Добавляем поля с возможностью копирования
        for key in ['Нынешний юз', 'Старый юз', 'Айди']:
            value = str(raw_data.get(key, '-'))
            if value not in ['-', '']:
                details.append(
                    ft.Row([
                        ft.Text(f"{key}: {value}", selectable=True),
                        ft.IconButton(
                            ft.icons.COPY,
                            on_click=lambda e, v=value: self.copy_to_clipboard(v)
                        )
                    ])
                )

        # Остальные поля
        for key in ['Первый запуск', 'Второй запуск', 'Дата смерти', 'Владелец', 'Статус', 'Айди']:
            value = str(raw_data.get(key, '-'))
            details.append(
                ft.Text(
                    f"{key}: {value}",
                    selectable=True
                    )
                )

        # Обработка каналов и сурсов
        for key in ['Каналы Ботов', 'Сурсы']:
            value = raw_data.get(key, '-')
            
            if isinstance(value, dict):
                # Если значение - словарь с текстом и ссылкой
                link = value.get('link')
                if link and (link.startswith('http://') or link.startswith('https://')):
                    details.append(
                        ft.TextButton(
                            text=key,
                            url=link,
                            on_click=lambda e, url=link: self.page.launch_url(url)
                        )
                    )
                else:
                    details.append(ft.Text(f"{key}: {value.get('text', '-')}", selectable=True))
            elif isinstance(value, str):
                # Если значение - строка
                if value.startswith(('http://', 'https://')):
                    details.append(
                        ft.TextButton(
                            text=key,
                            url=value,
                            on_click=lambda e, url=value: self.page.launch_url(url)
                        )
                    )
                else:
                    details.append(ft.Text(f"{key}: {value}", selectable=True))
        
        # Кд
        cooldown = raw_data.get('Кд', None)
        if cooldown:
            details.append(ft.Text("Кд:", weight=ft.FontWeight.BOLD))

            if isinstance(cooldown, dict):  # Если Кд содержит текст и другие данные
                text = cooldown.get('text', None)
                link = cooldown.get('link', None)
                # Отображение текста
                if text:
                    details.append(ft.Text(text, selectable=True))
                # Отображение изображения
                if link:
                    details.append(
                        ft.Container(
                            content=ft.Image(
                                src=link,
                                fit=ft.ImageFit.CONTAIN,
                                filter_quality=ft.FilterQuality.HIGH,
                                width=400,   # Можно убрать - последствия ниже
                                height=500,  # https://flet.dev/docs/controls/image/#height
                            ),
                            alignment=ft.alignment.center, 
                        )
                    )
            else:  # Если Кд — это просто строка
                details.append(ft.Text(cooldown, selectable=True))                

        # Обработка примечаний
        notes = raw_data.get('Примечания', None)
        if notes:
            details.append(ft.Text("Примечания:", weight=ft.FontWeight.BOLD))

            if isinstance(notes, dict):  # Если примечания содержат текст и другие данные
                text = notes.get('text', None)
                link = notes.get('link', None)
                # Отображение текста
                if text:
                    details.append(ft.Text(text, selectable=True))
                # Отображение изображения
                if link and (link.startswith('http://') or link.startswith('https://')):
                    details.append(
                        ft.Image(src=link)
                    )
            else:  # Если примечания — это просто строка
                details.append(ft.Text(notes, selectable=True))
                # details.append(ft.Text('Картинки нет', selectable=True, color=ft.Colors.RED_400))
        
        # ALertDialog для отображения
        dialog = ft.AlertDialog(
            title=ft.Text(bot.name),
            content=ft.Column(details, scroll=ft.ScrollMode.AUTO),
            actions=[
                ft.TextButton("Закрыть", on_click=lambda e: self.close_dialog(dialog))
            ],
        )
        self.page.overlay.append(dialog)
        dialog.open = True
        self.page.update()

    # Копирование
    def copy_to_clipboard(self, text):
        self.page.set_clipboard(text)
        snack = ft.SnackBar(content=ft.Text("Скопировано в буфер обмена"), show_close_icon=True, duration=300)
        self.page.overlay.append(snack)
        snack.open = True
        self.page.update()

    # Закрыть AlertDialog
    def close_dialog(self, dialog):
        dialog.open = False
        self.page.update()
        

def main(page: ft.Page):
    BotCatalog(page)

if __name__ == "__main__":
    ft.app(target=main, view=ft.WEB_BROWSER, port=int(os.getenv("PORT", 5000)))