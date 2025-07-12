from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route("/download", methods=["POST"])
def download_video():
    data = request.json
    title = data.get("title", "video").replace(" ", "_")
    url = data.get("link")
    filename = f"{title}.mp4"
    try:
        result = subprocess.run(["yt-dlp", "-f", "bestvideo[height<=1080]+bestaudio/best[height<=1080]", "-o", filename, url], capture_output=True, text=True)
        print(result.stdout)
        return jsonify({"status": "success", "message": f"Video saved as {filename}"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
