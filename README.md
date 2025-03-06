# RapidRescue

# 🚑 Healthcare Emergency System

## 📌 Overview
This project is a **Healthcare Emergency System** that provides essential healthcare services such as **ambulance requests, hospital listings, medication details, and distance calculations**. The system enables users to log in, request an ambulance via Twilio SMS, search for hospitals, retrieve medication details, and calculate distances between locations using OpenRouteService API.

## 🛠️ Tech Stack & Tools Used
- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Flask (Python)
- **Database:** In-memory storage (can be extended to MongoDB/PostgreSQL)
- **APIs Used:**
  - Twilio API (for sending SMS)
  - OpenFDA API (for fetching medication details)
  - OpenRouteService API (for calculating distances)
- **Other Tools:** Flask, Jinja2, Requests library

## ⚙️ Installation & Setup

### 🔹 Prerequisites
Ensure you have the following installed:
- Python 3.x
- Flask (`pip install flask`)
- Requests library (`pip install requests`)
- Twilio SDK (`pip install twilio`)

### 🔹 Clone the Repository
```bash
git clone https://github.com/yourusername/healthcare-emergency-system.git
cd healthcare-emergency-system

 Backend Setup

pip install -r requirements.txt
python server.py
🔹 Frontend Setup
Open index.html in a web browser.

✨ Features
🔹 User Authentication - Login and registration pages for secure access.
🚑 Ambulance Service - Request an ambulance via SMS using Twilio.
🏥 Hospital Listings - View hospitals and filter by specialization.
💊 Medication Lookup - Fetch medicine details based on diseases.
📏 Distance Calculation - Compute distances between two locations using OpenRouteService API.
🔄 Technical Workflow
User logs in/registers through login.html or register.html.
Homepage (index.html) provides navigation to all features.
Ambulance request (ambulance_service.html) allows users to send an emergency SMS using Twilio.
Hospital listings (hospitals.html) display available hospitals with search functionality.
Medication search (medications.html) fetches medicines based on disease queries.
Distance calculation (distance.html) computes the shortest route between two locations.
📝 License
This project is open-source under the MIT License.

