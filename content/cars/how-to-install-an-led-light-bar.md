---
title: "How to Install an LED Light Bar"
date: 2021-01-02T16:18:49-08:00
draft: false
featured_image: "/img/how-to-install-an-led-light-bar/1.png"
tags: ["honda", "crv", "how to", "electrical"]
---


Today’s project is installing this [42" LED light bar by Nilight](https://amzn.to/38wDLfx) (for off-road use) on my 2001 Honda CR-V. The mounting of the light will be specific to this light bar and this vehicle but the wiring I demonstrate (which will include a switch in the cabin) will apply to pretty much any kind of auxiliary lighting you want to add to any vehicle.

![](/img/how-to-install-an-led-light-bar/1.png)

The light bar comes with these brackets that are intended to be installed directly to the roof of the vehicle. This requires drilling (and then sealing holes) in the roof. I am going to try to *avoid* drilling through the roof if possible.

![](/img/how-to-install-an-led-light-bar/2.jpg)

I ordered a set of these [tube clamp brackets](https://amzn.to/2JEjpaL) also by Nilight. The brackets are metal but they include different sizes of rubber bushings so you can attach them to difference sizes of bars. My CR-V has the OEM roof rack as well as an aftermarket roof basket so I’m hoping I can find a way that fits and holds the light securely.

![](/img/how-to-install-an-led-light-bar/3.jpg)

This position on the OEM roof rack looks promising. I should be able to attach the brackets that came with the light bar to this.

![](/img/how-to-install-an-led-light-bar/4.jpg)

I’m just mocking it up here. The light will be higher so it lines up with the bolt hole in the top bracket.

![](/img/how-to-install-an-led-light-bar/5.jpg)

Amazingly, the width between the 2 brackets is just right.

![](/img/how-to-install-an-led-light-bar/6.png)

The light bar came with these M8 x 1.25 bolts (and nuts) that were intended to go through the thin sheet metal my roof. They’re not quite long enough for this thick bracket so I’ll need to get different longer ones.

![](/img/how-to-install-an-led-light-bar/7.png)

The hardware store had the correct size, length and thread pitch. My bolts are stainless steel and unfortunately these are not, but hopefully the zinc galvanization holds up to weather anyway.

![](/img/how-to-install-an-led-light-bar/8.png)

It fits. With these brackets are installed and ready to receive the light bar I can move on to the electrical.

![](/img/how-to-install-an-led-light-bar/9.jpg)

You can find online calculators to determine the appropriate gauge of wire for a given device (based on its wattage) but a good rule of thumb is to not use smaller wire than what the device came with. This 240 watt light bar is hardwired with 14 AWG ends and came with no other electrical bits. I’ll be using 14 AWG primary wire and a matching fuse holder. Always fuse anything that’s connected to the battery! I’m also using a standard 30 amp 4-pin relay.

![](/img/how-to-install-an-led-light-bar/10.jpg)

A relay is an electrically operated switch. It allows a low-current circuit (like a switch in your dash) to control a high-current circuit (like one to power lights). We use them instead of connecting our devices directly to the manual switch in the dash because it is inefficient and less safe to draw power for our device back and forth through the car and run it through a switch that is not rated for that much current in the first place.

![](/img/how-to-install-an-led-light-bar/11.png)

The diagram below shows how I’ll be wiring the relay. Standard 4 or 5 pin relays will have their pins numbered this way. A 5-pin relay will have a 5th pin labeled 87a but is not needed for this application. This is typical for any kind of light or other high current device you might be putting in a vehicle. The other wire from the light, the negative input, will of course be grounded to the chassis just like pin 86. If you want more detail about how relays work watch [this video](https://www.youtube.com/watch?v=xvFvJiiDD7w).

![](/img/how-to-install-an-led-light-bar/12.png)

Here is my progress on the wiring. I like using [heat-shrink wire connectors](https://amzn.to/388CqeY) to save time and have a clean secure install. For the ground wire going to pin 86 and the ground wire coming from the light bar I put a ring terminals on the ends so I can secure it to the chassis with one of the many 10mm bolts under the hood.

![](/img/how-to-install-an-led-light-bar/13.jpg)

Now that I have lengthened the wires coming from the light bar so they can reach where the relay will be (near the battery) I can install the light bar in the brackets. I’m running the wrapped wires in the channel on the side of the windshield and into the engine bay. I will use black silicone to make them stay there.

![](/img/how-to-install-an-led-light-bar/14.jpg)

The fused link connects pin 30 directly to the post battery terminal. Pin 87 is connected to the light bar. Pin 86 is grounded to the chassis. The relay itself will be zip-tied in place when I’m done. The last exposed pin is where I need 12v (+) input from the manual switch that has yet to be installed.

![](/img/how-to-install-an-led-light-bar/15.png)

I’ll be using this [rocker switch panel](https://amzn.to/3b0UqcK) from Nilight. Only one switch will be for the light bar and this gives me 4 switches for future projects. It comes pre-wired as shown below. The switches have a common 12v positive and ground input and individual positive outputs. The negative is just needed for the indicator lights.

![](/img/how-to-install-an-led-light-bar/16.png)

I recently discovered these [self-soldering heat-shrink connectors](https://amzn.to/3hDAluu) that I’m using to extend these input wires. I still manually solder mission critical things like fuel injectors but these are nice for jobs like this. You need a heat gun to seal these. I use a [Ryobi cordless heat gun](https://amzn.to/2KLEYH1) but a cheap Harbor Freight one works too.

![](/img/how-to-install-an-led-light-bar/17.png)

The switch panel is going to go over the second DIN location under my stereo. I’ll use this 1/2" paddle drill bit to make a hole in the back to pass wires through.

![](/img/how-to-install-an-led-light-bar/18.png)

And then I’ll remove a couple screws and scrape the skin off my knuckles trying to pass the wires through the hole I drilled and feed them down out the back of the console. This will vary wildly depending on the vehicle and where you mount your switch. It takes some creativity and experimentation.

![](/img/how-to-install-an-led-light-bar/19.png)

Now I have the input wires (positive and negative) as well as the output wire from one of the switches fed through my center console and exiting under the dash near the drivers feet. The output wire will eventually need to get to the relay under the hood but first let’s find input power. I want ignition switched power, power that is only “on” when the key is in the car. This way I don’t have to remember to flip any of these switches off when the car is off and there’s no risk of draining my battery. Fortunately, this Honda has empty locations on the under dash fuse box that provide ignition switched power. If it did not have this I would be splicing into the factory wiring harness to get ignition switched power. I’ll be using this [“add-a-ciruit”](https://amzn.to/3rI6xS9), which is basically a fuse holder with a wire that plugs into a fuse box. Also, I should vacuum my floor mats.

![](/img/how-to-install-an-led-light-bar/20.png)

Here it is plugged into my fuse box with the end leading off to where it is now connected to the input wire from the switch panel.

![](/img/how-to-install-an-led-light-bar/21.png)

The ground wire from the switches can simply be secured to the chassis with the nearest available 10mm bolt.

![](/img/how-to-install-an-led-light-bar/22.jpg)

With the key in I can now flip the switches and have the blue indicator lights come on. Sweet.

![](/img/how-to-install-an-led-light-bar/23.png)

The last step is to feed the output wire from the switches up behind the dash through a grommet in the firewall and over to the relay. I’ve documented similar jobs in this car when [installing a boost gauge](https://joelguerra.com/cars/how-to-install-boost-and-air-fuel-gauges-in-a-turbocharged-car/) and in my CRX [when running wires to the ECU](https://joelguerra.com/cars/how-to-convert-to-coil-on-plug/).

![](/img/how-to-install-an-led-light-bar/24.png)

With that last wire connected to the relay I can wrap some tape around it and zip tie it to the chassis and then flip the switch!

![](/img/how-to-install-an-led-light-bar/25.jpg)

It works great! I’m really pleased with these Nilight accessories. In my opinion their build quality exceeds their price point. They don’t pay me to say this but if you buy through any of the links on this page I may receive a commission. Thanks for reading!

![](/img/how-to-install-an-led-light-bar/26.png)
