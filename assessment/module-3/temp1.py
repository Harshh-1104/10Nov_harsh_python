# RepairMate with User Input + OOP + File Handling

class RepairItem:  # Base class (OOP Inheritance)
    item_id = ""
    status = "Pending"

    def set_id(self, item_id):
        self.item_id = item_id


class Customer(RepairItem):  # Inheritance
    name = ""
    phone = ""
    devices = []

    def set_details(self, cid, name, phone):
        self.set_id(cid)
        self.name = name
        self.phone = phone
        self.devices = []


class Device(RepairItem):  # Inheritance
    brand = ""
    model = ""
    issue = ""

    def set_details(self, brand, model, issue):
        self.brand = brand
        self.model = model
        self.issue = issue
        self.status = "Pending"


# File handling - write
def save_customer_to_file(customer, filename="customers.txt"):
    try:
        f = open(filename, "a")
        f.write(f"{customer.item_id},{customer.name},{customer.phone}\n")
        f.close()
        print("✓ Customer saved to file.")
    except Exception as e:
        print("Error saving:", e)

# File handling - read
def read_customers_from_file(filename="customers.txt"):
    try:
        f = open(filename, "r")
        lines = f.readlines()
        f.close()
        print("\n📋 All customers from file:")
        for line in lines:
            parts = line.strip().split(",")
            if len(parts) >= 3:
                print(f"  ID: {parts[0]}, {parts[1]}, {parts[2]}")
    except Exception as e:
        print("Error reading file:", e)


def main():
    print("=== RepairMate - User Input Demo ===")

    # User input for customer (OOP)
    print("\n👤 Enter Customer Details:")
    cid = input("  Customer ID: ")
    name = input("  Name: ")
    phone = input("  Phone: ")

    customer = Customer()
    customer.set_details(cid, name, phone)

    # User input for device (OOP)
    print("\n📱 Enter Device Details:")
    brand = input("  Brand: ")
    model = input("  Model: ")
    issue = input("  Issue: ")

    device = Device()
    device.set_details(brand, model, issue)
    customer.devices.append(device)

    # Display user data
    print("\n📄 Summary:")
    print(f"Customer: ID={customer.item_id}, {customer.name} ({customer.phone})")
    print(f"Device: {device.brand} {device.model} - {device.issue} [{device.status}]")

    # File handling
    save_customer_to_file(customer)
    read_customers_from_file()


main()
