from flask import Flask, render_template, request, flash, redirect, url_for, session
from forms import RegistrationForm, LoginForm, Admin_AccountForm, Admin_AccountEditForm, Admin_BrandForm, Admin_ProductForm
import pymysql

app = Flask(__name__)
app.secret_key = '6031b7887339381ad7308ac543cacd0c'
app.jinja_env.globals.update(zip=zip, type=type, len=len)

def fetch_items(table, column):
    db = pymysql.connect('localhost', 'root', '', 'ink')
    cursor = db.cursor()
    #sql command
    cursor.execute("SELECT %s FROM %s" % (column, table))
    db.commit()
    return cursor.fetchall()

@app.route("/")
@app.route("/home/")
def home():
    if 'AccountID' in session:
            #admin account
            if session['Type'] == 'Admin':
                return redirect(url_for('admin_display', mode="accounts"))
            else:
                return render_template('home.html', user = session['Name'])
    else:
        return render_template('home.html')

@app.route("/search/", methods= ["POST", "GET"])
def search():
    if request.method == "GET":
        hkey = request.args.getlist("hkey")
        #setup database connection and cursor
        db = pymysql.connect('localhost', 'root', '', 'ink')
        cursor = db.cursor()
        #sql command
        cursor.execute("""SELECT Product.ProductID, Category.CategoryName, Brand.BrandName, 
                                    Product.ProductName, Product.ProductDesc, Product.Picture, 
                                    Product.Quantity, Product.Price FROM Product
                                    INNER JOIN Brand on Product.BrandID = Brand.BrandID
                                    INNER JOIN Category on Product.CategoryID = Category.CategoryID
                                    WHERE Product.ProductName LIKE '%{}%'""".format(hkey[0]))
        db.commit()
        results = cursor.fetchall()
        if len(results) > 0:
            results = list(results)
            for row in range(len(results)):
                results[row-1] = list(results[row-1])
                results[row-1][5] = 'images/' + results[row-1][5]

        if 'AccountID' in session:
            #admin account
            if session['Type'] == 'Admin':
                return redirect(url_for('admin_display', mode="accounts"))
            else:
                return render_template('search.html', results = results, hkey = hkey, user = session['Name'])
        else:
            return render_template('search.html', results = results, hkey = hkey)

@app.route("/categories/<string:category>", methods= ["GET"])
def categories(category):
    if request.method == "GET":
        if category == "drawing_pencils":
            #setup database connection and cursor
            db = pymysql.connect('localhost', 'root', '', 'ink')
            cursor = db.cursor()
            #sql command
            cursor.execute("""SELECT Product.ProductID, Category.CategoryName, Brand.BrandName, 
                                    Product.ProductName, Product.ProductDesc, Product.Picture, 
                                    Product.Quantity, Product.Price FROM Product
                                    INNER JOIN Brand on Product.BrandID = Brand.BrandID
                                    INNER JOIN Category on Product.CategoryID = Category.CategoryID
                                    WHERE Category.CategoryName = 'Drawing Pencils'""")
            db.commit()
            results = cursor.fetchall()
            if len(results) > 0:
                results = list(results)
                for row in range(len(results)):
                    results[row-1] = list(results[row-1])
                    results[row-1][5] = 'images/' + results[row-1][5]
            if 'AccountID' in session:
                    #admin account
                    if session['Type'] == 'Admin':
                        return redirect(url_for('admin_display', mode="accounts"))
                    else:
                        return render_template('categories.html', user = session['Name'], category=category, results=results)
            else:
                return render_template('categories.html', category=category, results=results)
        if category == "colored_pencils":
            #setup database connection and cursor
            db = pymysql.connect('localhost', 'root', '', 'ink')
            cursor = db.cursor()
            #sql command
            cursor.execute("""SELECT Product.ProductID, Category.CategoryName, Brand.BrandName, 
                                    Product.ProductName, Product.ProductDesc, Product.Picture, 
                                    Product.Quantity, Product.Price FROM Product
                                    INNER JOIN Brand on Product.BrandID = Brand.BrandID
                                    INNER JOIN Category on Product.CategoryID = Category.CategoryID
                                    WHERE Category.CategoryName = 'Colored Pencils'""")
            db.commit()
            results = cursor.fetchall()
            if len(results) > 0:
                results = list(results)
                for row in range(len(results)):
                    results[row-1] = list(results[row-1])
                    results[row-1][5] = 'images/' + results[row-1][5]
            if 'AccountID' in session:
                    #admin account
                    if session['Type'] == 'Admin':
                        return redirect(url_for('admin_display', mode="accounts"))
                    else:
                        return render_template('categories.html', user = session['Name'], category=category, results=results)
            else:
                return render_template('categories.html', category=category, results=results)
        if category == "brushes":
            #setup database connection and cursor
            db = pymysql.connect('localhost', 'root', '', 'ink')
            cursor = db.cursor()
            #sql command
            cursor.execute("""SELECT Product.ProductID, Category.CategoryName, Brand.BrandName, 
                                    Product.ProductName, Product.ProductDesc, Product.Picture, 
                                    Product.Quantity, Product.Price FROM Product
                                    INNER JOIN Brand on Product.BrandID = Brand.BrandID
                                    INNER JOIN Category on Product.CategoryID = Category.CategoryID
                                    WHERE Category.CategoryName = 'Brushes'""")
            db.commit()
            results = cursor.fetchall()
            if len(results) > 0:
                results = list(results)
                for row in range(len(results)):
                    results[row-1] = list(results[row-1])
                    results[row-1][5] = 'images/' + results[row-1][5]
            if 'AccountID' in session:
                    #admin account
                    if session['Type'] == 'Admin':
                        return redirect(url_for('admin_display', mode="accounts"))
                    else:
                        return render_template('categories.html', user = session['Name'], category=category, results=results)
            else:
                return render_template('categories.html', category=category, results=results)
        if category == "tablets":
            #setup database connection and cursor
            db = pymysql.connect('localhost', 'root', '', 'ink')
            cursor = db.cursor()
            #sql command
            cursor.execute("""SELECT Product.ProductID, Category.CategoryName, Brand.BrandName, 
                                    Product.ProductName, Product.ProductDesc, Product.Picture, 
                                    Product.Quantity, Product.Price FROM Product
                                    INNER JOIN Brand on Product.BrandID = Brand.BrandID
                                    INNER JOIN Category on Product.CategoryID = Category.CategoryID
                                    WHERE Category.CategoryName = 'Tablets'""")
            db.commit()
            results = cursor.fetchall()
            if len(results) > 0:
                results = list(results)
                for row in range(len(results)):
                    results[row-1] = list(results[row-1])
                    results[row-1][5] = 'images/' + results[row-1][5]
            if 'AccountID' in session:
                    #admin account
                    if session['Type'] == 'Admin':
                        return redirect(url_for('admin_display', mode="accounts"))
                    else:
                        return render_template('categories.html', user = session['Name'], category=category, results=results)
            else:
                return render_template('categories.html', category=category, results=results)

@app.route("/brand/<string:brand>", methods= ["GET"])
def brands(brand):
    if request.method == "GET":
        #setup database connection and cursor
        db = pymysql.connect('localhost', 'root', '', 'ink')
        cursor = db.cursor()
        #sql command
        cursor.execute("""SELECT Product.ProductID, Category.CategoryName, Brand.BrandName, 
                                Product.ProductName, Product.ProductDesc, Product.Picture, 
                                Product.Quantity, Product.Price FROM Product
                                INNER JOIN Brand on Product.BrandID = Brand.BrandID
                                INNER JOIN Category on Product.CategoryID = Category.CategoryID
                                WHERE Brand.BrandName = '%s'""" % brand)
        db.commit()
        results = cursor.fetchall()
        if len(results) > 0:
            results = list(results)
            for row in range(len(results)):
                results[row-1] = list(results[row-1])
                results[row-1][5] = 'images/' + results[row-1][5]
        if 'AccountID' in session:
                #admin account
                if session['Type'] == 'Admin':
                    return redirect(url_for('admin_display', mode="accounts"))
                else:
                    return render_template('brands.html', user = session['Name'], brand=brand, results=results)
        else:
            return render_template('brands.html', brand=brand, results=results)

@app.route("/products/<int:item_id>", methods= ["POST", "GET"])
def products(item_id):
    if request.method == "GET":
        #setup database connection and cursor
        db = pymysql.connect('localhost', 'root', '', 'ink')
        cursor = db.cursor()
        #sql command
        cursor.execute("""SELECT Product.ProductID, Category.CategoryName, Brand.BrandName, 
                                Product.ProductName, Product.ProductDesc, Product.Picture, 
                                Product.Quantity, Product.Price FROM Product
                                INNER JOIN Brand on Product.BrandID = Brand.BrandID
                                INNER JOIN Category on Product.CategoryID = Category.CategoryID
                                WHERE Product.ProductID = %s""" % item_id)
        db.commit()
        results = cursor.fetchall()
        if len(results) > 0:
            results = list(results)
            for row in range(len(results)):
                results[row-1] = list(results[row-1])
                results[row-1][5] = 'images/' + results[row-1][5]
        if 'AccountID' in session:
                #admin account
                if session['Type'] == 'Admin':
                    return redirect(url_for('admin_display', mode="accounts"))
                else:
                    return render_template('products.html', user = session['Name'], results=results)
        else:
            return render_template('products.html', results=results)

@app.route("/addcart/<int:acc_id>/<int:item_id>", methods= ["GET"])
def addcart(acc_id, item_id):
    if request.method == "GET":
        #setup database connection and cursor
        db = pymysql.connect('localhost', 'root', '', 'ink')
        cursor = db.cursor()
        #sql command
        cursor.execute("""INSERT INTO Cart (ProductID, AccountID) VALUES (%s, %s)""", (item_id, acc_id))
        db.commit()
        flash('Product added to cart', 'success')
        hkey = ['']
        return redirect(url_for('search', hkey = hkey))

@app.route("/cart/<int:acc_id>", methods= ["GET"])
def cart(acc_id):
    if request.method == 'GET':
        #setup database connection and cursor
        db = pymysql.connect('localhost', 'root', '', 'ink')
        cursor = db.cursor()
        #sql command
        cursor.execute("""SELECT Cart.CartID, Account.AccountID, Product.ProductID, Product.ProductName, Product.Price FROM Cart
                                INNER JOIN Product on Cart.ProductID = Product.ProductID
                                INNER JOIN Account on Cart.AccountID = Account.AccountID
                                WHERE Cart.AccountID = %s""" % acc_id)
        db.commit()
        results = cursor.fetchall()

        #calculate total
        total = 0
        for result in results:
            total += result[4]

        if 'AccountID' in session:
                #admin account
                if session['Type'] == 'Admin':
                    return redirect(url_for('admin_display', mode="accounts"))
                else:
                    return render_template('cart.html', user = session['Name'], results=results, total=total)
        else:
            return render_template('cart.html', results=results, total=total)

@app.route("/cart/<int:acc_id>/delete/<int:cart_id>", methods= ["GET"])
def cart_delete(cart_id, acc_id):
    if request.method == 'GET':
        #setup database connection and cursor
        db = pymysql.connect('localhost', 'root', '', 'ink')
        cursor = db.cursor()
        #sql command
        cursor.execute("DELETE FROM Cart WHERE CartID = %d" % cart_id)
        db.commit()

        flash(f"Product deleted from cart", "success")
        return redirect(url_for('cart', acc_id = acc_id))

@app.route("/addorders/<int:acc_id>", methods= ["GET"])
def addorders(acc_id):
    if request.method == 'GET':
        #setup database connection and cursor
        db = pymysql.connect('localhost', 'root', '', 'ink')
        cursor = db.cursor()
        #sql command
        cursor.execute("""SELECT Cart.CartID, Account.AccountID, Product.ProductID FROM Cart
                                INNER JOIN Product on Cart.ProductID = Product.ProductID
                                INNER JOIN Account on Cart.AccountID = Account.AccountID
                                WHERE Cart.AccountID = %s""" % acc_id)
        db.commit()
        results = cursor.fetchall()

        for result in results:
            cursor.execute("INSERT INTO OrderDesc (ProductID, AccountID, OrderDate) VALUES (%s, %s, NOW())", (result[2], result[1]))
            db.commit()
            cursor.execute("DELETE FROM Cart WHERE CartID = %s" % result[0])
            db.commit()

        flash(f"Orders created", "success")
        return redirect(url_for('orders', acc_id = acc_id))

@app.route("/orders/<int:acc_id>", methods= ["GET"])
def orders(acc_id):
    if request.method == 'GET':
        #setup database connection and cursor
        db = pymysql.connect('localhost', 'root', '', 'ink')
        cursor = db.cursor()
        #sql command
        cursor.execute("""SELECT OrderDesc.OrderID, Account.AccountID, Product.ProductName, Product.Price, OrderDesc.OrderDate FROM OrderDesc
                                INNER JOIN Product on OrderDesc.ProductID = Product.ProductID
                                INNER JOIN Account on OrderDesc.AccountID = Account.AccountID
                                WHERE OrderDesc.AccountID = %s""" % acc_id)
        db.commit()
        results = cursor.fetchall()

        if 'AccountID' in session:
                #admin account
                if session['Type'] == 'Admin':
                    return redirect(url_for('admin_display', mode="accounts"))
                else:
                    return render_template('orders.html', user = session['Name'], results=results)
        else:
            return render_template('orders.html', results=results)

@app.route("/about/")
def about():
    if 'AccountID' in session:
            #admin account
            if session['Type'] == 'Admin':
                return redirect(url_for('admin_display', mode="accounts"))
            else:
                return render_template('about.html', user = session['Name'])
    else:
        return render_template('about.html')

@app.route("/contact/")
def contact():
    if 'AccountID' in session:
            #admin account
            if session['Type'] == 'Admin':
                return redirect(url_for('admin_display', mode="accounts"))
            else:
                return render_template('contact.html', user = session['Name'])
    else:
        return render_template('contact.html')

@app.route("/login/", methods= ["POST", "GET"])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        #success login
        try:
            name = request.form['username']
            pw = request.form['password']
            #setup database connection and cursor
            db = pymysql.connect('localhost', 'root', '', 'ink')
            cursor = db.cursor()
            #sql command
            cursor.execute("SELECT AccountID, Type, Name, Password FROM Account WHERE Name = %s", (name))
            db.commit()

            results = cursor.fetchall()
            for row in results:
                acc_id = row[0]
                acc_type = row[1]
                acc_name = row[2]
                acc_pw = row[3]
                #session
                session['Name'] = acc_name
                session['AccountID'] = acc_id
                session['Type'] = acc_type
                session['Password'] = acc_pw

            if session["Password"] == pw:
                #admin account
                if session['Type'] == 'Admin':
                    flash(f'Logged in as %s (Admin Account).'%session['Name'], 'success')
                    return redirect(url_for('admin_display', mode="accounts"))
                else:
                    flash(f'Logged in as %s.'%session['Name'], 'success')
                    return redirect(url_for('home'))
            else:
                flash('Login Unsuccessful, please check the password and/or the username', 'danger')
                return redirect(url_for('login'))
        except:
            flash('Login Unsuccessful, please check the password and/or the username', 'danger')
            return redirect(url_for('login'))
    return render_template('login.html', title = 'Login', form = form)

@app.route("/logout/")
def logout():
    #exit session logged in user
    session.pop('Name', None)
    session.pop('AccountID', None)
    session.pop('Type', None)
    session.pop('Password', None)
    flash('Logged out', 'success')
    return render_template('home.html')

@app.route("/register/", methods= ["POST", "GET"])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate_on_submit():
        name = request.form['username']
        email = request.form['email']
        pw = request.form['password']
        #setup database connection and cursor
        db = pymysql.connect('localhost', 'root', '', 'ink')
        cursor = db.cursor()
        #sql command
        cursor.execute("INSERT INTO Account (Type, Name, Email, Password) VALUES ('Member', %s, %s, %s)", (name, email, pw))
        db.commit()

        flash(f'Account created for '+name+'.', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form = form)

@app.route('/admin/display/<string:mode>', methods= ["POST", "GET"])
def admin_display(mode):
    if request.method == "GET":
        if mode == "accounts":
            #setup database connection and cursor
            db = pymysql.connect('localhost', 'root', '', 'ink')
            cursor = db.cursor()
            #sql command
            cursor.execute("SELECT * FROM Account")
            db.commit()
            results = cursor.fetchall()
            cursor.execute("DESC Account")
            db.commit()
            field_names = cursor.fetchall()

            return render_template('admin_display.html', user = session['Name'], mode=mode, results=results, field_names=field_names)

        if mode == "brands":
            #setup database connection and cursor
            db = pymysql.connect('localhost', 'root', '', 'ink')
            cursor = db.cursor()
            #sql command
            cursor.execute("SELECT * FROM Brand")
            db.commit()
            results = cursor.fetchall()
            cursor.execute("DESC Brand")
            db.commit()
            field_names = cursor.fetchall()

            return render_template('admin_display.html', user = session['Name'], mode=mode, results=results, field_names=field_names)

        if mode == "products":
            #setup database connection and cursor
            db = pymysql.connect('localhost', 'root', '', 'ink')
            cursor = db.cursor()
            #sql command
            cursor.execute("""SELECT Product.ProductID, Category.CategoryName, Brand.BrandName, 
                                    Product.ProductName, Product.ProductDesc, Product.Picture, 
                                    Product.Quantity, Product.Price FROM Product
                                    INNER JOIN Brand on Product.BrandID = Brand.BrandID
                                    INNER JOIN Category on Product.CategoryID = Category.CategoryID""")
            db.commit()
            results = cursor.fetchall()
            #reduce the number of text shown in display
            if len(results) > 0:
                results = list(results)
                for row in range(len(results)):
                    results[row-1] = list(results[row-1])
                    if len(results[row-1][4]) > 25:
                        results[row-1][4] = results[row-1][4][:25] + "..."
                    if len(results[row-1][5]) > 10:
                        results[row-1][5] = results[row-1][5][:25] + "..."
                    results[row-1][5] = 'images/' + results[row-1][5]
            #obtain column names from other tables
            cursor.execute("SELECT `COLUMN_NAME` FROM `INFORMATION_SCHEMA`.`COLUMNS` WHERE `TABLE_SCHEMA` = 'ink' AND `TABLE_NAME` IN ('Brand', 'Category') AND `COLUMN_NAME` LIKE '%Name';")
            db.commit()
            foreign_names = cursor.fetchall()
            cursor.execute("DESC Product")
            db.commit()
            field_names = cursor.fetchall()

            return render_template('admin_display.html', user = session['Name'], mode=mode, results=results, field_names=field_names, foreign_names=foreign_names)

        if mode == "orders":            #setup database connection and cursor
            db = pymysql.connect('localhost', 'root', '', 'ink')
            cursor = db.cursor()
            #sql command
            cursor.execute("""SELECT OrderDesc.OrderID, Product.ProductID, Product.ProductName, 
                                    Product.Price, Account.AccountID, Account.Name, OrderDesc.OrderDate FROM OrderDesc
                                    INNER JOIN Account on OrderDesc.AccountID = Account.AccountID
                                    INNER JOIN Product on OrderDesc.ProductID = Product.ProductID""")
            db.commit()
            results = cursor.fetchall()
            #obtain column names from other tables
            cursor.execute("SELECT `COLUMN_NAME` FROM `INFORMATION_SCHEMA`.`COLUMNS` WHERE `TABLE_SCHEMA` = 'ink' AND `TABLE_NAME` IN ('Account', 'Product') AND `COLUMN_NAME` LIKE '%Name';")
            db.commit()
            foreign_names = cursor.fetchall()
            cursor.execute("SELECT `COLUMN_NAME` FROM `INFORMATION_SCHEMA`.`COLUMNS` WHERE `TABLE_SCHEMA` = 'ink' AND `TABLE_NAME` IN ('Product') AND `COLUMN_NAME` LIKE '%Price';")
            db.commit()
            price_name = cursor.fetchall()
            cursor.execute("DESC OrderDesc")
            db.commit()
            field_names = cursor.fetchall()

            return render_template('admin_display.html', user = session['Name'], mode=mode, results=results, field_names=field_names, foreign_names=foreign_names, price_name=price_name)

@app.route('/admin/display/<string:mode>/delete/<int:item_id>', methods= ["POST", "GET"])
def admin_delete(mode, item_id):
    if request.method == 'GET':
        if mode == "accounts":
            #setup database connection and cursor
            db = pymysql.connect('localhost', 'root', '', 'ink')
            cursor = db.cursor()
            #sql command
            cursor.execute("DELETE FROM Account WHERE AccountID = %d" % item_id)
            db.commit()

            flash(f"Account deleted", "success")
            return redirect(url_for('admin_display', mode="accounts"))

        if mode == "brands":
            #setup database connection and cursor
            db = pymysql.connect('localhost', 'root', '', 'ink')
            cursor = db.cursor()
            #sql command
            cursor.execute("DELETE FROM Brand WHERE BrandID = %d" % item_id)
            db.commit()

            flash(f"Brand deleted", "success")
            return redirect(url_for('admin_display', mode="brands"))

        if mode == "products":
            #setup database connection and cursor
            db = pymysql.connect('localhost', 'root', '', 'ink')
            cursor = db.cursor()
            #sql command
            cursor.execute("DELETE FROM Product WHERE ProductID = %d" % item_id)
            db.commit()

            flash(f"Product deleted", "success")
            return redirect(url_for('admin_display', mode="products"))

        if mode == "orders":
            #setup database connection and cursor
            db = pymysql.connect('localhost', 'root', '', 'ink')
            cursor = db.cursor()
            #sql command
            cursor.execute("DELETE FROM OrderDesc WHERE OrderID = %d" % item_id)
            db.commit()

            flash(f"Order cancelled", "success")
            return redirect(url_for('admin_display', mode="orders"))

@app.route('/admin/display/<string:mode>/create', methods= ["POST", "GET"])
def admin_create(mode):
    if mode == "accounts":
        form = Admin_AccountForm()
        formfield = [getattr(form, 'acctype'), getattr(form, 'username'),
                    getattr(form, 'email'), getattr(form, 'password'),
                    getattr(form, 'confirm_password')]

        if request.method == 'POST':
            acc_type = request.form['acctype']
            name = request.form['username']
            email = request.form['email']
            pw = request.form['password']
            #setup database connection and cursor
            db = pymysql.connect('localhost', 'root', '', 'ink')
            cursor = db.cursor()
            #sql command
            cursor.execute("INSERT INTO Account (Type, Name, Email, Password) VALUES (%s, %s, %s, %s)", (acc_type, name, email, pw))
            db.commit()

            flash(f'Account created for '+name+'.', 'success')
            return redirect(url_for('admin_display', mode="accounts"))

    elif mode == "brands":
        form = Admin_BrandForm()
        formfield = [getattr(form, 'brandname')]
        if request.method == 'POST':
            brand_name = request.form['brandname']
            #setup database connection and cursor
            db = pymysql.connect('localhost', 'root', '', 'ink')
            cursor = db.cursor()
            #sql command
            cursor.execute("INSERT INTO Brand (BrandName) VALUES (%s)", (brand_name))
            db.commit()

            flash(f'Brand created for '+brand_name+'.', 'success')
            return redirect(url_for('admin_display', mode="brands"))

    elif mode == "products":
        form = Admin_ProductForm()
        form.categoryid.choices = []
        form.brandid.choices = []
        #add dynamic choices dependent from another table
        for row in fetch_items('Category', '*'):
            form.categoryid.choices += [(str(row[0]), row[1])]
        for row in fetch_items('Brand', '*'):
            form.brandid.choices += [(str(row[0]), row[1])]

        formfield = [getattr(form, 'categoryid'), getattr(form, 'brandid'), 
                    getattr(form, 'productname'), getattr(form, 'productdesc'), 
                    getattr(form, 'picture'), getattr(form, 'quantity'), 
                    getattr(form, 'price')]

        if request.method == 'POST':
            category_id = request.form['categoryid']
            brand_id = request.form['brandid']
            product_name = request.form['productname']
            product_desc = request.form['productdesc']
            image = request.form['picture']
            quantity = request.form['quantity']
            price = request.form['price']

            # if 'file' not in request.files:
            #     flash('no file directory', 'danger')
            #     return redirect(request.url)
            # image = request.files['picture']
            # if image and allowed_file(image.filename):
            #     filename = secure_filename(image.filename)
            #     file.save(os.path.join(app.config['image_folder'], filename))

            #setup database connection and cursor
            db = pymysql.connect('localhost', 'root', '', 'ink')
            cursor = db.cursor()
            #sql command
            cursor.execute("INSERT INTO Product (CategoryID, BrandID, ProductName, ProductDesc, Picture, Quantity, Price) VALUES (%s, %s, %s, %s, %s, %s, %s)", (category_id, brand_id, product_name, product_desc, image, quantity, price))
            db.commit()

            flash(f'Product created for '+product_name+'.', 'success')
            return redirect(url_for('admin_display', mode="products"))


    return render_template('admin_create.html', form = form, mode = mode, formfield = formfield)

@app.route('/admin/display/<string:mode>/edit/<int:item_id>', methods= ["POST", "GET"])
def admin_edit(mode, item_id):
    if mode == "accounts":
        form = Admin_AccountEditForm()
        if request.method == 'GET':
            #formfield for getting text input boxes
            formfield = [getattr(form, 'acctype'), getattr(form, 'username'),
            getattr(form, 'email'), getattr(form, 'password')]
            #fieldvalues for selected file's original values
            db = pymysql.connect('localhost', 'root', '', 'ink')
            cursor = db.cursor()
            #sql command
            cursor.execute("SELECT Type, Name, Email, Password FROM Account WHERE AccountID = %d" % item_id)
            db.commit()

            results = cursor.fetchall()
            return render_template('admin_edit.html', form = form, mode = mode, formfield = formfield, results = results, item_id = item_id)
        if request.method == 'POST':
            acc_type = request.form['acctype']
            name = request.form['username']
            email = request.form['email']
            pw = request.form['password']
            #setup database connection and cursor
            db = pymysql.connect('localhost', 'root', '', 'ink')
            cursor = db.cursor()
            #sql command
            cursor.execute("UPDATE Account SET Type = %s, Name = %s, Email = %s, Password = %s WHERE AccountID = %s", (acc_type, name, email, pw, item_id))
            db.commit()

            flash(f'Account edited for '+name+'.', 'success')
            return redirect(url_for('admin_display', mode="accounts"))

    elif mode == "brands":
        form = Admin_BrandForm()
        if request.method == 'GET':
            #formfield for getting text input boxes
            formfield = [getattr(form, 'brandname')]
            #fieldvalues for selected file's original values
            db = pymysql.connect('localhost', 'root', '', 'ink')
            cursor = db.cursor()
            #sql command
            cursor.execute("SELECT BrandName FROM Brand WHERE BrandID = %d" % item_id)
            db.commit()

            results = cursor.fetchall()
            return render_template('admin_edit.html', form = form, mode = mode, formfield = formfield, results = results, item_id = item_id)
        if request.method == 'POST':
            brand_name = request.form['brandname']
            #setup database connection and cursor
            db = pymysql.connect('localhost', 'root', '', 'ink')
            cursor = db.cursor()
            #sql command
            cursor.execute("UPDATE Brand SET BrandName = %s WHERE BrandID = %s", (brand_name, item_id))
            db.commit()

            flash(f'Brand edited for '+brand_name+'.', 'success')
            return redirect(url_for('admin_display', mode="brands"))

    elif mode == "products":
        form = Admin_ProductForm()
        form.categoryid.choices = []
        form.brandid.choices = []
        #add dynamic choices dependent from another table
        for row in fetch_items('Category', '*'):
            form.categoryid.choices += [(str(row[0]), row[1])]
        for row in fetch_items('Brand', '*'):
            form.brandid.choices += [(str(row[0]), row[1])]

        if request.method == 'GET':
            #formfield for getting text input boxes
            formfield = [getattr(form, 'categoryid'), getattr(form, 'brandid'), 
                        getattr(form, 'productname'), getattr(form, 'productdesc'), 
                        getattr(form, 'picture'), getattr(form, 'quantity'), 
                        getattr(form, 'price')]
            #fieldvalues for selected file's original values
            db = pymysql.connect('localhost', 'root', '', 'ink')
            cursor = db.cursor()
            #sql command
            cursor.execute("""SELECT Category.CategoryName, Brand.BrandName, 
                                    Product.ProductName, Product.ProductDesc, Product.Picture, 
                                    Product.Quantity, Product.Price FROM Product
                                    INNER JOIN Brand on Product.BrandID = Brand.BrandID
                                    INNER JOIN Category on Product.CategoryID = Category.CategoryID
                                    WHERE Product.ProductID = %s""" % item_id)
            db.commit()

            results = cursor.fetchall()
            return render_template('admin_edit.html', form = form, mode = mode, formfield = formfield, results = results, item_id = item_id)
        if request.method == 'POST':
            category_id = request.form['categoryid']
            brand_id = request.form['brandid']
            product_name = request.form['productname']
            product_desc = request.form['productdesc']
            image = request.form['picture']
            quantity = request.form['quantity']
            price = request.form['price']
            #setup database connection and cursor
            db = pymysql.connect('localhost', 'root', '', 'ink')
            cursor = db.cursor()
            #sql command
            cursor.execute("""UPDATE Product SET CategoryID = %s, BrandID = %s, ProductName = %s, 
                                    ProductDesc = %s, Picture = %s, Quantity = %s, Price = %s 
                                    WHERE ProductID = %s""", (category_id, brand_id, product_name, product_desc, image, quantity, price, item_id))
            db.commit()

            flash(f'Product edited for '+product_name+'.', 'success')
            return redirect(url_for('admin_display', mode="products"))

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port="8000")