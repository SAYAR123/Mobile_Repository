# 📱 Mobile Repository

> A simple **CRUD-based Mobile Inventory Management System** built using **Python** and **Streamlit**, featuring an integrated **Google Gemini AI Assistant** for mobile-related queries.

🌐 **Live Demo:** https://mobile-repository.onrender.com

---

## 📖 Overview

Mobile Repository is a beginner-friendly inventory management application that demonstrates the implementation of **CRUD (Create, Read, Update, Delete)** operations using Python. The application provides a clean Streamlit interface for managing mobile phone records while also integrating **Google Gemini AI** to answer mobile-related questions.

The project is designed to showcase fundamental Python programming concepts, modular programming, and web application development with Streamlit.

---

## ✨ Features

- ➕ Add new mobile phones
- 📄 View complete inventory
- ✏️ Update mobile details
  - Mobile Name
  - Brand
  - Price
- 🗑 Delete mobile records
- 🔍 Search mobiles by name or brand
- 💰 Sort inventory by price
- 🤖 Gemini AI Assistant for mobile-related queries
- ⚠️ Graceful fallback message when AI service is unavailable
- 🌐 Streamlit-based responsive interface

---

## 🛠️ Technologies Used

- Python 3
- Streamlit
- Google Gemini API
- python-dotenv

---

## 📂 Project Structure

```
MobileRepository/
│
├── backend.py      # CRUD operations + Gemini AI
├── app.py          # Streamlit Frontend
├── requirements.txt
├── .env            # API Key (not uploaded)
└── README.md
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/<your-username>/Mobile-Repository.git

cd Mobile-Repository
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Create a `.env` file

```env
GEMINI_API_KEY=YOUR_API_KEY
```

---

## ▶️ Run the application

```bash
streamlit run app.py
```

The application will open in your browser at

```
http://localhost:8501
```

---

## 📱 CRUD Operations

### ➕ Create

Add a new mobile phone by entering:

- Mobile Name
- Brand
- Price

---

### 📄 Read

Displays the complete inventory in a searchable table.

---

### ✏️ Update

Update existing mobile information:

- Mobile Name
- Brand
- Price

---

### 🗑 Delete

Delete a mobile record by entering its name.

---

### 🔍 Search

Search mobiles using:

- Mobile Name
- Brand

---

### 💰 Sort

Display all mobiles sorted in ascending order of price.

---

## 🤖 AI Assistant

The application integrates **Google Gemini 2.5 Flash**.

Users can ask questions such as:

- Best gaming phone under ₹30,000
- Compare Samsung and OnePlus
- Suggest a camera phone
- Latest smartphone recommendations

If the API quota has been exceeded or the service is temporarily unavailable, the application displays a user-friendly fallback message instead of crashing.

---

## 📸 Application Screens

| Feature | Description |
|----------|-------------|
| Home | Navigation menu for all operations |
| Add Mobile | Add new mobile records |
| View Inventory | Displays complete inventory |
| Update | Modify existing mobile details |
| Delete | Remove mobile entries |
| Search | Find mobiles instantly |
| Sort | Arrange mobiles by price |
| AI Assistant | Mobile recommendations using Gemini |

---

## 🎯 Learning Outcomes

This project demonstrates:

- Python Functions
- Lists & Dictionaries
- CRUD Operations
- Modular Programming
- Exception Handling
- Streamlit UI Development
- API Integration
- Environment Variables
- User Input Validation

---

## 🚀 Future Improvements

- SQLite/MySQL database integration
- User Authentication
- Image upload for mobiles
- Inventory statistics dashboard
- CSV/Excel export
- Advanced filters
- Trendy CSS Background
- Mobile specifications database
- Edit multiple records simultaneously

---

## 👨‍💻 Author

**Sayar Sekhar Ghosh**

GitHub: https://github.com/SAYAR123

Project Repo: https://github.com/SAYAR123/Mobile_Repository

---

## 📜 License

This project is developed for educational and learning purposes.
