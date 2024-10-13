from flask import Flask, render_template, request, redirect, url_for, flash
import db  

app = Flask(__name__)
app.secret_key = "supersecretkey"  
@app.route('/')
def index():
    try:
        pdb = db.connect('example.db')  
        data = {key: pdb[key] for key in pdb}  
        return render_template('index.html', data=data)
    except Exception as e:
        flash(f"Error fetching data: {str(e)}", "danger")
        return render_template('index.html', data={})

@app.route('/insert', methods=['POST'])
def insert():
    key = request.form['key']
    value = request.form['value']
    if key and value:
        try:
            pdb = db.connect('example.db')
            pdb[key] = value  
            pdb.commit()
            flash("Data inserted successfully!", "success")
        except Exception as e:
            flash(f"Error inserting data: {str(e)}", "danger")
    else:
        flash("Please enter both key and value.", "warning")
    return redirect(url_for('index'))

@app.route('/delete/<key>')
def delete(key):
    try:
        pdb = db.connect('example.db')
        del pdb[key]  
        pdb.commit()
        flash("Data deleted successfully!", "success")
    except KeyError:
        flash("Key not found.", "danger")
    except Exception as e:
        flash(f"Error deleting data: {str(e)}", "danger")
    return redirect(url_for('index'))

@app.route('/update/<key>', methods=['POST'])
def update(key):
    updated_value = request.form['value']
    if updated_value:
        try:
            pdb = db.connect('example.db')
            pdb[key] = updated_value  
            pdb.commit()
            flash("Data updated successfully!", "success")
        except KeyError:
            flash("Key not found.", "danger")
        except Exception as e:
            flash(f"Error updating data: {str(e)}", "danger")
    else:
        flash("Please enter a new value to update.", "warning")
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
