import aiohttp


async def get_dog_img_url(cli: aiohttp.ClientSession, formats=("jpg", "jpeg", "png")):
    resp = await cli.get(f"https://random.dog/woof.json?include={','.join(formats)}")
    if resp.status != 200:
        return None
    json_response = await resp.json()
    img_url = json_response["url"]
    return img_url
