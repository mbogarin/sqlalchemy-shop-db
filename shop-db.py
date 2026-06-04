
# [PART 1]: SETUP
# 1. Imports:
from sqlalchemy import Integer, create_engine, String, ForeignKey, select, Boolean
from sqlalchemy.orm import relationship, Mapped, mapped_column, DeclarativeBase, Session

# from typing import List

# 2. Create engine & base:
engine = create_engine("sqlite:///shop.db")
class Base(DeclarativeBase):
    pass
session = Session(engine)


# [PART 2]: DEFINE TABLES
# 1. Create a User table:
class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(200), unique=True)
    
    # 4a) Set up relationship: A user can have many orders
    orders: Mapped[list["Order"]] = relationship(back_populates="user")

# 2. Create a Product table:
class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    price: Mapped[int] = mapped_column(Integer)
    
    # 4b) a product can appear in many orders.
    orders: Mapped[list["Order"]] = relationship(back_populates="product")

# 3. Create an Order table:
class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))
    quantity: Mapped[int] = mapped_column(Integer)
    shipped: Mapped[bool] = mapped_column(Boolean, default=False) # Bonus (1): status column.
    
    # Relationship: An order belongs to one user & one product.
    user: Mapped["User"] = relationship(back_populates="orders")
    product: Mapped["Product"] = relationship(back_populates="orders")


# [PART 3]: CREATE TABLES
Base.metadata.create_all(engine)


# [PART 4]: INSERT DATA
# Create a session:
# session = Session(engine) ??

# 1. Users:
user1 = User(name="Magali", email="m.bogarin@outlook.com")
user2 = User(name="Chase", email="chase@gmail.com")
user3 = User(name="Alex", email="alex@icloud.com")

session.add_all([user1, user2, user3])
session.commit()

# 2. Products:
product1 = Product(name="Lavender Candle", price=15)
product2 = Product(name="Sandalwood Soap", price=20)
product3 = Product(name="Peppermint Balm", price=18)

session.add_all([product1, product2, product3])
session.commit()

# 3. Orders:
order1 = Order(quantity=3, user=user1, product=product1)
order2 = Order(quantity=5, user=user2, product=product3)
order3 = Order(quantity=10, user=user2, product=product2)
order4 = Order(quantity=1, user=user3, product=product1)
order5 = Order(quantity=2, user=user3, product=product3)

session.add_all([order1, order2, order3, order4, order5])
session.commit()


# [PART 5]: QUERIES
# 1. Retrieve all users & print info:
query = select(User)
users = session.execute(query).scalars().all()

print("\n\n\n1. Users:\n-----------------------------")
for user in users:
    print(f"{user.name} | {user.email}")


# 2. Retrieve all products & print name + price:
query = select(Product)
products = session.execute(query).scalars().all()

print("\n2. Products:\n-----------------------------")
for product in products:
    print(f"{product.name}: ${product.price}")


# 3. Retrieve all orders, showing user's name, product name, and quantity:
query = select(Order)
orders = session.execute(query).scalars().all()

print("\n3. Orders:\n-----------------------------")
for order in orders:
    print(f"{order.id}: {order.user.name} -> {order.product.name} (x{order.quantity})")


# (BONUS):
# Query all orders that are not shipped:
query = select(Order).where(Order.shipped.is_(False))
unshipped_orders = session.execute(query).scalars().all()

print("\n4. Unshipped Orders:\n-----------------------------")
for order in unshipped_orders:
    print(f"{order.id}: {order.user.name} -> {order.product.name} (x{order.quantity})")


# Count total number of orders per user:
query = select(User)
users = session.execute(query).scalars().all()

print("\n5. Total Orders per User:\n-----------------------------")
for user in users:
    total_orders = len(user.orders)
    print(f"- {user.name}: {total_orders} total orders")


# UPDATE/DELETE QUERIES:
# 4. Update a product's price:
query = select(Product).where(Product.name == "Lavender Candle")
product = session.execute(query).scalars().first()

print("\n\n6. Update Product Price:\n-----------------------------")
if product:
    print(f"In the process of updating the product price for: {product.name} ...")
    print(f"- Current Price: ${product.price}")
    product.price = 10
    session.commit()
    
    print(f"- Updated Price: ${product.price}")
    print(f"\nSuccess! The product price for '{product.name}' was updated!\n")


# 5. Delete a user by ID:
query = select(User).where(User.id == 2)
user = session.execute(query).scalars().first() 

print("\n7. Delete User:\n-----------------------------")
if user:
    amount_orders = len(user.orders)
    print(f"In the process of deleting {amount_orders} order(s) for user: {user.name} ...")
    orders = user.orders

    for order in orders:
        print(f"- Deleted order #{order.id} for product '{order.product.name}'")
        session.delete(order)
    
    session.delete(user)
    session.commit()
    print(f"\nSuccess! The user '{user.name}' was deleted!\n\n\n")
    
    
    session.close()