### Locate the `ltoken` and `ltuid` from HoyoLab. 

**Note: The Cookie script was created by [TakaGG](https://www.youtube.com/c/takagg/) and is not mine.**

1. Go to Bookmarks [Chrome](chrome://bookmarks/), [Opera GX](opera://bookmarks)
2. Create a new bookmark with Name `Cookie` and Url `javascript:(function(){var script=document.createElement("script");script.src="//cdn.takagg.com/eruda-v1/eruda.js";document.body.appendChild(script);script.onload=function(){eruda.init()}})();`
3. Check the box next to `Show the bookmarks bar` (optional).
4. Click on the 'Cookie' bookmark that you already created
5. Click on the lower right corner and copy all the text
6. Locate and copy the `ltuid`, `ltoken`, and `cookie_token` values.

### Create a Discord Webhook as Notification.

1. Open Your Discord Server
2. Select the channel you want to send the webhook to
3. Edit the channel and select `Integrations`
4. Select Webhook (View Webhook) and click `New Webhook`
5. Copy Webhook URL
6. Edit Webhook Name and Webhook Icon (Optional)
