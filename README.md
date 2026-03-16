# 🚀 PyStart

**PyStart** is a modern CLI tool for quickly creating Python projects from ready-to-use starter templates.

Inspired by tools like `create-next-app`, PyStart helps you bootstrap projects with a **beautiful interactive CLI**, **clean project structures**, and **instant dependency setup using `uv`**.

No more repetitive project setup. Start building immediately.

---

# ✨ Features

- ⚡ **Instant project scaffolding**
- 🎨 **Beautiful interactive CLI prompts**
- 📦 **Powered by `uv` for ultra-fast dependency management**
- 🧱 **Multiple starter templates**
- 🗂 **Clean and organized project structures**
- 🔧 **Automatic dependency installation**
- 🌱 **Optional Git initialization**

---

# 📦 Installation

First install **uv**:

```bash
curl -Ls https://astral.sh/uv/install.sh | sh
```

Then install PyStart:

```bash
pip install pystart
```

For development:

```bash
uv pip install -e .
```

---

# 🚀 Usage

Run the CLI:

```bash
pystart
```

You will see an interactive prompt:

```bash
? Project name: my_project
? Choose template:
❯ FastAPI
  CLI Tool
  Telegram Bot
  Flask API

? Initialize git? Yes
```

PyStart will generate your project:

```bash
✔ Creating project structure
✔ Initializing uv project
✔ Installing dependencies
✔ Initializing git repository

🎉 Your project is ready!
```

---

# 📁 Example Generated Project

Example FastAPI project:

```
my_project/
│
├── pyproject.toml
├── README.md
│
├── app/
│   └── main.py
│
└── .gitignore
```

---

# 🧱 Available Templates

Currently supported templates:

- ⚡ FastAPI API
- 🖥 CLI Tool
- 🤖 Telegram Bot
- 🌐 Flask API
- 📦 Empty Python Project

More templates coming soon.

---

# 🛠 Development

Clone the repository:

```bash
git clone https://github.com/yourusername/pystart.git
cd pystart
```

Install dependencies:

```bash
uv sync
```

Run locally:

```bash
uv run pystart
```

---

# 🧩 Project Structure

```
pystart/
│
├── cli.py
├── prompts.py
├── generator.py
│
├── templates/
│   ├── fastapi/
│   ├── flask/
│   ├── telegram_bot/
│   └── cli_tool/
│
└── utils/
```

---

# 🎯 Vision

PyStart aims to become a **simple yet powerful Python project generator**, similar to what modern JavaScript ecosystems have.

Future goals:

- 🌍 Remote templates
- 🔌 Plugin system
- 🧠 Smart project recommendations
- 🏗 Clean architecture templates
- 🐳 Docker-ready projects
- ☁️ Backend starter kits

---

# 🤝 Contributing

Contributions are welcome!

If you have ideas for new templates or improvements:

1. Fork the repository
2. Create a new branch
3. Submit a pull request

---

# 📜 License

MIT License

---

# ⭐ Support

If you like this project, consider giving it a **star ⭐ on GitHub**.
It helps the project grow and reach more developers.

---

**PyStart — Start your Python projects faster.**
