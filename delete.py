from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from pydantic import BaseModel
import datetime

# Import SQLAlchemy models and session setup (assuming already defined)
from sqlalchemy.orm import sessionmaker
from database import engine, SessionLocal
from models import Product, Order, User, OrderDetail  # Assuming models are defined as in previous examples

app = FastAPI()

# Dependency for getting the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic models for request validation
class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    stock_quantity: int

class ProductUpdate(BaseModel):
    name: str
    description: str
    price: float
    stock_quantity: int

class OrderCreate(BaseModel):
    user_id: int
    product_id: int
    quantity: int

class OrderStatus(BaseModel):
    status: str

# Admin Endpoints

# Add a new product (Admin only)
@app.post("/api/products", status_code=status.HTTP_201_CREATED)
async def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    new_product = Product(name=product.name, description=product.description, 
                          price=product.price, stock_quantity=product.stock_quantity)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

# Get product details by ID (Admin only)
@app.get("/api/products/{id}")
async def get_product(id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == id).first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return product

# Update a product (Admin only)
@app.put("/api/products/{id}")
async def update_product(id: int, product: ProductUpdate, db: Session = Depends(get_db)):
    existing_product = db.query(Product).filter(Product.id == id).first()
    if not existing_product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    
    existing_product.name = product.name
    existing_product.description = product.description
    existing_product.price = product.price
    existing_product.stock_quantity = product.stock_quantity
    db.commit()
    db.refresh(existing_product)
    return existing_product

# Delete a product (Admin only)
@app.delete("/api/products/{id}")
async def delete_product(id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == id).first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    
    db.delete(product)
    db.commit()
    return {"message": "Product deleted successfully"}

# List all orders (Admin only)
@app.get("/api/orders")
async def get_orders(db: Session = Depends(get_db)):
    orders = db.query(Order).all()
    return orders

# Get specific order details by ID (Admin only)
@app.get("/api/orders/{id}")
async def get_order(id: int, db: Session = Depends(get_db)):
    order = db.query(Order).filter(Order.id == id).first()
    if not order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")
    return order


# Customer Endpoints

# Fetch all products (Customer)
@app.get("/api/products")
async def get_all_products(db: Session = Depends(get_db)):
    products = db.query(Product).all()
    return products

# Create a new order (Customer)
@app.post("/api/orders", status_code=status.HTTP_201_CREATED)
async def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == order.product_id).first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    
    new_order = Order(user_id=order.user_id, order_date=datetime.datetime.utcnow(), status="Pending")
    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    # Add Order Details
    order_detail = OrderDetail(order_id=new_order.id, product_id=product.id, quantity=order.quantity, price=product.price)
    db.add(order_detail)
    db.commit()

    return {"message": "Order created successfully", "order_id": new_order.id}

# Fetch customer-specific orders (Customer)
@app.get("/api/orders/{customer_id}")
async def get_customer_orders(customer_id: int, db: Session = Depends(get_db)):
    orders = db.query(Order).filter(Order.user_id == customer_id).all()
    if not orders:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No orders found for this customer")
    return orders

# Check the status of a specific order (Customer)
@app.get("/api/orders/{order_id}/status")
async def get_order_status(order_id: int, db: Session = Depends(get_db)):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")
    return {"status": order.status}





from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from pydantic import BaseModel
import datetime

# Create FastAPI app with custom OpenAPI documentation
app = FastAPI(
    title="NewEra Cash & Carry API",
    description="This API allows admins and customers to manage products, orders, and view order status for NewEra Cash & Carry.",
    version="1.0.0"
)

# Define models and endpoints (as described previously)

# Example endpoint: Fetch all products
@app.get("/api/products", response_model=List[Product])
async def get_all_products(db: Session = Depends(get_db)):
    products = db.query(Product).all()
    return products
