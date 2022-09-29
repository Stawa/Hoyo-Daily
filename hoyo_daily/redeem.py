import requests
import genshin
import asyncio
import pytz
from genshin import Game
from discord_webhook import DiscordWebhook, DiscordEmbed
from datetime import datetime as dt
from typing import Optional


class AutoRedeem:
    def __init__(
        self,
        url: str = None,
        authkey: Optional[str] = None,
        webhook_url: str = None,
        cookies: dict = None,
    ) -> None:
        self.code_url = "https://hoyo-daily.vercel.app/api/v1/codes/"
        self.url = url
        self.authkey = (
            authkey if (authkey) else genshin.utility.extract_authkey(self.url)
        )
        self.webook_url = webhook_url
        self.timestamp = dt.now(pytz.timezone("Asia/Singapore")).strftime("%H:%M")
        self.Client = genshin.Client(
            cookies={
                "ltuid": int(cookies.get("ltuid")),
                "ltoken": cookies.get("ltoken"),
                "account_id": int(cookies.get("ltuid")),
                "cookie_token": cookies.get("cookie_token")
                if cookies.get("cookie_token")
                else None,
            },
            authkey=self.authkey,
        )

    async def auto_redeem(self) -> list:
        try:
            codes = requests.get(self.code_url).json().get("obtainable")["codes"]
            webhook = DiscordWebhook(url=self.webook_url)
            account = await self.Client.genshin_accounts()

            try:
                for i in range(len(codes)):
                    await self.Client.redeem_code(
                        code=codes[i], uid=await self.Client._get_uid(game=Game.GENSHIN)
                    )
                    await asyncio.sleep(5)
            except TypeError:
                return

            embed = DiscordEmbed(
                title="Genshin Impact Redeem Code",
                description=f"━━━━━━━━━━━━━━━━━━━━━━━━━\nUsername: {account[0].nickname} [{account[0].server_name}] ({await self.Client._get_uid(game='genshin')})\nRedeemed Codes: {', '.join(codes)}\n━━━━━━━━━━━━━━━━━━━━━━━━━",
                color="a2006d",
            )
            embed.set_timestamp()
            embed.set_thumbnail(
                url="https://upload-static.hoyoverse.com/event/2021/02/25/f4450e0ef470f777fca0b3dd95813734_1653002626503274756.png"
            )
            embed.set_footer(text="Developed by Stawa")

            webhook.add_embed(embed=embed)
            webhook.execute()

            return codes
        except (genshin.RedemptionException, genshin.RedemptionClaimed) as e:
            return e
