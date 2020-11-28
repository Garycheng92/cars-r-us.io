from flask import Flask, render_template
from flask import request, redirect
from db_connector.db_connector import connect_to_database, execute_query
#create the web application
app = Flask(__name__)

@webapp.route('/orders')
def orderData():
    print("Fetching and rendering orders web page...")
    db_connection = connect_to_database()
    query = "SELECT orderNumber, cartID, finalPrice from orders;"
    result = execute_query(db_connection, query).fetchall();
    print(result)
    return render_template('orders.html', rows = result)

@webapp.route('/cart')
def cartData():
    print("Fetching and rendering cart web page...")
    db_connection = connect_to_database()
    query = "SELECT cartID, productID, totalCost, quantity from cart;"
    result = execute_query(db_connection, query).fetchall();
    print(result)
    return render_template('cart.html', rows = result)

@webapp.route('/products_orders')
def products_ordersData():
    print("Fetching and rendering products_orders web page...")
    db_connection = connect_to_database()
    query = "SELECT productID, orderNumber from products_orders;"
    result = execute_query(db_connection, query).fetchall();
    print(result)
    return render_template('products_orders.html', rows = result)