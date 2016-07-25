from flask import Flask, render_template, request, redirect

import pg

db = pg.DB(dbname = 'restaurant_db')
app = Flask ('MyFormApp')

@app.route('/')
def form():
    return render_template(
    'restaurant.html',
    title= "Enter a new Restaurant"
    )

@app.route('/submit_form', methods = ['POST'])
def submit_form():
    new_restaurant_name = request.form['name']
    new_category = request.form['category']

    db.insert('restaurant', name = new_restaurant_name, category = new_category)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
