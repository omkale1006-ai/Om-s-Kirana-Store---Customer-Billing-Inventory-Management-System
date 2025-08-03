def duplicate(name, phone, email):
    with open("customer.txt", "r") as f:
        data = f.read()
    return name in data or phone in data or email in data


def main():
    user_name = input("Enter your name: ")
    while True:
        user_phone = input("Enter your phone number: ")
        user_email = input("Enter your email address: ")
        if user_phone.isdigit() and (len(user_phone)) == 10:
            if user_email.endswith("@gmail.com"):
                if duplicate(user_name, user_phone, user_email):
                    print(f"Welcome back, {user_name}!")
                else:
                    with open("customer.txt", "a") as f:
                        f.write(f"Name: {user_name}\n")
                        f.write(f"Phone: {user_phone}\n")
                        f.write(f"Email: {user_email}\n")
                        f.write("-" * 30 + "\n")
                    print("Thank you for visiting Om's Kirana Store. Your details have been successfully saved!")

                # Load items
                items = []
                with open("item.txt", "r") as f:
                    lines = f.readlines()
                    for line in lines:
                        name, price, stock = line.strip().split(",")
                        items.append({
                            "name": name,
                            "price": float(price),
                            "stock": int(stock),
                        })

                # Show items
                print("\nAvailable Items:")
                for index, item in enumerate(items):
                    print(f"{index}. {item['name']} - ₹{item['price']} (Stock: {item['stock']})")

                # Cart logic
                cart_item = []
                
                total = 0
                while True:
                    user_option = input("\nEnter the item number to purchase (or type 'done' to finish): ")

                    if user_option.lower() == "done":
                        print("Thank you for shopping with us!")
                        break

                    try:
                        index = int(user_option)
                        if index < 0 or index >= len(items):
                            print("Invalid item number. Please try again.")
                            continue

                        quantity = int(input("Enter quantity: "))
                        selected = items[index]

                        if quantity > selected["stock"]:
                            print("Sorry, the selected quantity is not available in stock.")
                        else:
                            amount = selected["price"] * quantity
                            total += amount
                            selected["stock"] -= quantity  # Optional update

                            cart_item.append((selected["name"], quantity, selected["price"], amount))
                            print(f"{quantity} x {selected['name']} added to cart. Subtotal: ₹{amount}")

                    except ValueError:
                        print("Invalid input. Please enter a valid number.")

                # Print final bill
                print("\n===== Final Bill =====")
                print(f"Customer Name : {user_name}")
                print(f"Phone Number  : {user_phone}")
                print(f"Email Address : {user_email}")
                print("-" * 30)

                with open("customer_bill.txt", "a", encoding="utf-8") as f:
                    f.write("\n===== Final Bill =====\n")
                    f.write(f"Customer Name : {user_name}\n")
                    f.write(f"Phone Number  : {user_phone}\n")
                    f.write(f"Email Address : {user_email}\n")
                    f.write("-" * 30 + "\n")

                    for name, qty, price, amount in cart_item:
                        line = f"{name} - ₹{price} x {qty} = ₹{amount}"
                        print(line)
                        f.write(line + "\n")

                    print(f"\nTotal Amount Payable: ₹{total}")
                    print("We appreciate your purchase. Have a wonderful day!")

                    f.write(f"\nTotal Amount Payable: ₹{total}\n")
                    f.write("=" * 50 + "\n")
                    with open("item.txt", "w") as f_item:
                        for item in items:
                            f_item.write(f"{item['name']},{item['price']},{item['stock']}\n")
                    break
            else:
                print("Invalid email address. Please ensure it ends with '@gmail.com'.")
        else:
            print("Invalid phone number. Please enter a 10-digit number only.")


main()
