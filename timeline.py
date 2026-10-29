import json, html, os
base = "https://tokishu.lazurite.cc"
E = html.escape
GH = "https://github.com/Tok1shu/"
# (date, title_en, title_ru, text_en, text_ru, repo or None)
EV = [
("", "Interest in computers", "Интерес к компьютерам", "Interested in computers since childhood.", "С детства интересовался компьютерами.", None),
("2019", "First programming courses", "Первые курсы программирования", "Introductory programming courses for children at ITSTEP in Odesa.", "Детские курсы по вводу в программирование в ITSTEP в Одессе.", None),
("2022-08", "First experience with code: PHP", "Первый опыт программирования: PHP", "The first repository is created on GitHub (account Tok1shu), and with it the first real programming experience, in PHP.", "Создан первый репозиторий на GitHub (аккаунт Tok1shu) и вместе с ним первый настоящий опыт программирования, на PHP.", None),
("2023-01", "First public project", "Первый публичный проект", "easydonate-ru-create-pay, a small PHP project for creating payments.", "easydonate-ru-create-pay, небольшой проект на PHP для создания платежей.", "easydonate-ru-create-pay"),
("2023-11", "First Java", "Первая Java", "MultiSignBook is the first public repository in Java.", "MultiSignBook, первый публичный репозиторий на Java.", "MultiSignBook"),
("2023-12", "Python scripts and bots", "Скрипты и боты на Python", "DiscordUserAPI, then YTMLikedSongsToPlaylist (2024) and telegram-bot-manager (2025): small Python tools around Discord, YouTube Music and Telegram.", "DiscordUserAPI, затем YTMLikedSongsToPlaylist (2024) и telegram-bot-manager (2025): небольшие инструменты на Python вокруг Discord, YouTube Music и Telegram.", "DiscordUserAPI"),
("2025-03", "ObsidianGate", "ObsidianGate", "A Java project, later archived.", "Проект на Java, позже заархивирован.", "ObsidianGate"),
("2025-04", "Commissioned work for FluffyRP", "Заказ на FluffyRP", "Development work on commission for FluffyRP begins, with a dedicated team organization on GitHub.", "Начало разработки на заказ для FluffyRP: появляется отдельная организация на GitHub.", "https://fluffyrp.com"),
("2025-05", "Spring Boot", "Spring Boot", "SpringBootNoteAPI: a note-taking REST API with a database, the first step into the framework that became the main focus.", "SpringBootNoteAPI: REST API для заметок с базой данных, первый шаг во фреймворк, который стал основным направлением.", "SpringBootNoteAPI"),
("2025-07", "Anime streaming service", "Аниме-стриминговый сервис", "Joined a team of 15 enthusiasts building an anime streaming service on Spring.", "Участие в разработке аниме-стримингового сервиса на Spring в команде из 15 энтузиастов.", None),
("2025-12", "Minecraft mods in Java", "Моды Minecraft на Java", "PearlTrajectoryPredictor shows where an ender pearl will land. Cubatar (2026-01) is an avatar and body generator with layered 3D rendering and caching.", "PearlTrajectoryPredictor показывает, куда упадёт эндер-жемчуг. Cubatar (2026-01) генерирует аватары и тела с послойным 3D-рендером и кешем.", "PearlTrajectoryPredictor"),
("2026-01", "Studying at STEP IT Academy", "Обучение в STEP IT Academy", "Course projects in Python (module 1) and Java (module 1), a console phone book among them.", "Учебные проекты на Python (модуль 1) и Java (модуль 1), среди них консольная телефонная книга.", "itstep-module-1-java"),
("2026-02", "Linux desktop", "Рабочее окружение на Linux", "dotfiles: a dynamic Material You Hyprland setup built with Matugen.", "dotfiles: динамический Material You конфиг Hyprland на базе Matugen.", "dotfiles"),
("2026-03", "Small utilities", "Небольшие утилиты", "pinterest-unshittifier fixes broken Pinterest filenames. Later in the spring: modrinth-fast-downloader and MrBeastSCAMBlocker.", "pinterest-unshittifier чинит кривые имена файлов Pinterest. Позже весной: modrinth-fast-downloader и MrBeastSCAMBlocker.", "pinterest-unshittifier"),
("2026-06", "Hardware: ESP32", "Железо: ESP32", "WakeOnLan-ESP32: a Telegram bot on an ESP32 that wakes a PC and checks that it is healthy.", "WakeOnLan-ESP32: Telegram-бот на ESP32, который включает ПК и проверяет, что он жив.", "WakeOnLan-ESP32"),
("2026-08", "Home server", "Домашний сервер", "A home server for my own services: self-hosting and Linux administration move from experiments into daily use.", "Домашний сервер для собственных сервисов: self-hosting и администрирование Linux из экспериментов становятся повседневной практикой.", None),
("2026-10", "Task Manager", "Task Manager", "A project and task management system, the diploma project at STEP IT Academy.", "Система управления проектами и задачами, дипломный проект в STEP IT Academy.", "task-manager"),
("2026-10", "Local RP showcase", "Витрина Local RP", "Public showcase of Local RP (LRP), a self-hosted web app for role-play chats with AI characters. The source stays private.", "Публичная витрина Local RP (LRP), self-hosted веб-приложения для ролевых чатов с ИИ-персонажами. Код остаётся закрытым.", "lrp-demo"),
]
TX = {"en": dict(path="/timeline/", title="Tokishu timeline: from first repositories to Spring Boot", desc="Timeline of Tokishu (Tok1shu): backend developer working with Java and Spring Boot, from the first GitHub repositories in 2022 to current projects.", h="Timeline", sub="Dates are approximate and follow GitHub repositories and my own recollection.", nav=["About", "Hardware", "Stack", "Contacts"], tln="Timeline", back="Home", note="Much was left out or simply forgotten while writing this. The real timeline is longer: there were more projects, experiments and courses than fit here.", foot="Available in English and Russian."),
      "ru": dict(path="/ru/timeline/", title="Таймлайн Токишу: от первых репозиториев до Spring Boot", desc="Таймлайн Токишу (Tok1shu): backend-разработчика на Java и Spring Boot, от первых репозиториев на GitHub в 2022 году до текущих проектов.", h="Таймлайн", sub="Даты приблизительные: по репозиториям на GitHub и по моей памяти.", nav=["Обо мне", "Железо", "Стек", "Контакты"], tln="Таймлайн", back="Главная", note="Многое не учтено или забыто при составлении. На самом деле таймлайн мог бы быть длиннее: проектов, экспериментов и курсов было больше, чем здесь поместилось.", foot="Доступен на английском и русском.")}
for k, t in TX.items():
    home = "/" if k == "en" else "/ru/"
    nav = "".join(f'<a href="{home}#{i}">{n}</a>' for i, n in zip(["about", "hardware", "stack", "contacts"], t["nav"])) + f'<a href="{t["path"]}" aria-current="page">{t["tln"]}</a>'
    items = ""
    for d, te, tr, xe, xr, repo in EV:
        title, text = (te, xe) if k == "en" else (tr, xr)
        link = (f'<a class="go" href="{repo if repo.startswith("http") else GH + repo}">{repo.replace("https://", "") if repo.startswith("http") else repo}</a>') if repo else ""
        tm = f'<time datetime="{d}">{d}</time>' if d else f'<time>{"Childhood" if k == "en" else "Детство"}</time>'
        items += f'<li>{tm}<div class="tcard"><h3>{E(title)}</h3><p>{E(text)}</p>{link}</div></li>'
    ld = {"@context": "https://schema.org", "@type": "ProfilePage", "mainEntity": {"@id": base + "/#person"}, "name": t["title"], "inLanguage": k, "url": base + t["path"]}
    loc, aloc = ("en_US", "ru_RU") if k == "en" else ("ru_RU", "en_US")
    imgalt = "Tokishu, Yaroslav Andrieiev, backend developer: Java and Spring Boot" if k == "en" else "Токишу, Ярослав Андреев, backend-разработчик: Java и Spring Boot"
    other = ("/ru/timeline/", "RU") if k == "en" else ("/timeline/", "EN")
    page = f'''<!doctype html>
<html lang="{k}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(t["title"])}</title>
<meta name="description" content="{E(t["desc"])}">
<link rel="canonical" href="{base}{t["path"]}">
<link rel="alternate" hreflang="en" href="{base}/timeline/"><link rel="alternate" hreflang="ru" href="{base}/ru/timeline/"><link rel="alternate" hreflang="x-default" href="{base}/timeline/">
<meta property="og:type" content="article"><meta property="og:title" content="{E(t["title"])}"><meta property="og:description" content="{E(t["desc"])}"><meta property="og:url" content="{base}{t["path"]}">
<meta property="article:author" content="{base}/"><meta property="article:modified_time" content="2026-10-29">
<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1">
<meta name="author" content="Yaroslav Andrieiev">
<meta name="referrer" content="strict-origin-when-cross-origin">
<meta name="color-scheme" content="dark light">
<meta name="theme-color" content="#141414" media="(prefers-color-scheme: dark)"><meta name="theme-color" content="#f4faf7" media="(prefers-color-scheme: light)">
<meta name="format-detection" content="telephone=no">
<link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="icon" href="/icon-192.png" type="image/png" sizes="192x192"><link rel="apple-touch-icon" href="/apple-touch-icon.png"><link rel="manifest" href="/site.webmanifest">
<link rel="alternate" type="text/plain" href="/llms.txt" title="llms.txt"><link rel="sitemap" type="application/xml" href="/sitemap.xml">
<meta property="og:site_name" content="Tokishu"><meta property="og:locale" content="{loc}"><meta property="og:locale:alternate" content="{aloc}">
<meta property="og:image" content="{base}/og-{k}.png"><meta property="og:image:type" content="image/png"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="{imgalt}">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{E(t["title"])}"><meta name="twitter:description" content="{E(t["desc"])}"><meta name="twitter:image" content="{base}/og-{k}.png"><meta name="twitter:image:alt" content="{imgalt}">
<link rel="stylesheet" href="/style.css">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head><body>
<div class="bg" aria-hidden="true"><i class="o1"></i><i class="o2"></i><i class="grid"></i></div>
<header class="top"><div class="wrap bar2"><a class="brand" href="{home}"><span class="tile" aria-hidden="true"><svg viewBox="0 0 64 64"><path d="M16 18h32v9H36v22h-8V27H16z" fill="currentColor"/></svg></span><span>Tokishu</span></a>
<nav>{nav}</nav><a class="lang" href="{other[0]}" hreflang="{other[1].lower()}">{other[1]}</a></div></header>
<main class="wrap narrow tlpage"><h1 class="h1s">{t["h"]}</h1><p class="sub">{t["sub"]}</p><ol class="tl">{items}</ol><p class="tlnote">{t["note"]}</p></main>
</body></html>'''
    d = "timeline" if k == "en" else "ru/timeline"
    os.makedirs(d, exist_ok=True)
    open(d + "/index.html", "w").write(page)
