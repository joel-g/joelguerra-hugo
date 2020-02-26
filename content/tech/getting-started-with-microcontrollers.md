---
title: "Getting Started With Microcontrollers — the Martin files"
date: 2019-06-16T00:08:14-08:00
draft: false
tags: ["hardware", "martin"]
---


My buddy [Martin Castro](https://twitter.com/AMartinCastro) likes to live tweet hardware projects. When he’s done you have a detailed step-by-step guide that anyone can follow along. However, since it’s a Twitter thread it is quickly lost to time. “The Martin Files” is my attempt to capture this content (with his permission) so others can find, read and learn from it in the future. The rest of this article (including the images) will be verbatim from his Twitter thread:

🖥️ **LEARNING THE HARD WAY**: Microcontrollers for Newbs 🖥️

Y’all wanted more hardware so… today we’re going to play with the BBC micro:bit ([https://amzn.to/2Ecs3XU ](https://t.co/CQpQBF79GU)) We’re going to do some simple projects because ANYONE can do this stuff, even if you don’t know a lick of code.

![](https://cdn-images-1.medium.com/max/2000/1*ozPoO5LbDWFd1FwR0izZYw.png)

This is dedicated to [@joelatwar](https://twitter.com/joelatwar) because he said I was a poor man’s [@shanselman](https://twitter.com/shanselman) and I want to prove him right

First up, the basics. The BBC micro:bit is the perfect starter for hardware hacking because it is SO DAMN EASY. It connects to your computer with a standard micro USB cable.

![](https://cdn-images-1.medium.com/max/2000/1*I8KERO6CJJ_7sOrFjzFJ1Q.png)

Writing code to this thing is very newb-friendly because you can do it from a browser without ever actually writing code using what [@Microsoft](https://twitter.com/Microsoft) calls “Blocks”. [https://makecode.microbit.org/#editor](https://t.co/bAmd9cCG8F)

![[https://makecode.microbit.org/#editor](https://t.co/bAmd9cCG8F)](https://cdn-images-1.medium.com/max/2110/0*j5kkRlWiT5I0bbcp.jpg)*[https://makecode.microbit.org/#editor](https://t.co/bAmd9cCG8F)*

![Chrome console](https://cdn-images-1.medium.com/max/2000/0*9fbsdMoyKo2uA1bu.png)*Chrome console*

The first little project we’re going to do is lighting up some LEDs on the front of this sucker. Lighting up LEDs is like the classic “Hello World” problem of hardware hacking.

In the editor, click “Basic”, grab “show leds”, and drag that son of gun right into the “Forever” slot.

![](https://cdn-images-1.medium.com/max/2000/1*Ke0ST27Nh7lAzU-OoGgUOw.png)

Here’s the editor again: [https://makecode.microbit.org/#editor](https://makecode.microbit.org/#editor)

Dragging Blocks into the “Forever” slot makes any code in the slot run as long as the micro:bit is drawing power. Dragging it into the “On start” slot makes it run when the micro:bit fires up, and until all the instructions are completed.

![](https://cdn-images-1.medium.com/max/2000/0*CYqJ1e6fTv_Y3raY.png)

I made a little design that’s like a rocket ship, or a Christmas tree, or arrow or something IDK. I’m not an artist.

![](https://cdn-images-1.medium.com/max/2000/0*dEzfDMArW8ixo-Ch.png)

If you click “{ } JavaScript” at the top, it toggles between Blocks and JavaScript code. If you’re already familiar with JS, you will recognize that showLeds() is a prebuilt function that takes a template literal as an argument to send signals to the LED hardware.

What else do we need to do to run this? Not much. The micro:bit just shows up as a USB drive on your computer, so just click “Download” in the editor, find the file in your downloads, and drag it to the MICROBIT drive.

![](https://cdn-images-1.medium.com/max/2162/0*F_HxsR8dqUeKAegd.jpg)

![](https://cdn-images-1.medium.com/max/2000/0*dYo867DHqIdHndve.png)

![](https://cdn-images-1.medium.com/max/2400/0*oiFKrMmkm5GkXoxM.jpg)

THAT’S LITERALLY IT. We have done a thing. Neato.

![](https://cdn-images-1.medium.com/max/2000/1*fj_VTnFBlYjorTkdaCepKQ.png)

Okay I hope you guys see how easy this is for a literal zero-code beginner to do this stuff. The only things you will need is $20 to buy the micro:bit, a computer with a USB slot, a browser, and the ability to follow the most basic of instructions.

YOU GOT THIS.

![Zamioculcas zamiifolia](https://cdn-images-1.medium.com/max/2000/0*yisoeNIYJ_RtBXTs.jpg)*Zamioculcas zamiifolia*

So let’s turn up the volume and do some! More! Interesting! Stuff!

Enter Stage Right one of my office plants. Internet, please meet Juliet, my 3-year old Zamioculcas zamiifolia, native to Eastern Africa and dentist office waiting rooms.

The Zamio… whatever it’s called, needs to be watered approximately every 2 weeks, but because of the dry climate, knowing when to water it is tricky. I am going to write a little program for the BBC micro:bit that checks the water moisture so I can see when to water!

For this little project, we need Juliet, the micro:bit, one of those little black metal binder clips, and two sets of alligator clips.

![](https://cdn-images-1.medium.com/max/2788/1*MU6GIi2cYiunrE_QEXSddQ.png)

Pull the handles off the binder clip and just stick ’em right in the dirt. We’re going send a little electricity into these dudes, and the electrical resistance created by the water in the soil will tell us how much moisture is in there.

![binder clips in a potted plant](https://cdn-images-1.medium.com/max/2000/1*YAhWACEEqtSSxrnwFItxMg.png)*binder clips in a potted plant*

![](https://cdn-images-1.medium.com/max/2000/0*3G189utR1ESm_a0c.png)

Clip one of the alligator clip ends to the tab labeled “3V” and the other to the tab labeled “0”. Clip the opposite ends of the clips to the binder clip handles in the plant.

![](https://cdn-images-1.medium.com/max/2000/1*wpzhJUKIiQrTymqXSeTHjw.png)

When you plug the micro:bit into the computer again, it will still be running the arrow/tree LED light code. It will keep whatever the latest code was in memory. So let’s write the code that makes it test the soil moisture. Back to the editor! [https://makecode.microbit.org/#editor](https://makecode.microbit.org/#editor)

![](https://cdn-images-1.medium.com/max/2000/0*ILHKdV5m3zrboHTv.png)

First thing we’ll do is make a variable to hold the moisture data. Click Variables, Make a Variable, and name it something Extremely Creative, like “moisture”.

![](https://cdn-images-1.medium.com/max/2000/0*2OF2t9n15K01raOV.png)

Grab “Set moisture to 0” and drag it into the “Forever” block.

![](https://cdn-images-1.medium.com/max/2000/0*rMVIpOl2_QG9WqAj.png)

Then go to “Advanced”, “Pins”, and “analog read pin”. Drag THAT into the “0” in the “Set moisture to 0” block.

![](https://cdn-images-1.medium.com/max/2000/0*fK1-UncMVgmgDWzw.png)

![](https://cdn-images-1.medium.com/max/2784/1*JWqUgwubE7YdxPpDd2LdlA.png)

In JavaScript, we just declared a variable named “moisture”, and set moisture equal to the return value from a function that takes a reading from Pin 0.

Cool right?

![](https://cdn-images-1.medium.com/max/2000/0*Zfzi9DSK70XkZt-W.png)

Now go to LED blocks, and choose “plot bar graph of 0 up to 0”, drag it under our variable, then go back to Variable blocks, grab “moisture”, and set it as the input. This will make the LED receive signals from that variable.

![](https://cdn-images-1.medium.com/max/2000/0*Uu2DHDMNnPBjvAyk.png)

![](https://cdn-images-1.medium.com/max/2000/0*WnCVMlq_lbVuH8oI.png)

Set the “Up to” number to 1023, the highest it will go. Now let’s get some conditional logic in here.

![](https://cdn-images-1.medium.com/max/2000/0*puT-F0R8J3dYRLMu.png)

Click Logic blocks and select “If true then” and drop it right under. We’re going to make a button do stuff.

![](https://cdn-images-1.medium.com/max/2000/0*dT2ZpMLRXRM8DOtn.png)

Click Input blocks, and drag “button A is pressed” into the space where “true” was in the conditional block.

![](https://cdn-images-1.medium.com/max/2000/1*PRXCCqeGE_lq_BlmMYPSUQ.png)

Click Basic blocks, grab “show number” and put it as the output block in the conditional logic. Then go to Variables blocks, grab “moisture”, and drop it in where “0” was. We maek butan.

![](https://cdn-images-1.medium.com/max/2000/1*vP1Ie2gMR3plswEwgTvykw.png)

Download the code, drop it in the MICROBIT folder and…..

![](https://cdn-images-1.medium.com/max/2000/1*p-u-l3zdFmtU0lOKsSDIgQ.png)

EXTREMELY MOIST

![](https://cdn-images-1.medium.com/max/2400/0*H_Kg8gjtDeKVA5zS.jpg)

We did the entire damn thing you guys. We wrote code that sends power through the dirt in a flower pot, testing the resistance of said dirt, storing that resistance as a variable, and printing the output of that variable to LED screens on a microcontroller
