from flask import Flask, render_template, request, redirect, url_for, flash
from db.interface import insert_data, get_all_data, delete_data, update_data

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Necessary for flashing messages

@app.route('/')
def index():
    data = get_all_data()  # Fetch data from the database
    return render_template('index.html', data=data)

@app.route('/insert', methods=['POST'])
def insert():
    new_data = request.form['data']
    if new_data:
        insert_data(new_data)  # Insert into the database
        flash("Data inserted successfully!", "success")
    else:
        flash("Please enter some data to insert.", "warning")
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):
    delete_data(id)  # Delete the data by ID
    flash("Data deleted successfully!", "success")
    return redirect(url_for('index'))

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    updated_data = request.form['data']
    if updated_data:
        update_data(id, updated_data)  # Update the data
        flash("Data updated successfully!", "success")
    else:
        flash("Please enter some data to update.", "warning")
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
