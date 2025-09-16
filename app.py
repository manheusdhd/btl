from flask import Flask, render_template, request, redirect

app = Flask(__name__)
# Lưu tạm trong RAM
messages = []

@app.route("/")
def index():
    return render_template("index.html", messages=messages)

@app.route("/send", methods=["POST"])
def send():
    name = request.form.get("name") or "Ẩn danh"
    text = request.form.get("text", "").strip()
    if text:
        messages.append({"name": name, "text": text})
    return redirect("/")

@app.route("/edit/<int:msg_id>", methods=["POST"])
def edit(msg_id):
    text = request.form.get("text", "").strip()
    if 0 <= msg_id < len(messages) and text:
        # Chỉ cập nhật nội dung (không sửa tên)
        messages[msg_id]["text"] = text
    return redirect("/")

@app.route("/delete/<int:msg_id>", methods=["POST"])
def delete(msg_id):
    if 0 <= msg_id < len(messages):
        messages.pop(msg_id)
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
