from flask import Flask, request, jsonify 
import pandas as pd

app = Flask(name)

products_df = pd.read_csv("ecommerce-dataset/products.csv") 
orders_df = pd.read_csv("ecommerce-dataset/orders.csv")

@app.route("/api/top-products", methods=["GET"]) 
def top_products(): 
    top = products_df.sort_values("sales", ascending=False).head(5) 
    return jsonify(top[["product_id", "name", "sales"]].to_dict(orient="records"))

@app.route("/api/order-status", methods=["GET"]) 
def order_status(): 
    order_id = request.args.get("id") 
    order = orders_df[orders_df["order_id"] == int(order_id)] 
    if order.empty: 
        return jsonify({"message": "Order not found"}), 404 
    return jsonify(order.to_dict(orient="records")[0])

@app.route("/api/stock-check", methods=["GET"]) 
def stock_check(): 
    name = request.args.get("name") 
    item = products_df[products_df["name"].str.contains(name, case=False)] 
    if item.empty: 
        return jsonify({"message": "Product not found"}), 404 
    return jsonify(item[["name", "stock"]].to_dict(orient="records"))

if name == "main": app.run(host="0.0.0.0", port=5000)