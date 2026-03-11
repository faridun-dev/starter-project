# 🤖 Aiogram Telegram Bot Template

This template provides a **clean and scalable starter structure** for building Telegram bots using **Aiogram**.

It is designed to help developers start quickly while maintaining a **modular architecture** that can grow with the project.

---

# ✨ Features

- 🤖 Built with **Aiogram**
- 🧱 Modular and scalable architecture
- ⚙️ Environment-based configuration using `.env`
- 🧩 Organized handlers and routers
- 📦 Dependency management with `uv`
- 🧼 Clean project structure ready for production
- 🚀 Simple bot startup with polling

---

# 📦 Requirements

- Python **3.10+**
- `uv` package manager
- A Telegram bot token from **BotFather**

---

# 🚀 Getting Started

## 1. Install dependencies

```bash
uv sync
```

Or manually:

```bash
uv add aiogram pydantic-settings python-dotenv
```

---

## 2. Configure environment variables

Copy the example file:

```bash
cp .env.example .env
```

Edit `.env` and add your bot token:

```env
BOT_TOKEN=your_bot_token_here
```

---

## 3. Run the bot

```bash
uv run bot/main.py
```

Your bot will now start in **polling mode**.

---

# 📁 Project Structure

```
telegram_bot/
│
├── pyproject.toml
├── README.md
├── .env
├── .env.example
│
├── bot/
│   ├── __init__.py
│   │
│   ├── main.py
│   ├── config.py
│   │
│   ├── handlers/
│   │   ├── __init__.py
│   │   └── start.py
│   │
│   ├── keyboards/
│   │   ├── __init__.py
│   │   └── main_menu.py
│   │
│   ├── services/
│   │   └── example_service.py
│   │
│   └── utils/
│       └── logger.py
│
└── tests/
```

---

# 🧠 How It Works

### `main.py`

The entry point of the bot.  
It initializes:

- Bot instance
- Dispatcher
- Routers
- Polling loop

---

### `config.py`

Handles configuration using **environment variables**.

Example:

```
BOT_TOKEN=your_token_here
```

---

### `handlers/`

Contains message handlers and command handlers.

Example:

```
/start
/help
```

Each handler is separated into its own module to keep the code organized.

---

### `keyboards/`

Contains **Telegram keyboard layouts**:

- Reply keyboards
- Inline keyboards

---

### `services/`

Business logic layer.

Use this folder for:

- API calls
- Database logic
- External services

Keeping logic here prevents handlers from becoming too complex.

---

### `utils/`

Utility helpers such as:

- logging
- formatting
- helper functions

---

# 🧪 Testing

Tests can be placed inside:

```
tests/
```

Example tools you can add:

```
pytest
pytest-asyncio
```

---

# 🔧 Development Tips

Run the bot in development mode:

```bash
uv run bot/main.py
```

Install new dependencies:

```bash
uv add package_name
```

Update dependencies:

```bash
uv lock
```

---

# 📈 Possible Extensions

This template can easily be extended with:

- FSM (Finite State Machine)
- Middleware
- PostgreSQL
- Redis
- Webhooks
- Docker
- Logging system
- Admin panel
- Background tasks

---

# 📜 License

This template is provided as part of the **PyStart project**.

You are free to modify and use it in your own projects.

---

# 🚀 Happy Coding

Build powerful Telegram bots faster with **Aiogram** and **PyStart**.