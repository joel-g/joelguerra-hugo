---
title: "Make a Stack Overflow Reputation Leader Board for Your Team With Python"
date: 2018-07-24T17:37:26-08:00
draft: false
tags: ["python", "how-to"]
---


If you’re a developer or student you probably have a Stack Overflow account. If you’re as (overly) competitive as I am you probably compare your Stack Overflow reputation with your colleagues. If you’re a real weirdo you might even want a sort-able leader board to compare yourself against your friends, enemies, etc.

Well, look no further than this simple Python Flask application!

![Screenshot of example leaderboard](/img/make-a-stack-overflow-reputation-leader-board-for-your-team-with-python/1.png)*Screenshot of example leaderboard*

Here is an example of this website in action using myself and some friends: h[ttp://sampleleaderboard.azurewebsites.net](https://sampleleaderboard.azurewebsites.net)

![](/img/make-a-stack-overflow-reputation-leader-board-for-your-team-with-python/2.png)

In order to run your own leader board you will need Python 2 or 3 installed as well as the Flask module; instructions are [here](https://flask.pocoo.org/docs/1.0/installation/).

With those installed fork and clone this GitHub repo:

    https://github.com/joel-g/StackOverFlow_Reputation_Leaderboard_Python_Sample.git

Fire up your code editor and edit app.py. On line 10 you will find a tuple that looks like this STACK_IDS = (’8822629’). The string in the tuple represents my Stack Overflow user ID. Delete my ID and add the IDs of yourself, coworkers, classmates, etc.

To get those precious IDs you’ll need to go to your profile page and the profile page of everyone you want to add to your board. The ID will be in the URL and appear on the page as seen below.

![screenshot of Stack Overflow profile page](/img/make-a-stack-overflow-reputation-leader-board-for-your-team-with-python/3.png)*screenshot of Stack Overflow profile page*

Once you’ve populated the tuple with strings of IDs you’re ready to get a free Stack Exchange API key by registering your [app here](https://stackapps.com/apps/oauth/register).

Once you have a key go back to your editor and app.py. Line 17 looks like:

    res = requests.get("https://api.stackexchange.com/2.2/users/" + user_id + "?order=desc&sort=reputation&site=stackoverflow&key=INSERT_YOUR_KEY_HERE"

Replace INSERT_YOUR_KEY_HERE with the key you just got from Stack Exchange. Save your changes and you should now be able to run the app locally! Run python app.py or flask run from the console and you should see:

    * Running on [http://127.0.0.1:5000/](http://127.0.0.1:5000/) (Press CTRL+C to quit)

Navigate your browser to [http://127.0.0.1:5000](http://127.0.0.1:5000) or localhost:5000 and you should be live! You can sort the list by total reputation, reputation change this month and reputation change this week.

![](/img/make-a-stack-overflow-reputation-leader-board-for-your-team-with-python/4.png)

By now you’re probably thinking “Wow, this is some really basic CSS. I could do better.” Please do! Change the HTML/CSS and show me screenshots of what you made at [@joelatwar](https://twitter.com/joelatwar). Or better yet deploy it to your favorite cloud. My preferred cloud is Azure. If you’d like to deploy it there follow [this guide](https://prmadi.com/running-flask-app-with-httpplatformhandler-in-azure-app-services/). If you deploy your own leader board definitely send me a link!
