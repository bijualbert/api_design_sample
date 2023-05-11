from flask import Flask, jsonify

app = Flask(__name__)

# Define the list of customers
customers = [
    {'id': 1, 'name': 'John Doe', 'email': 'john.doe@example.com'},
    {'id': 2, 'name': 'Jane Smith', 'email': 'jane.smith@example.com'},
    {'id': 3, 'name': 'Bob Johnson', 'email': 'bob.johnson@example.com'}
]

# Define the endpoint for the list of customers
@app.route('/customers')
def get_customers():
    return jsonify(customers)

# Define the endpoint for a specific customer
@app.route('/customers/<int:id>')
def get_customer(id):
    customer = next((customer for customer in customers if customer['id'] == id), None)
    if customer:
        return jsonify(customer)
    else:
        return 'Customer not found', 404

if __name__ == '__main__':
    app.run(debug=True)
