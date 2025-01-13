from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/cart")
def cart():
    return render_template("cart.html") 

@app.route("/checkout")
def checkout():
    return render_template("checkout.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/product-list")
def product():
    return render_template("product-list.html")

@app.route("/product-detail")
def product_detail():
    return render_template("product-detail.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")  # Add this route for registration
def register():
    return render_template("register.html")  # Ensure you have a register.html template

@app.route("/wishlist") 
def wishlist():
    return render_template("wishlist.html")

@app.route("/my-account")
def my_account():
    return render_template("my-account.html")

if __name__ == "__main__":
    app.run(debug=True)