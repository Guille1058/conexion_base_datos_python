# Student Management Database System

A Python-based CLI application that automates the creation of a MySQL database and manages user/student records. The script features administrative privilege checks, real-time data visualization using Pandas, and an emergency exit hotkey.

## 🚀 Features

* **Automatic Database Setup**: Creates the `alumnos_eig` database and the `Gente` table automatically if they don't exist.
* **Admin Shield**: Built-in check to ensure the script runs with Administrator (Windows) or Sudo (Linux/macOS) privileges.
* **Emergency Exit**: Immediate program termination by pressing the `ESC` key.
* **Data Validation**: Strict input length validation for all user fields.
* **Visual Reports**: Real-time display of the database content in a clean, formatted grid using `pandas` and `tabulate`.

## 🛠️ Prerequisites

Before running the application, ensure you have the following installed:

1.  **Python 3.x**
2.  **MySQL Server** (e.g., XAMPP, WAMP, or a standalone MySQL installation) running on `localhost:3306`.
3.  **Administrative Privileges**: Necessary for the `keyboard` library to intercept the hotkey.

## 📦 Installation

1. **Clone the repository** (or download the source code):
   ```bash
   git clone <your-repository-link>
   cd <project-folder>

    Create and activate a virtual environment:
   ```
   ```bash
    # Linux/macOS
    python3 -m venv .venv
    source .venv/bin/activate

    # Windows
    python -m venv .venv
    .venv\Scripts\activate
    ```
   
2. **Install dependencies**:
   
   ```bash
    pip install -r requirements.txt
   ```

🚦 Usage

    Start your local MySQL server.

    Run the script with Administrative/Sudo privileges:
    
   ```bash
    # Linux/macOS
    sudo .venv/bin/python main.py

    # Windows (Run PowerShell/CMD as Admin)
    python main.py
   ```

    Follow the on-screen prompts to enter the number of users and their details.

    Press ESC at any time to force-close the application safely.

📋 Requirements

The project relies on the following libraries:

    pymysql: Database connection.

    pandas: Data manipulation.

    tabulate: Table formatting in the console.

    keyboard: Global hotkey detection.

⚠️ Important Notes

    Database Credentials: By default, the script connects to localhost using user root with no password. If your configuration is different, please update the pymysql.connect parameters in main.py.

    Keyboard Library: This library requires root/admin access because it listens to hardware events globally.
