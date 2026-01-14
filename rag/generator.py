def generate_response(retrieved_text):
    if not retrieved_text:
        return None

    lines = retrieved_text.split("\n")

    data = {
        "mask": "",
        "purifier": "",
        "checkup": "",
        "actions": [],
        "message": ""
    }

    for line in lines:
        if line.startswith("Mask:"):
            data["mask"] = line.replace("Mask:", "").strip()
        elif line.startswith("Purifier:"):
            data["purifier"] = line.replace("Purifier:", "").strip()
        elif line.startswith("Checkup:"):
            data["checkup"] = line.replace("Checkup:", "").strip()
        elif line.startswith("-"):
            data["actions"].append(line.replace("-", "").strip())
        elif line.startswith("Message:"):
            data["message"] = line.replace("Message:", "").strip()

    return data
