from flask import Flask, render_template, request

app = Flask(__name__)

# Fake tracking database (you can expand this later)
fake_data = {
    "ABC123": {"status": "In Transit", "location": "Kerala, India"},
    "XYZ789": {"status": "Delivered", "location": "Toronto, Canada"},
    "TEST001": {"status": "Pending Pickup", "location": "Warehouse"}
}

@app.route("/", methods=["GET", "POST"])
def index():
    tracking_info = None
    if request.method == "POST":
        tracking_id = request.form["tracking_id"].strip()
        tracking_info = fake_data.get(tracking_id, {"status": "Not Found", "location": "N/A"})
    return render_template("index.html", tracking_info=tracking_info)

if __name__ == "__main__":
    app.run(debug=True)

