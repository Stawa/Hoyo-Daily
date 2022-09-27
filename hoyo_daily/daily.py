import genshin
import asyncio
import pytz
from genshin import AlreadyClaimed, Game
from discord_webhook import DiscordWebhook, DiscordEmbed
from datetime import datetime as dt
from typing import Optional


class AutoCheckIn:
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

    async def genshin_daily(self):
        try:

            reward = await self.Client.claim_daily_reward(game=Game.GENSHIN)
            webhook = DiscordWebhook(url=self.webook_url)
            account = await self.Client.genshin_accounts()

            x = []

            print(
                f"[ {self.timestamp} ] Daily Rewards (GenshinImpact) - {reward.amount}x {reward.name}"
            )

            async for claimed in self.Client.claimed_rewards(game=Game.GENSHIN):
                x.append(claimed.time)

            async for claimed in self.Client.claimed_rewards(game=Game.GENSHIN):
                embed = DiscordEmbed(
                    title="Genshin Impact Daily Sign-in",
                    description=f"━━━━━━━━━━━━━━━━━━━━━━━━━\nUsername: {account[0].nickname} [{account[0].server_name}] ({await self.Client._get_uid(game='genshin')})\nItem Rewards: {reward.name} x{reward.amount}\nToday's Checkin Time: {claimed.time.strftime('%d %B, %Y')}\nTotal Checkin: {len(x)} Days\nStatus: OK\n━━━━━━━━━━━━━━━━━━━━━━━━━",
                    color="0038a8",
                )
                embed.set_timestamp()
                embed.set_thumbnail(url=reward.icon)
                embed.set_footer(text="Developed by Stawa")

            webhook.add_embed(embed=embed)
            webhook.execute()

        except AlreadyClaimed:
            print(
                f"[ {self.timestamp} ] Daily Rewards (GenshinImpact) - Already Claimed"
            )

    async def honkai_daily(self):

        try:
            reward = await self.Client.claim_daily_reward(game=Game.HONKAI)
            webhook = DiscordWebhook(url=self.webook_url)
            account = await self.Client.get_honkai_user(
                uid=await self.Client._get_uid(game=Game.HONKAI)
            )

            x = []

            async for claimed in self.Client.claimed_rewards(game=Game.HONKAI):
                x.append(claimed.time)

            async for claimed in self.Client.claimed_rewards(game=Game.HONKAI):
                embed = DiscordEmbed(
                    title="Honkai Impact 3rd Daily Sign-in",
                    description=f"━━━━━━━━━━━━━━━━━━━━━━━━━\nUsername: {account.info.nickname} [{account.info.server}] ({await self.Client._get_uid(game=Game.HONKAI)})\nItem Rewards: {reward.name} x{reward.amount}\nToday's Checkin Time: {claimed.time.strftime('%d %B, %Y')}\nTotal Checkin: {len(x)} Days\nStatus: OK\n━━━━━━━━━━━━━━━━━━━━━━━━━",
                    color="0038a8",
                )
                embed.set_timestamp()
                embed.set_thumbnail(url=reward.icon)
                embed.set_footer(text="Developed by Stawa", icon_url=account.info.icon)

            webhook.add_embed(embed=embed)
            webhook.execute()

        except AlreadyClaimed:
            print(
                f"[ {self.timestamp} ] Daily Rewards (HonkaiImpact) - Already Claimed"
            )
