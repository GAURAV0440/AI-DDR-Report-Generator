from extractor import extract_pdf
from processor import structure_data
from ai_engine import generate_ddr


def map_images_to_areas(inspection_images):
    area_map = {
        "Hall": [],
        "Bedroom": [],
        "Master Bedroom": [],
        "Kitchen": [],
        "Bathroom": [],
        "Parking": [],
        "External Wall": []
    }

    for img in inspection_images:
        name = img.lower()

        if "page3" in name:
            area_map["Hall"].append(img)

        elif "page4" in name:
            area_map["Bedroom"].append(img)

        elif "page5" in name:
            area_map["Master Bedroom"].append(img)

        elif "page6" in name:
            area_map["Bathroom"].append(img)

        elif "page7" in name:
            area_map["Kitchen"].append(img)

        elif "page8" in name:
            area_map["External Wall"].append(img)

        elif "page9" in name:
            area_map["Parking"].append(img)

    return area_map


def attach_images(ddr_text, inspection_images, thermal_images):
    area_map = map_images_to_areas(inspection_images)

    image_section = "\n\n---\n## 📸 Area-wise Supporting Images\n\n"

    for area, imgs in area_map.items():
        image_section += f"\n### {area}\n"

        if imgs:
            for img in imgs[:2]:  # limit for cleanliness
                image_section += f"- {img}\n"
        else:
            image_section += "- Image Not Available\n"

    # Add thermal images separately
    image_section += "\n### Thermal Images\n"
    if thermal_images:
        for img in thermal_images[:5]:
            image_section += f"- {img}\n"
    else:
        image_section += "- Image Not Available\n"

    return ddr_text + image_section


def main():
    print("🚀 Starting PDF Extraction...\n")

    try:
        inspection_text, inspection_images = extract_pdf(
            "data/Sample_Report.pdf",
            "outputs/inspection_images"
        )

        thermal_text, thermal_images = extract_pdf(
            "data/Thermal_Images.pdf",
            "outputs/thermal_images"
        )

        print("✅ Extraction Completed Successfully!\n")

        structured_data = structure_data(inspection_text, thermal_text)

        print("\n🧠 Structured Data Preview:\n")
        print(structured_data[:1000])

        # Generate DDR
        ddr_report = generate_ddr(structured_data)

        # Attach images properly
        ddr_report = attach_images(ddr_report, inspection_images, thermal_images)

        print("\n📄 DDR REPORT GENERATED:\n")
        print(ddr_report[:1500])

        # Save output
        with open("outputs/ddr_report.md", "w", encoding="utf-8") as f:
            f.write(ddr_report)

        print("\n✅ DDR report saved as Markdown!")

    except Exception as e:
        print("❌ Error:", e)


if __name__ == "__main__":
    main()