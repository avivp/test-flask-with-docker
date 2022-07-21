from flask import Flask, render_template, jsonify
from inventory import Inventory

class MyWebApp:
    def __init__(self):
        self.port = 5000
        self.app = Flask(__name__)
        self.host = '0.0.0.0'
        self.inventory = Inventory()

    def run(self):
        @self.app.route('/')
        def home():
            return render_template('home.html')

        @self.app.route('/item/<item_id>')
        def item(item_id):
            res = self.inventory.get(int(item_id))
            if res is None:
                return jsonify({})
            return jsonify({'output': res})

        # port = int(os.environ.get('PORT', 5000))
        self.app.run(debug=True, host=self.host, port=self.port)


if __name__ == '__main__':
    webapp = MyWebApp()
    webapp.run()
