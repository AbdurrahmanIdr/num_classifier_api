---

# **Number Classification API**  

A simple Flask-based API that classifies a given number based on its mathematical properties (prime, perfect, Armstrong, odd/even) and returns a fun fact about it.

---

## **Features**  
✅ Check if a number is **prime**  
✅ Check if a number is **perfect**  
✅ Check if a number is an **Armstrong number**  
✅ Determine if a number is **odd or even**  
✅ Compute the **sum of its digits**  
✅ Fetch an **interesting fun fact** using the [Numbers API](http://numbersapi.com)  

---

## **API Documentation**  

### **Endpoint**  
`GET /api/classify-number?number=<number>`  

### **Request Parameters**  
| Parameter | Type   | Description                    | Required |
|-----------|--------|--------------------------------|----------|
| number    | int    | The number to classify        | ✅ Yes   |

### **Successful Response (200 OK)**  
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

### **Error Response (400 Bad Request)**  
```json
{
    "number": "alphabet",
    "error": true
}
```

---

## **Installation**  

### **Prerequisites**  
- Python 3.8+
- pip (Python package manager)  

### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/AbdurrahmanIdr/num_classifier_api.git
cd number-classification-api
```

### **2️⃣ Create a Virtual Environment**  
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### **3️⃣ Install Dependencies**  
```bash
pip install -r requirements.txt
```

### **4️⃣ Run the API Locally**  
```bash
python run.py
```

The API will be available at `http://127.0.0.1:5000/api/classify-number?number=371`.

---

## **Project Structure**  

```
num_classifier_api/
│── app/
│   │── __init__.py         # Initializes Flask app
│   │── routes.py           # Defines API routes
│   │── controllers.py      # Handles request logic
│   │── services.py         # Business logic for number classification
│   │── utils.py            # Utility/helper functions
│── tests/
│   │── test_api.py         # Unit tests for the API
│── requirements.txt        # Dependencies (Flask, requests, etc.)
│── run.py                  # Entry point to run the app
│── README.md               # Project documentation
│── .gitignore              # Files to ignore in version control
```

---

## **Deployment**  

### **Deploying to Render / Railway / Heroku**  
1. Set up an account on **[Render](https://render.com)**, **[Railway](https://railway.app/)**, or **[Heroku](https://heroku.com/)**.  
2. Create a new project and connect your GitHub repository.  
3. Set the start command to:  
   ```bash
   gunicorn run:app
   ```
4. Deploy and obtain your public API URL.

---

## **Running Tests**  

To run unit tests, use:  
```bash
pytest tests/
```

---

## **Contributing**  

Feel free to fork the project, submit pull requests, or report issues.  

---

## **License**  

This project is open-source and available under the **MIT License**.

---

## **Contact**  

📧 Email: [abdurrahmaneedrees@gmail.com](mailto:abdurrahmaneedrees@gmail.com)  
🐙 GitHub: [AIAlmeida](https://github.com/AbdurrahmanIdr)  

---
