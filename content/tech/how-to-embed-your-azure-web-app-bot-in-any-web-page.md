---
title: "How To: Embed Your Azure Web App Bot in Any Web Page"
date: 2018-05-27T13:18:41-08:00
draft: false
tags: ["azure", "how-to"]
---

Embedding an Azure bot in your web page is actually very simple but the Azure portal doesn’t make it obvious how to do this. The portal blade for bots is geared towards developers who are integrating bots into channels like Skype, Facebook Messenger, Slack, SMS, etc but I’ve seen several questions on Stack Overflow asking how to simply slap the bot on a web page - so here you go.

Start by navigating to your bot in the portal and select the Channels blade:

![](https://cdn-images-1.medium.com/max/2000/1*g1twn4ISo3MVyRM-hBlPww.png)

Ignore the many channels offered and choose “Get bot embed codes” and on the next screen choose “ Click here to open the Web Chat configuration page”.

![](https://cdn-images-1.medium.com/max/2324/1*DfrBjvg_bIB37u8gMTIBJw.png)

From the final screen you can “Show” your secret key and use it in the code snippet supplied to embed your bot in any web page.

![](https://cdn-images-1.medium.com/max/2000/1*JQ5wxySbvIbfqZs8WOn1IQ.png)

You can set the size of the `<iframe>` with ‘width’ and ‘height’ tags or add a class to position and size the frame with CSS and off you go.

**Note**: This isn’t as secure as using Channels or the REST endpoint because your key will be visible in the DOM to anyone who cares to inspect your web site. This would allow others to embed your bot in their web page which may not be acceptable depending on your use case.
