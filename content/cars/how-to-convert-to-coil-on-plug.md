---
title: "How to Convert a Honda B-Series Engine to Coil-on-Plug"
date: 2020-12-18T18:53:13-08:00
draft: false
featured_image: "/img/how-to-convert-to-coil-on-plug/1.png"
tags: ["honda", "crx", "turbo", "how to"]
---

In this guide I’ll be upgrading a Honda B20B engine (from a JDM CRV) in a 1991 CRX Si to coil-on-plug. This method will be largely the same if you have a D, H or F series Honda engines.

![](/img/how-to-convert-to-coil-on-plug/1.png)

In the 90s cars used a mechanical distributor to send high voltage current to the spark plugs in the engine. It was nice and it worked but it can be less precise and is harder to tune, which is important in a turbocharged setup.

![](/img/how-to-convert-to-coil-on-plug/2.png)

Mechanical distributors get their timing by being directly connected to a camshaft using these “teeth” seen below.

![](/img/how-to-convert-to-coil-on-plug/3.jpg)

The cam shaft turns a rotor with in turn distributes power to the contacts inside of the distributor cap.

![](/img/how-to-convert-to-coil-on-plug/4.jpg)

From there, power flows through the spark plug wires to the spark plugs.

![](/img/how-to-convert-to-coil-on-plug/5.jpg)

It’s a beautiful system, however nowadays modern cars control spark via computer. Normally I’m not a fan of handing over mechanical functions in cars to computers but when you are performance tuning an engine for big power and boost it is significant advantage. The goal is to be able to use these coil packs from a 2001–2006 Civic D17 engine to send spark to my cylinders. You can order some [here](https://amzn.to/3nBQySY). This is a non-VTEC B20B. If I was working on a VTEC B-Series I would use K-Series coil packs like [these](https://amzn.to/2J26hMa). Currently these coil packs don’t fit because of the bolt holes that are intended to go into the newer Civic’s valve cover.

![](/img/how-to-convert-to-coil-on-plug/6.png)

I’ll put the coil pack in my vice and chop the bolt ring off with this [Ryobi band saw](https://amzn.to/3p70QuN) because that’s the level of overkill I’m going for today. Non-VTEC B-series engine valve covers do not have holes to bolt down into anyway.

![](/img/how-to-convert-to-coil-on-plug/7.jpg)

Next, I’ll smooth out the rough cut on a belt sander.

![](/img/how-to-convert-to-coil-on-plug/8.jpg)

Now it fits down in the “ditch” of the B-series valve cover.

![](/img/how-to-convert-to-coil-on-plug/9.jpg)

Next I’ll do that 3 more times!

![](/img/how-to-convert-to-coil-on-plug/10.jpg)

Now that I can put computer controlled coil packs in my engine… I need a computer! On the left is the chipped and tuned OBD1 ECU (from an Acura Integra) that was already running my CRX. On the right is another OBD1 ECU that has had a “daughter board” added to control coil packs. This board is made by HondaRuleZ. [AE Race](https://ae-race.com) offers this board pre-installed into a chipped and tuned Honda OBD1 ECU which is a huge time and money saver. AE Race is also the manufacturer of the harness I’ll be using. If the car you’re working on isn’t OBD1 you’ll need to upgrade from an OBD0 ECU or downgrade from an OBD2 ECU depending on what you have, but that is out of scope for this particular guide.

![](/img/how-to-convert-to-coil-on-plug/11.jpg)

Here’s a close-up of the daughter board in the OBD1 ECU from [AE Race](https://ae-race.com).

![](/img/how-to-convert-to-coil-on-plug/12.jpg)

The other critical piece to this puzzle is this aviation grade wiring harness that will connect my ECU to the 4 coils. This is my first part from AE Race but I am really impressed by the quality so far. You can read more about the harness and the ECU kit (as well as order it) at [ae-race.com](https://ae-race.com/products/honda-b-series-coil-on-plug-harness).

![](/img/how-to-convert-to-coil-on-plug/13.jpg)

To install this, I’ll start from the engine bay and feed the end of the harness through the firewall. This is also a good time to install the new ECU which is under the carpet near the passenger’s feet.

![](/img/how-to-convert-to-coil-on-plug/14.jpg)

The other end of the harness has plugs for all 4 coils. You can tell which plug goes to which coil by the lengths of the wire. Starting from the passenger side of the car plug in the shortest cable into the left-most cylinder and then the next shortest, and so on. If you get them in the wrong order it will be obvious and the plugs probably won’t reach the coils. As with any time you are adding wiring in the engine bay take care to route and secure the cables away from anything that gets hot (exhaust) or moves (throttle cable, belts, etc).

![](/img/how-to-convert-to-coil-on-plug/15.jpg)

The harness has 3 more connections to make. A ring terminal for ground (choose a 10mm bolt nearby and secure it) and 2 spade connectors that go into the distributor harness. You will disconnect your distributor from the engine harness and plug these spade connectors in to the distributor side. The plug will have a blue wire and a black/yellow wire. The harness from AE-RACE has a red wire and a white wire. Red is the power source and goes to the side of the plug that matches the black/yellow wire. White is for RPM signal (tachometer reference) and will go into the side of the plug that has the blue wire.

This is really the only part of this install that you can screw up so I’ll say it again:

RED plugs into BLACK/YELLOW.

WHITE plugs into BLUE.

![](/img/how-to-convert-to-coil-on-plug/16.jpg)

“Hold up bro, I thought you didn’t need a distributor anymore?”

You’re right, the distributor won’t be distributing spark anymore, but we still need it for the sensors it has. However, I can get rid of all these spark plugs cables.

![](/img/how-to-convert-to-coil-on-plug/17.jpg)

This next step isn’t strictly required. I could remove the cables and call it a day but since I’m now only using the distributor for its sensor I’m going to pull the distributor and remove the extra internals. Then I can replace the distributor cap with this new delete plate from VMS Racing.

![](/img/how-to-convert-to-coil-on-plug/18.jpg)

I won’t be needing this rotor anymore.

![](/img/how-to-convert-to-coil-on-plug/19.jpg)

Or this coil…

![](/img/how-to-convert-to-coil-on-plug/20.jpg)

With the extra parts removed I can put the low-profile cap and not have exposed electrical contacts on the outside (like a normal distributor cap without cables present).

![](/img/how-to-convert-to-coil-on-plug/21.jpg)

Reinstall the “distributor” the normal way making sure to align the teeth into the camshaft (they should only go one way) and plug the AE Race harness into the distributor plug.

![](/img/how-to-convert-to-coil-on-plug/22.jpg)

With the distributor re-installed I’m going to use [25mm heat shrink wrap ](https://amzn.to/38kb3gC)to secure where the AE Race harness plugs into the distributor harness. Remember, red plugs into black/yellow and white plugs into blue! And that’s it, the install is done!

![](/img/how-to-convert-to-coil-on-plug/23.png)

Tomorrow I will take this to my tuner, Facetuned Tuning, and hopefully squeeze another 10 horsepower out of the engine. Later when I turbocharge this car it will be even more meaningful. Thanks for reading!

![](/img/how-to-convert-to-coil-on-plug/24.jpg)
