from flask import Flask

app = Flask(__name__)


# setup all data from a simple get
@app.get('/api/get_all')
def all_data():
    return {'data': 'all data'}

# Be able to query available stores at a certain time in the day and return only those
# that apply
@app.get('/api/available') # input: hour, minutes
def stores_available():
    return {
        'stores': 'stores available'
    }

# Be able to query all available products, across stores, with their total stock.
@app.get('/api/products')
def products():
    return {
        'products': 'All the available products with stock'
    }

# Be able to query if a product is available, at a certain store, and return that product's
# info
@app.get('/api/products/available_all_stores')
def products_avaiable():
    return {
        'store1': 'all the available products with info',
        'store2': 'all the available products with info',
        'store3': 'all the available products with info'
    }

# Be able to query available products for a particular store
@app.get('/api/products/available_one_store')
def products_avaiable_on_store(): # input: name
    return {
        'store_x' : 'all the available products',
    }

# Be able to check the validity of a Voucher code on said virtual cart. Calculate discounts
# and return both original and discounted prices
@app.get('/api/voucher')
def voucher(): #input: voucher, store_name
    
    return {
        'price' : '20000',
        'dicounted_price' : '14000'
    }

app.run(host='0.0.0.0', port=81) 