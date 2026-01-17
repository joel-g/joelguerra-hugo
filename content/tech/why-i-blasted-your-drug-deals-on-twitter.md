---
title: "Why I Blasted Your Drug Deals on Twitter"
date: 2018-07-20T17:33:20-08:00
draft: true
tags: ["python"]
---

## How it happened

A couple of days ago Twitter user [Mike Rundle]() tweeted a link for the endpoint to Venmo’s public API. I learned that Venmo’s public by default setting made the details of millions of Venmo transactions publicly available to anyone who cared to look. So I did what any software engineer would do and started digging through the data. I could see the names, Facebook profile pictures, payment types and “message” fields that users filled out when they made a transaction.

I thought about the many times I had filled that out myself with joke descriptions like “baby oil backrub” or “plan B pills” when splitting restaurant tabs with friends. I could see that I’m not the only one who likes to put salacious descriptions on their transactions but unlike my Venmo account all of these users had their transactions set to “public” instead of “private”. The Venmo app’s default setting is public and it’s up to users to realize that and change their settings if they don’t like it.

## What I did

I wanted to do something creative with this to demonstrate the lack of privacy in Venmo’s default settings. I already run a squad of Twitter bots doing harmless things like [spreading news about the Seattle Mariners](https://twitter.com/reddit_mariners) and giving users the [contact information for their members of congress](https://twitter.com/findyourreps) upon request so another Twitter bot was a natural choice. *I actually don’t care for the term “bot” because it implies some sort of AI when they’re really just running a set of pre-programmed commands on a loop but that’s a discussion for another day.*

Anyway, writing a Python script is generally my solution to everything so I slapped together 70 lines of code and made a new Twitter account and let it run. It was automatically tweeting the names of profile pictures of users making “drug” transactions on Venmo. I chose drugs, sex and alcohol keywords as the trigger for the bot because because they were funny and shocking. I removed the last names of users because I didn’t want to actually contribute to the problem of lack of privacy.

![Screenshot of the Twitter account](/img/why-i-blasted-your-drug-deals-on-twitter/1.png)*Screenshot of the Twitter account*

## What came next…

I tweeted out a link to the new account [*“Who’s buying drugs on Venmo”](https://twitter.com/venmodrugs)* less than 2 hours after Mike’s original tweet that inspired me expecting to get a few laughs from my friends and colleagues and that would be the end of it. I was wrong. Accounts with tens and hundreds of thousands of followers had caught wind of the account and its mentions were blowing up. I braced myself for backlash but the response was overwhelmingly positive.

![](/img/why-i-blasted-your-drug-deals-on-twitter/2.png)

![Screenshot of Twitter notifications](/img/why-i-blasted-your-drug-deals-on-twitter/3.png)*Screenshot of Twitter notifications*

People understood my point and I had sparked a lot of discussion about online privacy and the need for users to do a better job of understanding the terms of software they were using — and a lot of discussion about how companies need to do a better job of informing customers how their data was being used.

By the next morning I had Vice News in my inbox asking for comment. By mid afternoon CNET, Mercury News and a half dozen other websites had posted articles about it. Not used to seeing my name on news websites, I cringed as I read expecting to get blasted — but I wasn’t.

[Marrian Zhou](undefined) of CNET [wrote](https://www.cnet.com/news/how-to-get-caught-buying-drugs-on-venmo-this-twitter-bot/):
> “@venmodrugs highlights the public nature of the payment service’s transaction histories, which are public by default. Whether you’re really buying drugs or just joking around with friends, the [Twitter](https://www.cnet.com/tags/twitter/) bot serves as a reminder that your Venmo transactions are open for all to see and you should ‘consider setting your transactions to private.’”

[Joseph Cox](undefined) of Motherboard [wrote](https://motherboard.vice.com/amp/en_us/article/qvmkvx/twitter-bot-venmo-buying-drugs-photo-names):
> The bot raises questions not only about whether users are truly aware of the sort of data they are exposing by not using certain account settings, but also at which point does already public data qualitatively take on a different meaning or significance when compiled in aggregate and presented in new formats.

[Seung Lee](https://seungylee.tumblr.com/) of San Jose Mercury News [wrote](https://www.mercurynews.com/2018/07/20/venmo-a-friend-about-drugs-or-sex-and-this-twitter-bot-will-rat-you-out/):
> The word on the street has always been snitches get stitches. But one tattletale Twitter bot flies right into the age-old adage by disclosing Venmo users who tag their transactions with words or emojis related to drugs — all for the sake of promoting data privacy.

In reading these articles I learned about Hang Do Thi Duc who had recently published [research](https://publicbydefault.fyi/) about Venmo’s ‘public by default’ privacy settings and one of my favorite comments came from [Tristan Greene](https://thenextweb.com/author/tristangreen/) of [TheNextWeb](https://thenextweb.com/artificial-intelligence/2018/07/19/twitter-bots-are-running-amok-with-your-public-venmo-data/):
> Hang’s the angel on your shoulder trying to keep you safe. And, if you look to your other side, you’ll see the devil in the form of a bot that tweets the names and faces of Venmo users who are referencing drugs and sex in their transactions. …
> …And, in the spirit of fairness, the method he chose to demonstrate his point seems like it would be an effective one. Where Hang’s work, which we [wrote about](https://thenextweb.com/security/2018/07/17/this-visualization-of-venmos-public-data-is-terrifying/) earlier this week, uses anonymized data and clever visualizations to show how a person’s public data could be exploited, Guerra sort of rubs people’s face in it like a dog who’s pissed on the rug.

## So I killed it

After about 24 hours of tweeting everyone’s drug laden Venmo transactions I shut down the bot (*Python script!!*) and deleted all the tweets. I had successfully made my point and gotten more attention than I had imagined possible. Thousands of people were reading tweets and articles about the bot and discussing data privacy. I saw no further value in tweeting out anyone’s personal transactions anymore.

However, all I ever did was format the data and automate a Twitter account — the data is still readily available. Click this link for [Venmo’s](https://venmo.com/api/v5/public?limit=1000) API and you’ll see all the details of the last one thousand Venmo transactions including last names and usernames that I chose not to include in my bot’s tweets.