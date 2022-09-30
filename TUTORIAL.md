## Locate the `auth_key` from Genshin Impact

**Note: The Powershell script was from [`paimon.moe`](https://paimon.moe/) and it wasn't mine.**

- PC

  1. Open `Wish History` in Game and Wait until it Load
  2. Press START and search `Powershell`
  3. Open the `Powershell` and paste

  ```
  Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex "&{$((New-Object System.Net.WebClient).DownloadString('https://gist.githubusercontent.com/MadeBaruna/1d75c1d37d19eca71591ec8a31178235/raw/702e34117b07294e6959928963b76cfdafdd94f3/getlink.ps1'))} global"
  ```

  4. Copy the link from the output

- Mobile
  1. Coming Soon

## Locate the `ltoken`, `ltuid` and `cookie_token` from HoyoLab.

**Note: The Cookie script was created by [TakaGG](https://www.youtube.com/c/takagg/) and it wasn't mine.**

1. Go to Bookmarks [Chrome](chrome://bookmarks/), [Opera GX](opera://bookmarks)
2. Create a new bookmark with Name `Cookie` and URL

```sh
javascript:(function(){var script=document.createElement("script");script.src="//cdn.takagg.com/eruda-v1/eruda.js";document.body.appendChild(script);script.onload=function(){eruda.init()}})();
```

3. Check the box next to `Show the bookmarks bar` (optional).
4. Click on the 'Cookie' bookmark that you already created
5. Click on the lower right corner and copy all the text
6. Locate and copy the `ltuid`, `ltoken`, and `cookie_token` values.

## Create a Discord Webhook as Notification.

1. Open Your Discord Server
2. Select the channel you want to send the webhook to
3. Edit the channel and select `Integrations`
4. Select Webhook (View Webhook) and click `New Webhook`
5. Copy Webhook URL
6. Edit Webhook Name and Webhook Icon (Optional)
