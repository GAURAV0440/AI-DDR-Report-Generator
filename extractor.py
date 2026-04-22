import fitz
import os


def extract_pdf(pdf_path: str, output_folder: str):
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"❌ File not found: {pdf_path}")

    doc = fitz.open(pdf_path)

    text_parts = []
    images = []

    os.makedirs(output_folder, exist_ok=True)

    MAX_IMAGES_PER_PAGE = 5

    for page_num in range(len(doc)):
        page = doc[page_num]

        # -------- TEXT EXTRACTION --------
        page_text = page.get_text("text")
        if page_text:
            text_parts.append(page_text.strip())

        # -------- IMAGE EXTRACTION --------
        image_list = page.get_images(full=True)

        for img_index, img in enumerate(image_list[:MAX_IMAGES_PER_PAGE]):
            try:
                xref = img[0]
                base_image = doc.extract_image(xref)

                image_bytes = base_image.get("image")
                image_ext = base_image.get("ext", "png")

                width = base_image.get("width", 0)
                height = base_image.get("height", 0)

                # ❌ Skip small/icon images (UI elements)
                if width < 120 or height < 120:
                    continue

                # ❌ Skip very tiny file size images
                if len(image_bytes) < 5000:
                    continue

                # ✅ Save valid image
                image_name = f"page{page_num+1}_img{img_index+1}.{image_ext}"
                image_path = os.path.join(output_folder, image_name)

                with open(image_path, "wb") as f:
                    f.write(image_bytes)

                images.append(image_path)

            except Exception:
                continue

    doc.close()

    full_text = "\n".join(text_parts)

    return full_text, images