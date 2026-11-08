---
title: "Agent Docket: Keeping Track of Open Threads With AI Agents"
date: 2026-11-08T12:00:00Z
draft: true
description: "A Cloudflare Worker, a small CLI, and a TRMNL display for tracking which agent conversations need your attention."
summary: "I built Agent Docket to put open threads with AI agents on an e-ink display, split into what needs me and what is waiting on someone else."
tags: ["ai", "cloudflare", "trmnl"]
---

An agent can finish its part of a task and still need you to review a draft or approve a change. Meanwhile, another thread is waiting on somebody else, and opening it again won't make them respond any faster.

I built Agent Docket to put those open threads on a [TRMNL](https://trmnl.com) e-ink display. It has two columns: **Needs you** and **Waiting on others**. An agent can add an item, update it as things change, move it between columns, and remove it when we're done.

The distinction is who owns the next step. An agent being busy doesn't automatically mean something belongs on the display. A question I need to answer does.

## From a command to the screen

The backend is a Cloudflare Worker with KV storage. An agent sends an authenticated HTTP request, the Worker saves the updated docket, and then it sends a compact version to a TRMNL private plugin through a webhook. A Liquid template turns those variables into the two-column layout.

There's no model running in the Worker. It doesn't need to know which agent made the request, and it doesn't read conversations to figure out what belongs on the docket. The agent has to do that part. Anything that can make the HTTP requests can use it.

For agents that can run a shell command, I added a dependency-free Node CLI. It wraps the API so the agent can spend less time assembling requests and more time doing whatever I asked it to do.

Here's an example. From the Agent Docket checkout, with the Worker URL and Docket token already configured:

```sh
node bin/docket.js list --json
node bin/docket.js add --title "Review article draft" --detail "Check the CLI example before publishing" --group needs-you --source "Writing agent" --json
```

The first command matters. If the article is already on the docket, we should update that item instead of adding another one every time the conversation moves forward.

The create response includes an item ID. Use that ID in place of `ITEM_ID` below when the next step belongs to somebody else:

```sh
node bin/docket.js update ITEM_ID --detail "Waiting for technical review"
node bin/docket.js move ITEM_ID waiting-on-others
```

Run mutations sequentially, at least a second apart. When the work is finished and removal is authorized:

```sh
node bin/docket.js delete ITEM_ID
```

Each change attempts to update TRMNL. The physical screen still follows its refresh schedule, so a successful webhook response doesn't mean the pixels have changed yet.

## Give the agent a useful job

The repository includes an `AGENTS.md` file with guidance for working with the docket. Keep the title short, make the detail say what needs to happen, reuse the item's ID, and check whether an operation actually succeeded.

For the article example, "Review article draft" is a useful title. "Article" leaves me opening the conversation to remember why it's there. The optional source label can tell me which agent or workflow put it on the board, and a reference URL stays available through the API.

Items can also have a due date and a kind: topic, reminder, or todo. A reminder is an item on the screen. There's no scheduler hiding behind it that will send a notification at 9am. Due dates affect sorting.

The display fits four items per column, with a count for anything beyond that. It puts due dates first, then sorts by the most recent change. Longer text gets clipped for the screen; the API keeps the full stored details and reference URLs. The template targets an 800x480 display, so concise text earns its keep. Use plain text rather than emoji for reliable monochrome rendering.

## Saved and displayed are separate outcomes

One detail that matters for an agent is what happens when the item saves but the webhook fails.

The Worker writes to KV before calling TRMNL. Suppose the item saves successfully, then TRMNL rejects the webhook or the request times out. Repeating the original `add` could create a second item. Now the board has two reminders to review the same article, which isn't much of an improvement.

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

<!-- Publication check: confirm the Agent Docket repository is public and the link is accessible before changing draft to false. -->
