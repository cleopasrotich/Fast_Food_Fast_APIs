from flask import Flask, jsonify, abort

app = Flask(__name__)

orders = [
    {
        'id': 1,
        'order_id': 'V2001',
        'customer': 'John Wick',
        'summary': '2 chips, 1/4 chicken',
        'location': 'Juja',
        'time': '1 hour ago',
    },
    {
        'id': 2,
        'order_id': 'V2511',
        'customer': 'Beverly Mideva',
        'summary': '1 Pizza Large, Latte',
        'location': 'Juja',
        'time': '2 hours ago',
    },
    {
        'id': 3,
        'order_id': 'V4000',
        'customer': 'Christene Mwangi',
        'summary': 'Expresso',
        'location': 'Westlands',
        'time': '6 hours ago',
    },
    {
        'id': 4,
        'order_id': 'V2288',
        'customer': 'Tony Stark',
        'summary': '1 Pizza Large',
        'location': 'Juja',
        'time': '1 day ago',
    },
    {
        'id': 5,
        'order_id': 'V2191',
        'customer': 'Cleopas Rotich',
        'summary': 'French Fries',
        'location': 'Juja',
        'time': '6 days ago',
    }
]


@app.route('/Fast_Food_Fast/api/v1/orders', methods=['GET'])
def get_orders():
    return jsonify(
        {'orders': orders}
    )


@app.route('/Fast_Food_Fast/api/v1/orders/<int:order_id>', methods=['GET'])
def get_task(order_id):
    required_order = []
    for order in orders:
        if order['id'] == order_id:
            required_order.append(order)
    if len(required_order) == 0:
        abort(404)

    return jsonify({'order': required_order[0]})


if __name__ == '__main__':
    app.run(debug=True)
