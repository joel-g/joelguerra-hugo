---
title: "API Basics With Postman"
date: 2019-07-01T00:15:44-08:00
draft: false
---

# How to: API basics with Postman — the Martin files

This week I’m stealing all of [Martin Castro's](https://twitter.com/AMartinCastro) hardwork from Twitter (with his permission) to bring you his guide on using Postman to consume APIs. This is a great way to test an API before you starting writing code. The rest of this post is straight from Martin’s thread:

👽 LEARNING THE HARD WAY: API basics with Postman 👽

I am going to use Github’s Noop Challenge — Hexbot to teach y’all about one of biggest tools in my API toolbelt, Postman.

If you’ve never used an API before in your entire life, it’s cool. This is for you bb

![Github tweet about Noop’s Challenge](https://cdn-images-1.medium.com/max/2000/1*Rdg6ELixuSJ2Qw3oNraKcg.png)*Github tweet about Noop’s Challenge*

Github is doing this programming challenge call NOOP which basically means functions that do nothing. It’s stuff that has no purpose. We are just dorking around for the sake of it. I love it. We are going to use [@github](https://twitter.com/github)’s web-exposed API for their first challenge, Hexbot, to try out Postman.

Here’s the Hexbot NOOP challenge: [(noopschallenge.com/challenges/hex…)](https://noopschallenge.com/challenges/hexbot)

I am not going to explain what an API is, or why you should care, or any of that. You don’t care. I don’t care. Nothing matters, everything is pain.

Let’s just talk to the API, yeah? First let’s download Postman. Postman is free software that lets you test APIs. You can test other people’s public APIs, like we will do today.

You can also use it to test APIs you make, and even to automate the documentation (!!!!!) of your APIs. Okay, download Postman: [(getpostman.com/downloads/)](https://www.getpostman.com/downloads/)

![](https://cdn-images-1.medium.com/max/2400/0*x5yLvWf2iaBWdyoD.jpg)

Once you’ve downloaded and installed Postman, if it gives you any tutorial popups, just skip ’em. We are going to do the code equivalent of eating the juicy center of the PB&J and throw away the crust.

I need to create a new Workspace because mine is cluttered. Top center button

![](https://cdn-images-1.medium.com/max/2000/0*NaGJDFKBW3mfdkBY.jpg)

Hit “Create New” and name your Workspace. I named it Github NOOP Hexbot so I don’t accidentally use this workspace for real work later.

I chose a really clever description because I just like the word NOOP. NOOP NOOP NOOP NOOP NOOP NOOP NOOP NOOPNOOP NOOP NOOP NOOP NOOP NOOP NOO

![](https://cdn-images-1.medium.com/max/2000/0*7Kshw8ZPs-9OekQH.png)

![](https://cdn-images-1.medium.com/max/2000/0*oNsRzv6uM7JRXAj8.png)

Here’s the workspace I created.

There’s a buncha buttons and words we don’t need to care about right now.

![](https://cdn-images-1.medium.com/max/2000/0*qmpYSQBduuzdqHyA.jpg)

The API that Github made for Hexbot is super simple, and here is the documentation for it: [(github.com/noops-challeng…)](https://github.com/noops-challenge/hexbot#-api-basics)

![](https://cdn-images-1.medium.com/max/2000/0*qfGU4KTo4kBExmJc.jpg)

There’s only a single API endpoint for it:

An endpoint is the part of the API that receives requests and does stuff with them. We are going to send a request to the Hexbot API endpoint and get some kinda something back. I don’t know what it’s gonna do yet [(api.noopschallenge.com/hexbot)](http://api.noopschallenge.com/hexbot)

We are going to copy paste what’s between quotes here “”

And paste it into where it says “Enter request URL” right in the center of Postman [(api.noopschallenge.com/hexbot)](http://api.noopschallenge.com/hexbot)

![](https://cdn-images-1.medium.com/max/2000/0*t5WX4IGqVGkqQw9U.jpg)

Paste it in, hit send, and what do we have? Without any parameters, the API just sends back a random color in hexadecimal form.

![](https://cdn-images-1.medium.com/max/2000/0*q8-nGH7YcjawXbVQ.jpg)

I wonder what color “[#326688](https://twitter.com/hashtag/326688?src=hash)” is

Drop it into this color-hex site and we see it’s some kind of blue. Neat.

![](https://cdn-images-1.medium.com/max/2000/0*pDqlOFCoHFfVAQpD.png)

The API documentation showed us some parameters. Let’s try them all out.

![](https://cdn-images-1.medium.com/max/2000/0*Ici-EEUieRWBBPkf.png)

If we add “?count=” to the end of our API request, we can get more colors at once. The new API request will read: [(api.noopschallenge.com/hexbot?count=5)](http://api.noopschallenge.com/hexbot?count=5)

![](https://cdn-images-1.medium.com/max/2000/0*bpEQrFEeh-oMdI46.jpg)

It sent me back 5 different colors at once. Let’s try the width and height parameters. These parameters require ranges between 10 and 100,000, so I chose width of 69 and height of 420, because I am a child

Nice.

![](https://cdn-images-1.medium.com/max/2000/0*6cZP_Rz4oJYpDhoY.jpg)

You can also seed the API. The API is not clear what it does with this information. Are we training a world-destroying artificial intelligence? I dunno. But I know based on the Postman GET request output that the API spits out similar-looking hex colors when you seed it this way

![](https://cdn-images-1.medium.com/max/2000/0*5z4EioNlRJjKoC8d.jpg)

🤘🤘🤘🤘

That’s it folks. Today we learned: downloading and installing [@postmanclient](https://twitter.com/postmanclient), setting up a workspace, sending a GET request to a public API, reading API documentation, and experimenting with API parameters. This is basically what I do with every API I find

🤘🤘🤘🤘

Check out this incredibly cool Hexbot someone made: [(aytekk.github.io/hexbot/)](https://aytekk.github.io/hexbot/)

Polka dot party! 🥳🥳🥳

![](https://cdn-images-1.medium.com/max/2398/0*_iE9-dnP4DFJP0Bf.jpg)
