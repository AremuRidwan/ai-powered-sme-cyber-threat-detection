def generate_alert(prediction):
    if prediction != "BENIGN":
        return "⚠️ ALERT: Suspicious network activity detected"
    return "Normal traffic observed"
