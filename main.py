import json
import requests
import image_functions as img
import pdf_functions as pdf


def initialise_config(path: str)-> dict:
    try:
        with open(path, "r") as f:
            config = json.loads(f.read())
    except Exception as e:
        print(f"Unable to initialise project {e}")
        exit(1)
    return config





if __name__ == '__main__':
    config = initialise_config("config.json")
    # print(config)
    # image_url = img.get_dog_image_url(config['rest_api_url'])
    # img.save_image(image_url)
    # print(image_url)
    # img.show_images()
    pdf.create_pdf("pdf.pdf")
