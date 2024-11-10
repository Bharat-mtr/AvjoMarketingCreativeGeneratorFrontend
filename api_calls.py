import requests


# First API call to get competitor ads
def get_competitor_ads(company_name, product_name):
    url = "https://sour-panther-bharatavjo-fca7ad2f.koyeb.app/analyze-competitor-ads"
    payload = {"company_name": company_name, "product_name": product_name}
    response = requests.post(url, json=payload, timeout=120)
    response.raise_for_status()
    print("the response json is", response.json())
    return response.json()  # Expected to be a list of 5 competitor ad objects


# Second API call to generate creative ideas based on competitor ads
def generate_creative_ideas(competitor_ads, product_name):
    url = "https://sour-panther-bharatavjo-fca7ad2f.koyeb.app/generate-ad-ideas"
    payload = {"competitor_ads": competitor_ads, "product_name": product_name}
    response = requests.post(url, json=payload, timeout=120)
    response.raise_for_status()
    return response.json()  # Expected to be a list of 5 creative ideas


# Final API calls for customized ad generation
def create_final_ad_text(text_idea, company_name, product_name, custom_text):
    url = "https://sour-panther-bharatavjo-fca7ad2f.koyeb.app/generate-marketing-text"
    payload = {
        "idea": text_idea,
        "company_name": company_name,
        "product_name": product_name,
        "user_input": custom_text,
    }
    response = requests.post(url, json=payload, timeout=60)
    response.raise_for_status()
    return response.json()  # Expected to be the final ad text


# Keeping style hardcode as of now
def create_final_ad_image(image_idea):
    return {
        "image_url": "https://img.recraft.ai/b6cLjEzfJGPg4fLSwmCV2U_ACzRyTokSrZARSx2fFo8/rs:fit:1024:1024:0/raw:1/plain/abs://external/images/43d92767-b20c-4caf-90be-2e2629d775fa"
    }
    url = "https://sour-panther-bharatavjo-fca7ad2f.koyeb.app/ggenerate-marketing-image"
    payload = {"prompt": image_idea, "style": "digital_illustration"}
    response = requests.post(url, json=payload, timeout=60)
    response.raise_for_status()
    return response.json()  # Expected to be the final ad image URL
