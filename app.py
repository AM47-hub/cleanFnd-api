import json
from datetime import datetime

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
    
    result = clean_fnd_logic(fnd_list, status_date)
    return json.dumps(result)
