import genshin
import asyncio
import pytz
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
            },
            authkey=self.authkey,
        )

    async def auto_redeem(self) -> None:
        try:
            x = await self.Client.redeem_code(
                code="GENSHINGIFT", uid=await self.Client._get_uid(game="genshin")
            )
            return x
        except (genshin.RedemptionException, genshin.InvalidCookies) as e:
            return e
