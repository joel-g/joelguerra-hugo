---
title: "How to Draw a Dick on the City of Bellevue’s “Report Gatherings” Map With Go"
date: 2020-05-10T12:31:04-07:00
draft: false
featured_image: 'https://miro.medium.com/max/1400/1*Pn9mHkjDJwGl0xEnJ_U5SQ.png'
tags: ["golang", "how-to"]
---

The city of Bellevue, Washington recently debuted an online tool to allow residents to report “gatherings” or other violations of Governor Inslee’s “shelter in place” order. Bellevue Police Department plans to make a heat map to identify areas with high concentrations of violations. This guide will walk through how to reverse engineer an API and use Go’s standard library to send form data. We’ll use the “report a gathering” application as the example API.

Oh, and we’re going to draw a dick on the city’s map with reported “gatherings”.

![Screenshot of Bellevue’s website](https://cdn-images-1.medium.com/max/4212/1*GkL2jqF9SAjYUox6puJAZg.png)*Screenshot of Bellevue’s website*

So, what’s the plan exactly?

1. We’re going to analyze Bellevue’s website to see how we can submit a “report” with code without clicking around on the page.

1. We’re going to plot the coordinates needed to draw a penis.

1. We’re going to write a program that, if we ran it, would report many, many gatherings such that they would draw a dick on Bellevue PD’s map.

## Step 1: Make a report

As always, to see what a website is doing, go to the page and open up the network tab! The site allows you to enter an address, add a description, and optionally add a photo. Instead of an address you can also drag a pointer on the map. I’ll drag the pointer to a park; the page automatically updates with an address when you move the pointer. The page has no warnings about submitting false reports (do not confuse this with a real “police report”) but just so no one thinks this is real and acts on it I’ll add “test report” as the description.

![](https://cdn-images-1.medium.com/max/6720/1*oC4GLs8il5Pci76e1rQiUQ.png)

Next, if we were to click “Submit”, we would see…

![](https://cdn-images-1.medium.com/max/3408/1*u73Kp0rNjWcLMnhdyoLdYQ.png)

There would be a flood of activity in the network tab. We’re not interested in images and other assets that get loaded so let’s filter by “XHR” and look for the payload our browser hypothetically would have sent to the server.

![](https://cdn-images-1.medium.com/max/2800/1*SmmauL1J3ppRfpOr38oV9Q.png)

Right away we see something called “request_submit” that returned a 200. That looks promising! If we drill down we see the request URL (we’ll need that later), the request and response headers and if we scroll down we find the real prize… the format of the form data that would be sent!

![Network tab results](https://cdn-images-1.medium.com/max/3380/1*ercdQCmgp-hz1tQoYAzpSQ.png)*Network tab results*

![Form data](https://cdn-images-1.medium.com/max/2452/1*zkQU65DzcI6R2txWh6woWQ.png)*Form data*

We can see that the pin drop on the map was translated to latitude and longitude coordinates. That’s going to be really useful when we want to draw a picture later. Armed with this information, let’s head to our editor and write some code to recreate this functionality.

The first thing we’ll do is store that request URL and make a simple function that will take latitude and longitude coordinates as string arguments.

![](https://cdn-images-1.medium.com/max/2576/1*etf3_EBvnWas1Jtz-PdpBA.png)

From the form data we got found in the network tab we have values for space_id, client_id, request_type_id. We don’t know exactly what those values mean but since we weren’t logged in or authenticated in any way "client_id": "954" is probably the code for an anonymous report, maybe? And request_type_id almost certainly refers to the “gathering” type of report (Bellevue lets you report other things as well like… Lime Bikes for some reason). Whatever these numbers mean, we’re going to hard code them to match what we saw in our test report.

What we really care about is the latitude and longitude! We’re going to be using the [PostForm()](https://golang.org/pkg/net/http/#Client.PostForm) function from Go’s http package. Since this function takes a [url.Values](https://golang.org/pkg/net/url/) type as an argument we’ll have our function return a urls.Values type. This type is based on a map of a string/slice-of-string (map[string][]string) so we can populate our url.Values literal like this, inserting our latitude and longitude values as strings:

![](https://cdn-images-1.medium.com/max/2524/1*3sqif7u8XpQr7mbaVEs7tQ.png)

Now that we can generate the arguments we need for our HTTP request, let’s fill out the main() function to do just that using the same latitude and longitude from that park earlier. We’re not animals so we’ll check for errors and print any we find, but more importantly we’ll print the HTTP status code we get from our POST request. You can read more about HTTP requests in Go [here](https://gobyexample.com/http-clients).

![](https://cdn-images-1.medium.com/max/3112/1*hFaLXuOxiCMmmV9C5cWIeA.png)

And if we were to run it…

![](https://cdn-images-1.medium.com/max/2000/1*fHoZOmvfKgOGqWI_oCDAPw.png)

No errors and a 200 OK response. Nice!

At this point we’ve written code that (if we were to run it) would create a single “gatherings” report on Bellevue’s website. We did it with a single pair of hard coded of latitude and longitude coordinates but if we want to draw anything we’ll need a list of many coordinates. On to step 2!

## Step 2: Draw a dick with latitude and longitude coordinates

Google Maps provides many public APIs relating to maps (duh). We’ll use an existing [open source project](https://github.com/jeremy-hawes/google-maps-coordinates-polygon-tool) that leverages one of their APIs and allows you draw a polygon on the map and returns a set of coordinates. You can play with the Codepen [here](https://codepen.io/jhawes/pen/ujdgK).

![](https://cdn-images-1.medium.com/max/6716/1*J1N8bKG42U9QGCdw3y9PlQ.png)

The tool allows you to drag the polygon around the map and add more sides until it becomes… a masterpiece. I’m no graphic artist but if I may say so myself, I think this is a pretty good depiction given the medium. I had to be very careful to draw all the dots within the boundaries of the city’s map.

![](https://cdn-images-1.medium.com/max/3292/1*Pn9mHkjDJwGl0xEnJ_U5SQ.png)

The Codepen outputs the latitude and longitude coordinates that we’ll need in our Go code. Just for safe keeping, I’ll paste them right here:

{“47.62266”, “-122.14746”}, {“47.62018”, “-122.15174”}, {“47.61817”, “-122.15405”}, {“47.61615”, “-122.15705”}, {“47.61178”, “-122.16218”}, {“47.60695”, “-122.16971”}, {“47.60096”, “-122.17655”}, {“47.59633”, “-122.18569”}, {“47.5921”, “-122.1864”}, {“47.58649”, “-122.18436”}, {“47.58313”, “-122.17973”}, {“47.57977”, “-122.17097”}, {“47.57843”, “-122.16683”}, {“47.57754”, “-122.16269”}, {“47.57717”, “-122.15372”}, {“47.57715”, “-122.14572”}, {“47.57922”, “-122.13737”}, {“47.58591”, “-122.13304”}, {“47.59462”, “-122.13622”}, {“47.5973”, “-122.1401”}, {“47.59874”, “-122.14784”}, {“47.60208”, “-122.14239”}, {“47.60669”, “-122.13591”}, {“47.61084”, “-122.13012”}, {“47.61355”, “-122.12514”}, {“47.61856”, “-122.11878”}, {“47.62212”, “-122.11054”}, {“47.62575”, “-122.10951”}, {“47.62942”, “-122.1083”}, {“47.63309”, “-122.10779”}, {“47.63536”, “-122.10949”}, {“47.63759”, “-122.11186”}, {“47.63952”, “-122.11729”}, {“47.63689”, “-122.12815”}, {“47.6343”, “-122.13332”}, {“47.62986”, “-122.13643”}, {“47.62634”, “-122.14194”}

We’ll need to add them as a slice of slices of strings in our Go code too.

![](https://cdn-images-1.medium.com/max/4968/1*srTSrCrxzYC0x-TRIYBZiw.png)

## Step 3: Finalize the script to use the coords

The obvious last step is to write a for loop to iterate over the coordinates and “report a gathering” for each coordinate but there’s one last thing missing here… the description. We haven’t come up with a good description. If there is one thing I think government officials, politicians and police officers should frequently read it is the US constitution. Let’s add a constitutional amendment as the description to each report!

First, we’ll need to gather the first 10 amendments into a slice of strings.

![](https://cdn-images-1.medium.com/max/4876/1*bULCM-v5l8Y1xniFGkT9ng.png)

Let’s wrap this in a function that will return just one of them randomly. The function Intn() from Go’s rand package takes an integer as an argument and returns a random integer between 0 and that number (non-inclusive of that number). So rand.Intn(10) will give us any number from 0–9.

![](https://cdn-images-1.medium.com/max/2000/1*XA7AKbDNzPU407IUHX0lPA.png)

It is true that Go’s rand.Intn() doesn’t offer true randomness and every time we run this we’ll get the same “random” numbers in the same order but for our purposes that is just fine. Let’s incorporate our new randomAmmendment() function in our generateReportBody() function from before.

![](https://cdn-images-1.medium.com/max/2000/1*V2uiHcAFQwF8_6BZBgx6JA.png)

Now that we have a complete reports with coordinates and descriptions we can write the loop. Nothing fancy here, just a loop over the slices of strings:

![](https://cdn-images-1.medium.com/max/2416/1*QmFqy9ghDpib9FMg7078Lw.png)

The last thing we should do with this program is consider rate limiting. We don’t know what the Bellevue website’s API would do if we were to send all the reports at once but it would be somewhat rude to spam their API like that anyway. A simple solution is to add a sleep timer between each report with time.Sleep(60 * time.Second) . This will make the program wait 1 minute between reports. That does mean the program will run for 36 minutes before it finishes the 37 reports (for the 37 coordinates) but that’s okay.

![](https://cdn-images-1.medium.com/max/2380/1*Kg9ejWg8zvuChCLu5NBwvw.png)

## That’s it!

We did it! We have a complete Go program that could create 37 “gathering reports” and use them to draw a big ole dong on the City of Bellevue’s map! You can see the complete code here: [https://github.com/joel-g/form-data-with-go](https://github.com/joel-g/form-data-with-go/blob/master/main.go)

I, of course, would never run this code because I so deeply respect the important job that our local government officials are doing when they restrict our freedoms to prevent such nefarious acts such as:

* jogging

* biking

* BBQing

* pushing our children on a swing set

But seriously folks, please don't place your neighbors in mortal peril by forcing them to have face-to-face confrontations with police. Social distancing is important but calling police on people is not cool.