def clean_text(text: str) -> str:
    text = text.replace("\t", " ")
    text = text.replace("\r", "")
    text = text.replace("\n\n", "\n")
    text = text.replace("  ", " ")
    return text.strip()


def extract_area_data(text: str) -> dict:
    areas = {
        "Hall": [],
        "Bedroom": [],
        "Master Bedroom": [],
        "Kitchen": [],
        "Bathroom": [],
        "Parking": [],
        "External Wall": []
    }

    for line in text.split("\n"):
        l = line.lower()

        if "hall" in l:
            areas["Hall"].append(line)

        elif "master bedroom" in l:
            areas["Master Bedroom"].append(line)

        elif "bedroom" in l:
            areas["Bedroom"].append(line)

        elif "kitchen" in l:
            areas["Kitchen"].append(line)

        elif "bathroom" in l or "wc" in l:
            areas["Bathroom"].append(line)

        elif "parking" in l:
            areas["Parking"].append(line)

        elif "external wall" in l:
            areas["External Wall"].append(line)

    # remove empty + duplicates
    for key in areas:
        unique = list(set(areas[key]))
        areas[key] = unique

    return areas


def extract_thermal_summary(thermal_text: str) -> str:
    lines = []
    for line in thermal_text.split("\n"):
        if "coldspot" in line.lower() or "hotspot" in line.lower():
            lines.append(line.strip())

    return "\n".join(lines)


def detect_missing_info(text: str) -> list:
    missing = []

    if "Customer Name" in text and ":" in text:
        missing.append("Customer Name: Not Available")

    if "Mobile" in text and ":" in text:
        missing.append("Mobile: Not Available")

    if "Email" in text and ":" in text:
        missing.append("Email: Not Available")

    if "Address" in text and ":" in text:
        missing.append("Address: Not Available")

    return missing


def structure_data(inspection_text: str, thermal_text: str) -> str:
    inspection_text = clean_text(inspection_text)
    thermal_text = clean_text(thermal_text)

    # Extract structured info
    area_data = extract_area_data(inspection_text)
    thermal_summary = extract_thermal_summary(thermal_text)
    missing_info = detect_missing_info(inspection_text)

    structured_input = f"""
STRUCTURED INSPECTION DATA (AREA-WISE):
{area_data}

THERMAL DATA SUMMARY:
{thermal_summary}

MISSING INFORMATION:
{missing_info if missing_info else "None"}

TASK:
- Correlate thermal cold spots with dampness areas
- Identify root causes (plumbing, cracks, waterproofing, tile gaps)
- Avoid repetition
- Be specific per area
"""

    return structured_input