from typing import *
import royalnet.commands as rc
import aiohttp
import io


class DogCommand(rc.Command):
    name: str = "dog"

    description: str = "Invia un cane della razza specificata in chat."

    syntax: str = "[razza]"

    async def run(self, args: rc.CommandArgs, data: rc.CommandData) -> None:
        breed = args.joined()
        if breed:
            url = f"https://dog.ceo/api/breed/{breed}/images/random"
        else:
            url = f"https://dog.ceo/api/breeds/image/random"

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status >= 400:
                    raise rc.ExternalError(f"Request returned {response.status}")
                result = await response.json()
                assert "status" in result
                assert result["status"] == "success"
                assert "message" in result
                url = result["message"]
            async with session.get(url) as response:
                img = await response.content.read()
                await data.reply_image(image=io.BytesIO(img))
