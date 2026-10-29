import json, html
base = "https://tokishu.lazurite.cc"
E = html.escape
T = {
"en": dict(path="/", title="Tokishu: backend developer, Java and Spring Boot",
 desc="Tokishu (Yaroslav Andrieiev, Tok1shu, Токишу) is a backend developer working with Java and Spring Boot. Profiles, hardware and contacts.",
 nav=["About", "Hardware", "Stack", "Contacts"],
 role="Backend developer", real="Yaroslav Andrieiev (Ярослав Андреев)",
 lead="I work mainly with Java and Spring Boot: REST APIs, databases and the services around them.",
 b1="GitHub", b2="Contact",
 about="About",
 aboutp="Tokishu is the nickname of Yaroslav Andrieiev. I use it on GitHub, Steam, Discord and Telegram. I am a backend developer at the start of my career, focused on Java and Spring Boot. I also self-host my own services and run them on Linux.",
 facts=[("Nickname", "Tokishu, Tok1shu"), ("Born", "11 February 2008"), ("Location", "Prague, Czechia"), ("Languages", "Ukrainian, Russian, English, Czech")],
 hwh="Hardware",
 hw=[("Main device", "MacBook Air 13\" (2026)", [("Chip", "Apple M5"), ("CPU", "10 cores: 4 performance, 6 efficiency"), ("Memory", "24 GB unified"), ("Storage", "512 GB SSD"), ("System", "macOS 27")], "Daily laptop. Used as a thin client: the code runs on the server."),
 ("Server", "Home server", [("CPU", "AMD Ryzen 7 7700X, 8 cores / 16 threads"), ("Motherboard", "ASRock B650M Pro RS (AM5)"), ("Memory", "32 GB DDR5-6000 (2 x 16 GB)"), ("GPU", "NVIDIA GeForce RTX 4060 Ti, 16 GB"), ("Storage", "1 TB NVMe (WD Black SN7100), 960 GB and 256 GB SATA SSD"), ("Network", "1 Gbit/s Ethernet"), ("System", "Arch Linux, LTS kernel")], "Headless. Runs the IDE backend over JetBrains Gateway, game streaming and self-hosted services.")],
 stackh="Stack", stackp="Java and Spring Boot at the center.",
 stack=[("Languages and core", ["Java 17 / 21", "SQL", "Python (scripting, automation)"]),
        ("Backend frameworks", ["Spring Boot 3", "Spring Data JPA", "Spring Security", "Spring AOP", "MapStruct", "Lombok"]),
        ("Databases and caching", ["PostgreSQL", "Hibernate ORM", "Flyway", "Redis", "MariaDB"]),
        ("Messaging and real-time", ["RabbitMQ", "WebSocket"]),
        ("Architecture and security", ["REST API", "OpenAPI / Swagger", "OAuth2", "JWT", "RBAC"]),
        ("DevOps and tools", ["Docker", "Docker Compose", "Linux", "Systemd", "Bash", "Caddy", "Git", "Maven", "Coolify", "S3 API"])],
  find="Contacts",
 foot="Available in English and Russian."),
"ru": dict(path="/ru/", title="Токишу (Tokishu): backend-разработчик, Java и Spring Boot",
 desc="Токишу (Ярослав Андреев, Tokishu, Tok1shu) — backend-разработчик, работает с Java и Spring Boot. Профили, железо и контакты.",
 nav=["Обо мне", "Железо", "Стек", "Контакты"],
 role="Backend-разработчик", real="Yaroslav Andrieiev (Ярослав Андреев)",
 lead="Работаю в основном с Java и Spring Boot: REST API, базы данных и сервисы вокруг них.",
 b1="GitHub", b2="Связаться",
 about="Обо мне",
 aboutp="Токишу — ник Ярослава Андреева. Под ним я на GitHub, в Steam, Discord и Telegram. Я backend-разработчик в начале пути, сфокусирован на Java и Spring Boot. Также сам поднимаю и обслуживаю свои сервисы на Linux.",
 facts=[("Ник", "Токишу, Tokishu, Tok1shu"), ("Родился", "11.02.2008"), ("Город", "Прага, Чехия"), ("Языки", "Украинский, русский, английский, чешский")],
 hwh="Железо",
 hw=[("Основное устройство", "MacBook Air 13\" (2026)", [("Чип", "Apple M5"), ("Процессор", "10 ядер: 4 производительных, 6 энергоэффективных"), ("Память", "24 ГБ единая"), ("Накопитель", "SSD 512 ГБ"), ("Система", "macOS 27")], "Ежедневный ноутбук. Работает тонким клиентом: код выполняется на сервере."),
 ("Сервер", "Домашний сервер", [("Процессор", "AMD Ryzen 7 7700X, 8 ядер / 16 потоков"), ("Материнская плата", "ASRock B650M Pro RS (AM5)"), ("Память", "32 ГБ DDR5-6000 (2 x 16 ГБ)"), ("Видеокарта", "NVIDIA GeForce RTX 4060 Ti, 16 ГБ"), ("Накопители", "NVMe 1 ТБ (WD Black SN7100), SATA SSD 960 ГБ и 256 ГБ"), ("Сеть", "Ethernet 1 Гбит/с"), ("Система", "Arch Linux, LTS-ядро")], "Без монитора. Держит бэкенд IDE через JetBrains Gateway, игровой стриминг и собственные сервисы.")],
 stackh="Стек", stackp="В центре Java и Spring Boot.",
 stack=[("Языки и база", ["Java 17 / 21", "SQL", "Python (скрипты, автоматизация)"]),
        ("Backend-фреймворки", ["Spring Boot 3", "Spring Data JPA", "Spring Security", "Spring AOP", "MapStruct", "Lombok"]),
        ("Базы данных и кеш", ["PostgreSQL", "Hibernate ORM", "Flyway", "Redis", "MariaDB"]),
        ("Очереди и real-time", ["RabbitMQ", "WebSocket"]),
        ("Архитектура и безопасность", ["REST API", "OpenAPI / Swagger", "OAuth2", "JWT", "RBAC"]),
        ("DevOps и инструменты", ["Docker", "Docker Compose", "Linux", "Systemd", "Bash", "Caddy", "Git", "Maven", "Coolify", "S3 API"])],
  find="Контакты",
 foot="Доступен на английском и русском."),
}
SAME = ["https://github.com/Tok1shu", "https://www.twitch.tv/tokishu", "https://modrinth.com/user/tokishu", "https://steamcommunity.com/id/tokishu/", "https://discord.com/users/761175017588916224", "https://t.me/tokishu", "https://www.linkedin.com/in/tokishu/", "https://www.reddit.com/user/tok1shu/"]
ICONS = {"reddit": '<svg viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="M12 0C5.373 0 0 5.373 0 12c0 3.314 1.343 6.314 3.515 8.485l-2.286 2.286C.775 23.225 1.097 24 1.738 24H12c6.627 0 12-5.373 12-12S18.627 0 12 0Zm4.388 3.199c1.104 0 1.999.895 1.999 1.999 0 1.105-.895 2-1.999 2-.946 0-1.739-.657-1.947-1.539v.002c-1.147.162-2.032 1.15-2.032 2.341v.007c1.776.067 3.4.567 4.686 1.363.473-.363 1.064-.58 1.707-.58 1.547 0 2.802 1.254 2.802 2.802 0 1.117-.655 2.081-1.601 2.531-.088 3.256-3.637 5.876-7.997 5.876-4.361 0-7.905-2.617-7.998-5.87-.954-.447-1.614-1.415-1.614-2.538 0-1.548 1.255-2.802 2.803-2.802.645 0 1.239.218 1.712.585 1.275-.79 2.881-1.291 4.64-1.365v-.01c0-1.663 1.263-3.034 2.88-3.207.188-.911.993-1.595 1.959-1.595Zm-8.085 8.376c-.784 0-1.459.78-1.506 1.797-.047 1.016.64 1.429 1.426 1.429.786 0 1.371-.369 1.418-1.385.047-1.017-.553-1.841-1.338-1.841Zm7.406 0c-.786 0-1.385.824-1.338 1.841.047 1.017.634 1.385 1.418 1.385.785 0 1.473-.413 1.426-1.429-.046-1.017-.721-1.797-1.506-1.797Zm-3.703 4.013c-.974 0-1.907.048-2.77.135-.147.015-.241.168-.183.305.483 1.154 1.622 1.964 2.953 1.964 1.33 0 2.47-.81 2.953-1.964.057-.137-.037-.29-.184-.305-.863-.087-1.795-.135-2.769-.135Z"/></svg>', "linkedin": '<svg viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>', 'github': '<svg viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"/></svg>', 'telegram': '<svg viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="M11.944 0A12 12 0 0 0 0 12a12 12 0 0 0 12 12 12 12 0 0 0 12-12A12 12 0 0 0 12 0a12 12 0 0 0-.056 0zm4.962 7.224c.1-.002.321.023.465.14a.506.506 0 0 1 .171.325c.016.093.036.306.02.472-.18 1.898-.962 6.502-1.36 8.627-.168.9-.499 1.201-.82 1.23-.696.065-1.225-.46-1.9-.902-1.056-.693-1.653-1.124-2.678-1.8-1.185-.78-.417-1.21.258-1.91.177-.184 3.247-2.977 3.307-3.23.007-.032.014-.15-.056-.212s-.174-.041-.249-.024c-.106.024-1.793 1.14-5.061 3.345-.48.33-.913.49-1.302.48-.428-.008-1.252-.241-1.865-.44-.752-.245-1.349-.374-1.297-.789.027-.216.325-.437.893-.663 3.498-1.524 5.83-2.529 6.998-3.014 3.332-1.386 4.025-1.627 4.476-1.635z"/></svg>', 'discord': '<svg viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="M20.317 4.3698a19.7913 19.7913 0 00-4.8851-1.5152.0741.0741 0 00-.0785.0371c-.211.3753-.4447.8648-.6083 1.2495-1.8447-.2762-3.68-.2762-5.4868 0-.1636-.3933-.4058-.8742-.6177-1.2495a.077.077 0 00-.0785-.037 19.7363 19.7363 0 00-4.8852 1.515.0699.0699 0 00-.0321.0277C.5334 9.0458-.319 13.5799.0992 18.0578a.0824.0824 0 00.0312.0561c2.0528 1.5076 4.0413 2.4228 5.9929 3.0294a.0777.0777 0 00.0842-.0276c.4616-.6304.8731-1.2952 1.226-1.9942a.076.076 0 00-.0416-.1057c-.6528-.2476-1.2743-.5495-1.8722-.8923a.077.077 0 01-.0076-.1277c.1258-.0943.2517-.1923.3718-.2914a.0743.0743 0 01.0776-.0105c3.9278 1.7933 8.18 1.7933 12.0614 0a.0739.0739 0 01.0785.0095c.1202.099.246.1981.3728.2924a.077.077 0 01-.0066.1276 12.2986 12.2986 0 01-1.873.8914.0766.0766 0 00-.0407.1067c.3604.698.7719 1.3628 1.225 1.9932a.076.076 0 00.0842.0286c1.961-.6067 3.9495-1.5219 6.0023-3.0294a.077.077 0 00.0313-.0552c.5004-5.177-.8382-9.6739-3.5485-13.6604a.061.061 0 00-.0312-.0286zM8.02 15.3312c-1.1825 0-2.1569-1.0857-2.1569-2.419 0-1.3332.9555-2.4189 2.157-2.4189 1.2108 0 2.1757 1.0952 2.1568 2.419 0 1.3332-.9555 2.4189-2.1569 2.4189zm7.9748 0c-1.1825 0-2.1569-1.0857-2.1569-2.419 0-1.3332.9554-2.4189 2.1569-2.4189 1.2108 0 2.1757 1.0952 2.1568 2.419 0 1.3332-.946 2.4189-2.1568 2.4189Z"/></svg>', 'steam': '<svg viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="M11.979 0C5.678 0 .511 4.86.022 11.037l6.432 2.658c.545-.371 1.203-.59 1.912-.59.063 0 .125.004.188.006l2.861-4.142V8.91c0-2.495 2.028-4.524 4.524-4.524 2.494 0 4.524 2.031 4.524 4.527s-2.03 4.525-4.524 4.525h-.105l-4.076 2.911c0 .052.004.105.004.159 0 1.875-1.515 3.396-3.39 3.396-1.635 0-3.016-1.173-3.331-2.727L.436 15.27C1.862 20.307 6.486 24 11.979 24c6.627 0 11.999-5.373 11.999-12S18.605 0 11.979 0zM7.54 18.21l-1.473-.61c.262.543.714.999 1.314 1.25 1.297.539 2.793-.076 3.332-1.375.263-.63.264-1.319.005-1.949s-.75-1.121-1.377-1.383c-.624-.26-1.29-.249-1.878-.03l1.523.63c.956.4 1.409 1.5 1.009 2.455-.397.957-1.497 1.41-2.454 1.012H7.54zm11.415-9.303c0-1.662-1.353-3.015-3.015-3.015-1.665 0-3.015 1.353-3.015 3.015 0 1.665 1.35 3.015 3.015 3.015 1.663 0 3.015-1.35 3.015-3.015zm-5.273-.005c0-1.252 1.013-2.266 2.265-2.266 1.249 0 2.266 1.014 2.266 2.266 0 1.251-1.017 2.265-2.266 2.265-1.253 0-2.265-1.014-2.265-2.265z"/></svg>', 'twitch': '<svg viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="M11.571 4.714h1.715v5.143H11.57zm4.715 0H18v5.143h-1.714zM6 0L1.714 4.286v15.428h5.143V24l4.286-4.286h3.428L22.286 12V0zm14.571 11.143l-3.428 3.428h-3.429l-3 3v-3H6.857V1.714h13.714Z"/></svg>', 'modrinth': '<svg viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="M12.252.004a11.78 11.768 0 0 0-8.92 3.73 11 10.999 0 0 0-2.17 3.11 11.37 11.359 0 0 0-1.16 5.169c0 1.42.17 2.5.6 3.77.24.759.77 1.899 1.17 2.529a12.3 12.298 0 0 0 8.85 5.639c.44.05 2.54.07 2.76.02.2-.04.22.1-.26-1.7l-.36-1.37-1.01-.06a8.5 8.489 0 0 1-5.18-1.8 5.34 5.34 0 0 1-1.3-1.26c0-.05.34-.28.74-.5a37.572 37.545 0 0 1 2.88-1.629c.03 0 .5.45 1.06.98l1 .97 2.07-.43 2.06-.43 1.47-1.47c.8-.8 1.48-1.5 1.48-1.52 0-.09-.42-1.63-.46-1.7-.04-.06-.2-.03-1.02.18-.53.13-1.2.3-1.45.4l-.48.15-.53.53-.53.53-.93.1-.93.07-.52-.5a2.7 2.7 0 0 1-.96-1.7l-.13-.6.43-.57c.68-.9.68-.9 1.46-1.1.4-.1.65-.2.83-.33.13-.099.65-.579 1.14-1.069l.9-.9-.7-.7-.7-.7-1.95.54c-1.07.3-1.96.53-1.97.53-.03 0-2.23 2.48-2.63 2.97l-.29.35.28 1.03c.16.56.3 1.16.31 1.34l.03.3-.34.23c-.37.23-2.22 1.3-2.84 1.63-.36.2-.37.2-.44.1-.08-.1-.23-.6-.32-1.03-.18-.86-.17-2.75.02-3.73a8.84 8.839 0 0 1 7.9-6.93c.43-.03.77-.08.78-.1.06-.17.5-2.999.47-3.039-.01-.02-.1-.02-.2-.03Zm3.68.67c-.2 0-.3.1-.37.38-.06.23-.46 2.42-.46 2.52 0 .04.1.11.22.16a8.51 8.499 0 0 1 2.99 2 8.38 8.379 0 0 1 2.16 3.449 6.9 6.9 0 0 1 .4 2.8c0 1.07 0 1.27-.1 1.73a9.37 9.369 0 0 1-1.76 3.769c-.32.4-.98 1.06-1.37 1.38-.38.32-1.54 1.1-1.7 1.14-.1.03-.1.06-.07.26.03.18.64 2.56.7 2.78l.06.06a12.07 12.058 0 0 0 7.27-9.4c.13-.77.13-2.58 0-3.4a11.96 11.948 0 0 0-5.73-8.578c-.7-.42-2.05-1.06-2.25-1.06Z"/></svg>'}
SOC = [("GitHub", "github.com/Tok1shu", SAME[0], ICONS["github"]), ("Telegram", "t.me/tokishu", SAME[5], ICONS["telegram"]), ("LinkedIn", "linkedin.com/in/tokishu", SAME[6], ICONS["linkedin"]), ("Reddit", "u/tok1shu", SAME[7], ICONS["reddit"]), ("Discord", "tokishu", SAME[4], ICONS["discord"]), ("Steam", "steamcommunity.com/id/tokishu", SAME[3], ICONS["steam"]), ("Twitch", "twitch.tv/tokishu", SAME[1], ICONS["twitch"]), ("Modrinth", "modrinth.com/user/tokishu", SAME[2], ICONS["modrinth"])]
ICON_GH = '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 .5a11.5 11.5 0 0 0-3.64 22.41c.58.1.79-.25.79-.56v-2c-3.2.7-3.87-1.37-3.87-1.37-.52-1.33-1.28-1.69-1.28-1.69-1.04-.71.08-.7.08-.7 1.15.08 1.76 1.18 1.76 1.18 1.03 1.76 2.7 1.25 3.35.96.1-.74.4-1.25.73-1.54-2.55-.29-5.24-1.28-5.24-5.69 0-1.26.45-2.28 1.18-3.09-.12-.29-.51-1.46.11-3.05 0 0 .97-.31 3.17 1.18a11 11 0 0 1 5.77 0c2.2-1.49 3.17-1.18 3.17-1.18.62 1.59.23 2.76.11 3.05.74.81 1.18 1.83 1.18 3.09 0 4.42-2.69 5.39-5.25 5.68.41.36.78 1.06.78 2.13v3.16c0 .31.21.67.8.56A11.5 11.5 0 0 0 12 .5z"/></svg>'
ICON_MAIL = '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" d="M3 6h18v12H3zM3 7l9 7 9-7"/></svg>'
for k, t in T.items():
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "Person", "@id": base + "/#person", "name": "Tokishu", "alternateName": ["Tok1shu", "Токишу", "Yaroslav Andrieiev", "Ярослав Андреев"], "givenName": "Yaroslav", "familyName": "Andrieiev", "birthDate": "2008-02-11", "homeLocation": {"@type": "City", "name": "Prague"}, "url": base + "/",
         "image": base + "/avatar.jpg", "jobTitle": "Backend developer", "description": t["desc"], "email": "tokishu@lazurite.cc",
         "knowsAbout": ["Java", "Spring Boot", "REST API", "Backend development", "Linux", "Docker"],
         "sameAs": SAME},
        {"@type": "WebSite", "@id": base + "/#site", "url": base + "/", "name": "Tokishu", "inLanguage": k}]}
    nav = "".join(f'<a href="#{i}">{n}</a>' for i, n in zip(["about", "hardware", "stack", "contacts"], t["nav"]))
    facts = "".join(f"<div><dt>{E(a)}</dt><dd>{E(b)}</dd></div>" for a, b in t["facts"])
    stack = "".join('<div class="sg"><h3>' + E(g) + '</h3><div class="chips">' + "".join(f"<span>{E(i)}</span>" for i in items) + '</div></div>' for g, items in t["stack"])
    soc = "".join(f'<a class="link" rel="me" href="{u}"><span class="ic">{c}</span><span><b>{n}</b>{h}</span></a>' for n, h, u, c in SOC)
    tl = "/timeline/" if k == "en" else "/ru/timeline/"; tln = "Timeline" if k == "en" else "Таймлайн"
    hwc = "".join(f'<div class="hwrow"><div class="hwinfo"><div class="eyebrow">{E(a)}</div><h3>{E(b)}</h3><p>{E(n)}</p></div><dl class="hwstats" style="--n:{len(sp)}">{"".join(f"<div><dt>{E(x)}</dt><dd>{E(y)}</dd></div>" for x, y in sp)}</dl></div>' for a, b, sp, n in t["hw"])
    loc, aloc = ("en_US", "ru_RU") if k == "en" else ("ru_RU", "en_US")
    imgalt = "Tokishu, Yaroslav Andrieiev, backend developer: Java and Spring Boot" if k == "en" else "Токишу, Ярослав Андреев, backend-разработчик: Java и Spring Boot"
    other = ("/ru/", "RU") if k == "en" else ("/", "EN")
    page = f'''<!doctype html>
<html lang="{k}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(t["title"])}</title>
<meta name="description" content="{E(t["desc"])}">
<link rel="canonical" href="{base}{t["path"]}">
<link rel="alternate" hreflang="en" href="{base}/"><link rel="alternate" hreflang="ru" href="{base}/ru/"><link rel="alternate" hreflang="x-default" href="{base}/">
<meta property="og:type" content="profile"><meta property="og:title" content="{E(t["title"])}"><meta property="og:description" content="{E(t["desc"])}"><meta property="og:url" content="{base}{t["path"]}">
<meta property="profile:first_name" content="Yaroslav"><meta property="profile:last_name" content="Andrieiev"><meta property="profile:username" content="tokishu">
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
<header class="top"><div class="wrap bar2"><a class="brand" href="{t["path"]}"><span class="tile" aria-hidden="true"><svg viewBox="0 0 64 64"><path d="M16 18h32v9H36v22h-8V27H16z" fill="currentColor"/></svg></span><span>Tokishu</span></a>
<nav>{nav}<a href="{tl}">{tln}</a></nav><a class="lang" href="{other[0]}" hreflang="{other[1].lower()}">{other[1]}</a></div></header>
<main>
<section class="hero wrap" id="top"><div class="hcopy">
<div class="role">{t["role"]}</div>
<h1>Tokishu</h1>
<p class="real">{t["real"]}</p>
<p class="lead">{t["lead"]}</p>
<div class="cta"><a class="btn primary" href="https://github.com/Tok1shu">{ICON_GH}{t["b1"]}</a><a class="btn" href="#contacts">{t["b2"]}</a></div></div>
<div class="ava"><img src="/avatar.jpg" alt="Tokishu" width="460" height="460"></div></section>
<section class="wrap" id="about"><h2>{t["about"]}</h2><div class="split"><p class="big">{t["aboutp"]}</p><dl class="facts">{facts}</dl></div></section>
<section class="wrap" id="hardware"><h2>{t["hwh"]}</h2><div class="hwlist">{hwc}</div></section>
<section class="wrap" id="stack"><h2>{t["stackh"]}</h2><p class="sub">{t["stackp"]}</p><div class="sgrid">{stack}</div></section>
<section class="wrap" id="contacts"><h2>{t["find"]}</h2><div class="links">
{soc}
<a class="link" href="mailto:tokishu@lazurite.cc"><span class="ic">{ICON_MAIL}</span><span><b>Email</b>tokishu@lazurite.cc</span></a>
</div></section>
</main>
<script src="/app.js" defer></script>
</body></html>'''
    open(("ru/" if k == "ru" else "") + "index.html", "w").write(page)
