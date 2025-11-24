def load_settings(file_text):
    settings = {}
    lines = file_text.split("\n")
    for line in lines:
        line = line.strip()
        if line == "":
            continue
        if line.startswith("#"):
            continue
        parts = line.split("=")
        if len(parts) != 2:
            continue
        key = parts[0].strip()
        value = parts[1].strip()
        settings[key] = value
    return settings
