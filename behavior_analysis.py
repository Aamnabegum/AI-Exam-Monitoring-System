def update_suspicious_count(status, count):
    if "Suspicious" in status:
        count += 1
    return count
