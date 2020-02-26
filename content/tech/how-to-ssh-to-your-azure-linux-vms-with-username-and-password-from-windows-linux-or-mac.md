---
title: "How To: SSH to Your Azure Linux Vms With Username and Password From Windows Linux or Mac"
date: 2018-05-27T13:27:18-08:00
draft: false
tags: ["azure", "how-to"]
---

If you’re looking to generate SSH keys and use them to login to an Azure Linux VM then good on you because that’s the recommended and most secure method to access your VMs. It’s readily documented here in official documentation. However, I’ve seen people asking on forums how to simply connect to a Linux VM hosted in Azure via SSH with a username and password. If that’s you then I assume you have a good reason (like this VM will generally not have ports open to the internet or this is a proof of concept) and this post will detail how.

## Create the Linux VM

When you create your VM make sure you’ve chosen “Password” as your authentication type as seen here in Step 1. Choose the username and password that you will use when you connect to this machine.

![Step 1 of the ‘Create virtual machine’ blade.](https://cdn-images-1.medium.com/max/2000/1*aBKDkvZg20O8sY9J9lwK4w.png)*Step 1 of the ‘Create virtual machine’ blade.*

On Step 2 choose whatever size you need. On Step 3 make sure you’re creating a Public IP. The default Network Security Group rules will leave port 22 open for inbound SSH connections so you can leave it as is.

![Step 3 of the ‘Create virtual machine’ blade.](https://cdn-images-1.medium.com/max/2000/1*xyh8O5f68kO5Vg6FgkdCag.png)*Step 3 of the ‘Create virtual machine’ blade.*

The default Public IP settings will generate a dynamic IP address which is fine but you will need to get your IP address from the portal every time it changes in order to connect via SSH. If you plan to SSH to this VM often you may want to set it to static.

![Public IP configuration](https://cdn-images-1.medium.com/max/2192/1*5pGboizGnohsrZxluYNrZw.png)*Public IP configuration*

Complete the wizard and deploy your VM. From the Overview blade of your VM you can see your public IP address; make note of it.

## Connect from Windows

You will need an SSH client. I recommend [PuTTY](https://www.putty.org/) which you can download free from [here](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html). Once you’ve fired up PuTTY put your VMs public IP in the Host Name field and leave the port at the default of 22.

![PuTTY configuration screen.](https://cdn-images-1.medium.com/max/2000/1*WzibaeABg6QgMaINvz75oQ.png)*PuTTY configuration screen.*

Click open and then login with the username and password you chose in the Azure portal and there you go you’re in!

![Ubuntu shell within PuTTY.](https://cdn-images-1.medium.com/max/2000/1*0l2LBbqBiB3u2QPJhB7JIA.png)*Ubuntu shell within PuTTY.*

## Connect from Linux

You may have guessed that establishing a remote connection to a Linux VM from a Linux/GNU machine would be trivial. You were right. From your command line run the following command with the username you chose in the Azure portal:

    ssh <vm username>@<vm ip address>

![Example command from Ubuntu terminal.](https://cdn-images-1.medium.com/max/2568/1*uj6vA1UsknzVZKsrtwhg5w.png)*Example command from Ubuntu terminal.*

Login with the password you created in the Azure portal and you’re in. Your local terminal now acts as the terminal of your VM. You may be warned that the machine is untrusted and you’ll need to type “yes” to add it to list of known hosts.

![Secure shell logged into an Ubuntu Server VM.](https://cdn-images-1.medium.com/max/2568/1*PJ2BTjHDYSZ9uxKBX5gXbA.png)*Secure shell logged into an Ubuntu Server VM.*

## Connect from MacOS

Like Linux, connecting from a Mac doesn’t require additional software. Open your terminal and run the following command where the username is the one you chose in the Azure portal and the IP address is the public IP of your VM :

    ssh <vm username>@<vm ip address>

![Example command from Mac terminal.](https://cdn-images-1.medium.com/max/2280/1*gFqb7g1KSrFmn9r-0Cq8aQ.png)*Example command from Mac terminal.*

You will be prompted for the password you created in the Azure portal and you may be asked to type “yes” to add the VM to your list of known hosts. Your Mac terminal is now a Linux terminal. Sudo away!

![Mac terminal remotely connected to an Ubuntu Server VM.](https://cdn-images-1.medium.com/max/2280/1*mIFDTvxFznTq4BG6OioaFA.png)*Mac terminal remotely connected to an Ubuntu Server VM.*
