from .redeem import *
from .daily import *
from typing import Optional

__name__ = "Hoyo-Daily"
__author__ = "Stawa"
__version__ = "1.0.2"


class HoyoDaily:
    """HoyoDaily - Client for Set Authorization, Cookies, and Webhooks"""

    def __init__(
        self,
        auth_url: str = None,
        auth_key: Optional[str] = None,
        webook_url: str = None,
        cookies: dict = None,
    ):
        self.Daily = AutoCheckIn(
            url=auth_url, authkey=auth_key, webhook_url=webook_url, cookies=cookies
        )
        self.Redeem = AutoRedeem(
            url=auth_url, authkey=auth_key, webhook_url=webook_url, cookies=cookies
        )
