from flask import Flask, request, make_response
import re
import json
from datetime import datetime, timedelta
import os

app = Flask(__name__)

@app.route('/process', methods=['POST'])

def clean_fnd_logic(fnd_list, status_date_str):
    status_date = datetime.fromisoformat(status_date_str)
    past_anchors = []

    for item in fnd_list:
        # Extract the anchor from the raw string
        # Assuming format: "Address | Anchor:2026-04..."
        try:
            anchor_part = item.split("Anchor:")[1].strip()
            # Use your regex-validated timestamp logic
            anchor_dt = datetime.fromisoformat(anchor_part)
            
            if anchor_dt < status_date:
                past_anchors.append(anchor_part)
        except (IndexError, ValueError):
            continue # Skip malformed notes

    return past_anchors

# Standard wrapper for your Render/API setup
def handle_request(data):
    fnd_list = data.get("fndList", [])
    status_date = data.get("statusDate")

        return make_response(json.dumps(results), 200, {"Content-Type": "application/json"})
        # Silent: return make_response(json.dumps(debug_report), 200, {"Content-Type": "application/json"})

    except Exception as e:
        return make_response(json.dumps([{"fatal_crash": str(e)}]), 200)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
