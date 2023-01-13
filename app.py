from flask import Flask, render_template, request, flash, redirect
import connection_sql

app = Flask(__name__)
app.secret_key = 'awdsuhiIUZFQT34234G0032q03we2'


@app.route('/')
def index():
    items = connection_sql.get_items()
    return render_template("index.html", items=items)


@app.route('/add', methods=['POST'])
def add_item():
    item = request.form.get('new_item') + "\n"
    items = connection_sql.get_items()
    if item in items:
        flash("Keine doppelten Einträge bitte, das gibt Ärger!!!", "danger")
    else:
        items.append(item)
        connection_sql.write_items(items)
        flash("Item added successfully", "success")
    return redirect('/')


@app.route('/delete', methods=['POST'])
def delete_item():
    items = connection_sql.get_items()
    for item in items:
        if request.form.get(item):
            items.remove(item)
    connection_sql.write_items(items)
    flash("Item(s) deleted successfully", "success")
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
