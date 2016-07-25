import pg
db = pg.DB(dbname='my_yelp')
import traceback

from flask import Flask, session, request, render_template, redirect
app = Flask('MyApp')



@app.route('/')
def home():

    if 'name' in session:

        return render_template('myReviews.html', name=session['name'])
    else:
        return render_template('restaurant_getname.html')




@app.route('/submit_name', methods=['POST'])
def submit_name():
    # This is how you set a value of a session variable
    session['name'] = request.form['name']
    return redirect('/')






@app.route('/display_review', methods=['GET'])
def display_review():
    try:
        query = db.query('''
        select
    	reviewer.name, review.content
        from
        	reviewer
        left outer join
          review on reviewer.id = review.reviewer_id where reviewer.name = '%s' limit 1 ''' % session['name'])

        users = query.namedresult()
        for user in users:
            print "User: %s, Review: %s" % (user.name, user.content)

        return render_template('myReviews.html', reviews = query)

    except Exception, e:
        return traceback.format_exc()









@app.route('/clear_name')
def clear_name():
    del session['name']
    return redirect('/')



app.secret_key = 'CSF686CCF85C6FRTCHQDBJDXHBHC1G478C86GCFTDCR'

if __name__ == '__main__':
    app.run(debug=True)
