---
title: "Agent Docket: Keeping Track of Open Threads With AI Agents"
date: 2026-11-08T12:00:00Z
draft: false
description: "A Cloudflare Worker, a small CLI, and a TRMNL display for tracking who has the next step on tasks that span days or weeks."
summary: "I built Agent Docket to keep track of tasks I work on with AI agents over days or weeks, from waiting on someone else's reply to making a decision myself."
featured_image: "/img/agent-docket/trmnl-display.png"
featured_image_alt: "Agent Docket on a TRMNL e-ink display, with three items under Needs you and two under Waiting on others."
tags: ["ai", "cloudflare", "trmnl"]
---

Some tasks you give a personal agent can take days or weeks. I'll use shopping for car insurance as an example. You ask a few insurers for quotes, one sends a price the next day, and another needs your annual mileage before they can finish. An AI agent can help you keep the quotes straight, but there's still a lot of time when the next step belongs to you or someone you're waiting on.

I built Agent Docket for work that happens in bursts over days or weeks. It puts open tasks on a [TRMNL](https://trmnl.com) e-ink display so I can see who has the next step without reopening each chat. The display has two columns: **Needs you** and **Waiting on others**.

While the quotes are coming in, “Compare car insurance quotes” sits under **Waiting on others**. If an insurer asks for my mileage, the AI agent can move that same item to **Needs you** and say what I need to send. Once I've replied, it can move the item back. When the quotes are ready, the item goes under **Needs you** again so I can compare them and pick a policy. Then the agent can take it off the docket.

![Agent Docket on a TRMNL e-ink display. The Needs you column includes follow-ups with PEMCO and Grundy. Waiting on others lists NameCamper Instagram check metrics and a State Farm rerate.](/img/agent-docket/trmnl-display.png)

## From a command to the screen

The backend is a Cloudflare Worker with KV storage. An agent sends an authenticated HTTP request, the Worker saves the updated docket, and then it sends a compact version to a TRMNL private plugin through a webhook. A Liquid template turns those variables into the two-column layout.

There's no model running in the Worker. It doesn't need to know which agent made the request, and it doesn't read conversations to figure out what belongs on the docket. The agent has to do that part. Anything that can make the HTTP requests can use it.

For agents that can run a shell command, I added a dependency-free Node CLI. It wraps the API so the agent can spend less time assembling requests and more time doing whatever I asked it to do.

Here's an example. From the Agent Docket checkout, with the Worker URL and Docket token already configured:

```sh
node bin/docket.js list --json
node bin/docket.js add --title "Compare car insurance quotes" --detail "Send annual mileage for the last quote" --group needs-you --json
```

The first command matters. If the insurance task is already on the docket, we should update that item as the quotes come in instead of adding another one.

The create response includes an item ID. Use that ID in place of `ITEM_ID` below when the next step belongs to somebody else:

```sh
node bin/docket.js update ITEM_ID --detail "Waiting for the final quote"
node bin/docket.js move ITEM_ID waiting-on-others
```

Run mutations sequentially, at least a second apart. When the work is finished and removal is authorized:

```sh
node bin/docket.js delete ITEM_ID
```

Each change attempts to update TRMNL. The physical screen still follows its refresh schedule, so a successful webhook response doesn't mean the pixels have changed yet.

## Give the agent a useful job

The repository includes an `AGENTS.md` file with guidance for working with the docket. Keep the title short, make the detail say what needs to happen, reuse the item's ID, and check whether an operation actually succeeded.

“Compare car insurance quotes” tells me what I'm doing, and “Send annual mileage for the last quote” tells me what I can do today. The optional source label can tell me which agent or workflow put it on the board, and a reference URL stays available through the API.

Items can also have a due date and a kind: topic, reminder, or todo. A reminder is an item on the screen. There's no scheduler hiding behind it that will send a notification at 9am. Due dates affect sorting.

The display fits four items per column, with a count for anything beyond that. It puts due dates first, then sorts by the most recent change. Longer text gets clipped for the screen; the API keeps the full stored details and reference URLs. The template targets an 800x480 display, so concise text earns its keep. Use plain text rather than emoji for reliable monochrome rendering.

## Saved and displayed are separate outcomes

One detail that matters for an agent is what happens when the item saves but the webhook fails.

The Worker writes to KV before calling TRMNL. Suppose the item saves successfully, then TRMNL rejects the webhook or the request times out. Repeating the original `add` could create a second item. Now the board has two reminders to send the same mileage figure, which isn't much of an improvement.

The API reports storage and delivery separately. The CLI returns exit code `3` when an item was saved but the display wasn't updated. Once the delivery problem is resolved, send the current docket again:

```sh
node bin/docket.js publish --json
```

If the client loses the response and can't tell whether a mutation saved, it returns exit code `4`. In that case, inspect `list` or `get` before retrying, allowing for KV read lag. The CLI doesn't automatically retry writes.

That behavior gives an agent something concrete to act on instead of treating every error as "try the same thing again."

## Run your own installation

Each installation needs its own Cloudflare Worker, KV namespace, and TRMNL private plugin with the required Developer access. The repository includes the Worker configuration, a setup guide, and the full-screen Liquid template.

The setup is to create the KV namespace, configure the Worker for your account, set a Docket bearer token, and put the TRMNL webhook URL in a Worker secret. On the TRMNL side, create a private plugin using the Webhook strategy, paste in the template, and set `no_screen_padding=yes` so the template controls the spacing.

The agent only needs the deployed Worker's HTTPS origin and the Docket token. Those can come from its environment or an approved local configuration file. It doesn't need your Cloudflare deployment credentials or the TRMNL webhook URL.

There is one shared Docket token, though. Everyone holding it can read, edit, and delete the entire docket. A source label that says "Writing agent" is just text, not a permission boundary. Only give access to agents you trust with the whole board, and remember that somebody walking past the display can read what's on it.

## Where this version stops

The docket is stored as one JSON document in KV. That's convenient for a small proof of concept, but overlapping read-modify-write requests can overwrite each other. There isn't a lock or a queue coordinating agents, and spacing requests a second apart doesn't solve concurrent writes from different clients. Updates need to be sparse and coordinated.

The Worker also attempts a webhook push after every change. Keep TRMNL's [webhook limits and refresh behavior](https://docs.trmnl.com/go/private-plugins/webhooks) in mind before having an agent report every little step. There is no background retry queue, and completed items are deleted rather than archived.

For this version, the useful update is that a task needs a decision or that the next step has changed hands. Put that on the screen, with enough detail to act on it.

The code and setup instructions are in the [Agent Docket repository](https://github.com/joel-g/agent-docket-trmnl).
