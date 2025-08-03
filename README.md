
# Om's Kirana Store 🛒

A Python-based billing and inventory management system designed for a Kirana (grocery) store. It manages customer information, displays available products, handles purchases, updates stock, and generates a bill for the customer.

---

## 📌 Features

- ✅ Customer data storage and duplicate detection
- 🛍 Item selection with quantity input
- 📦 Inventory stock management
- 🧾 Auto-generated final bill with totals
- 💾 File-based record keeping using `.txt` files

---

## 📁 Files Used

- `customer.txt` – Stores customer name, phone number, and email.
- `item.txt` – Contains item details in the format: `ItemName,Price,Stock`.
- `customer_bill.txt` – Stores the bill details for each customer.

---

## ⚙️ How It Works

1. Asks the user for their name, phone number, and email.
2. Checks if the customer already exists.
3. Displays available items from `item.txt`.
4. User selects items and quantity.
5. Validates stock and adds items to cart.
6. Generates a final bill.
7. Updates `item.txt` to reflect remaining stock.
8. Saves bill in `customer_bill.txt`.

---

## 🧪 Sample Item Format (item.txt)

