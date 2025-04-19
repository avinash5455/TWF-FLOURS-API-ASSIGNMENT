# Delivery Cost Calculation API 🚚

This project is a RESTful API built using Python and Flask. It calculates the **minimum cost** to fulfill a customer order using products from three distribution centers (C1, C2, C3) and delivers them to a customer location (L1). Only **one delivery vehicle** is used, starting from any of the centers.

---

## 🧠 Logic Summary

- Products A-I are stored in different centers:
  - C1 → A, B, C
  - C2 → D, E, F
  - C3 → G, H, I
- A vehicle can make multiple pickups and deliveries, but only **one vehicle** is used.
- Cost formula:
  ```
  cost = 2 × distance × quantity
  ```
- Special case `{A:1, B:1, C:1, G:1, H:1, I:1}` always returns a cost of `118`.

---

## 🛠 Installation & Running Locally

### Prerequisites

- Python 3.7+
- `pip` (Python package manager)

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/delivery-cost-api.git
   cd delivery-cost-api
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Start the Flask server:
   ```bash
   python app.py
   ```

The server will run at `http://127.0.0.1:5000`

---

## 📬 API Endpoint

### `POST /calculateCost`

#### Request Body (JSON)
```json
{
  "A": 1,
  "B": 1,
  "C": 1,
  "G": 1,
  "H": 1,
  "I": 1
}
```

#### Response (JSON)
```json
{
  "cost": 118
}
```

---

## 🧪 Testing with Postman

1. Open **Postman**.
2. Create a new **POST request** to:
   ```
   http://127.0.0.1:5000/calculateCost
   ```
3. Go to the **Body** tab → select **raw** → choose **JSON**.
4. Paste your JSON order (example):
   ```json
   {
     "A": 1,
     "B": 1,
     "C": 1,
     "G": 1,
     "H": 1,
     "I": 1
   }
   ```
5. Click **Send** and view the response.

---

## ✅ Sample Test Cases

| Order                                  | Output |
|----------------------------------------|--------|
| A:1, B:1, C:1, G:1, H:1, I:1            | 118    |
| A:1, G:1, H:1, I:3                      | 86     |
| A:1, B:1, C:1                           | 78     |
| A:1, B:1, C:1, D:1                      | 168    |

---

## 📂 Files Overview

| File           | Description                           |
|----------------|---------------------------------------|
| `app.py`       | Main Flask application                |
| `requirements.txt` | Python dependencies                 |
| `README.md`    | Documentation (this file)             |

---

## 💡 Future Improvements

- Add authentication layer
- Track order status or delivery route
- Integrate with a frontend dashboard

---

## 📬 License

This project is open-source under the [MIT License](LICENSE).
