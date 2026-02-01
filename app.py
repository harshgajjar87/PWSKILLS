from flask import Flask

app = Flask(__name__)

@app.route('/user/<username>')
def show_user(username):
    return f"<h1>Profile Page for: {username}</h1>"

@app.route('/post/<int:post_id>')
def show_post(post_id):
    result = post_id * 10 
    return f"Displaying Post ID: {post_id} (Math check: {result})"

@app.route('/buy/<item>/<int:quantity>')
def buy_item(item, quantity):
    return f"You are buying {quantity} units of {item}."

if __name__ == '__main__':
    app.run(debug=True)