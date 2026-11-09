# Writing for joelguerra.com

This is a starting style guide inferred from Joel's existing articles. Follow Joel's explicit direction when it differs from this guide, and refine the guide as he supplies preferences.

## Before starting work

- Always pull the latest `master` from `origin` before beginning work in this repository, including writing and editing articles. Inspect the current branch and working-tree status first so local work is preserved.
- On `master`, run `git pull --ff-only origin master` before making changes. On a working branch, fetch and update local `master` first, then integrate it into the working branch as appropriate.
- If local changes or divergent history prevent a clean update, reconcile them without discarding work or force-pushing. Don't silently proceed from stale `master`.

## Voice

- Write like a developer showing a friend something he built or figured out: conversational, direct, practical, and technically specific.
- Use first person for Joel's own work and opinions. Use “you” when addressing the reader and “we” when walking through a task together.
- Use contractions and ordinary language. Read the prose aloud; it should sound like a person talking, not a product announcement or a corporate white paper.
- Joel explicitly says sales pitches aren't his style. Write project introductions as a builder explaining the work, without marketing hype, manufactured urgency, or pressure to sign up. A plain link to try a project is enough.
- Let enthusiasm come from the project and the details. Avoid grand claims and generic excitement.
- Humor can be dry, sarcastic, irreverent, or occasionally crude when it fits the subject. Don't manufacture jokes or turn every paragraph into a bit.
- Treat readers as capable and curious. Explain unfamiliar mechanisms without lecturing or assuming that everyone knows the same tools.

## Words and phrases Joel actually uses

These examples come from the site's tech and car articles, with particular attention to the older hands-on posts. They are evidence of voice, not a phrase bank to sprinkle into every draft. Recurring habits are distinguished below from individual examples. Joel's explicit preferences above and below still apply, including the ban on em dashes, even where older articles differ.

### Recurring habits

- **Physical, ordinary verbs:** “grab,” “pop,” “slap,” “pull,” and “drop,” along with “fire up” / “fired up.” These appear across software and car posts. For example, the Stack Overflow guide says “Fire up your code editor and edit app.py,” and the Azure bot guide talks about how to “slap the bot on a web page.” Keep precise verbs for precise operations; don't make every action “slap.”
- **Transitions tied to progress:** “Now that…,” “With all…,” “Before we can…,” “Once you’ve…,” “Next,” and “Then.” The engine build moves from “With the crank secured we can come back to the pistons and rods” to the next task. Transition by naming what is now ready or what is still needed.
- **Direct instructions and reminders:** “make sure,” “Remember,” “Don’t forget,” “You can,” and “If you….” These point to a specific action or choice. They aren't an excuse to pad each step with a generic warning.
- **Casual judgments:** “pretty,” “nice,” “cheap,” “not cheap,” and “of course.” The car posts discuss actual prices and whether parts are worth buying. Keep that plain judgment when the facts support it, rather than replacing it with polished product language.
- **Reasons attached to actions:** “because,” “so,” “so we can,” and “we need to.” Joel explains a dependency in the same breath as the step: “Before we can actually put this in the block we need to install new bearings.”
- **Concrete scope:** “In our case,” “for this car,” and “the process will be largely the same.” Joel names the thing he's working on, then explains which details transfer to the reader's situation. Don't present a single implementation as universal.

### Individual examples worth learning from

| Exact wording | Source in `content/` | What to preserve |
| --- | --- | --- |
| “Nothing fancy here, just a loop over the slices of strings” | `tech/how-to-draw-a-dick-on-the-city-of-belleuve.md` | Plain description of a small implementation, with the concrete operation included. |
| “We’re not animals so we’ll check for errors” | Same Bellevue article | A quick joke attached to a real coding decision. |
| “They’re 20 years old and made of plastic so of course I broke one.” | `cars/how-to-restore-your-cars-exterior-trim.md` | Matter-of-fact admission of a snag, without a dramatic lesson. Never invent a mishap to imitate this. |
| “Could we have done this *before* installing the pistons? Yeah, but here we are.” | `cars/lets-build-a-500-hp-honda-engine.md` | Self-directed humor about a specific choice. Occasional natural questions are part of Joel's voice; repeated canned question-and-answer beats aren't. |
| “Now do it 16 times.” | Same engine build article | A short, dry instruction after the full process has already been explained. |
| “For added style points I’m using this purple magnetic oil plug bolt.” | Same engine build article | An aside about an actual personal choice. |
| “This mount is totally shot.” | `cars/how-to-replace-a-transmission-mount.md` | A blunt assessment grounded in what the article shows. |
| “and off you go.” | `tech/how-to-embed-your-azure-web-app-bot-in-any-web-page.md` | A casual finish to an instruction. |
| “Have fun and as always, bother me on” | `tech/introducing-go-goldapi-a-go-package-for-querying-precious-metal-prices.md` | An informal invitation for feedback, followed by a Twitter link in the original. The about page similarly says “you can yell at me about it.” Don't force a sign-off into every post. |

Use the underlying habits more often than the memorable lines. Preserve natural contractions, occasional asides, and uneven sentence lengths. Don't imitate typos, broken links, outdated facts, or every quirk of old formatting. An ordinary expression appearing on an AI-ism list doesn't require removing it when it communicates something specific in Joel's voice; explicit bans and the instruction to cut empty filler still stand.

## Shape of an article

- Put the thesis in the first sentence. If the title asks a question, answer it directly. For a how-to, state the job and what it accomplishes. For a project write-up, say what Joel built and what it does. Bring in the example, video, or first step once the reader knows the point of the article.
- For a project write-up, explain what it does, how it works, and the interesting decisions or problems encountered. Choose the order that makes the project easiest to understand.
- For a tutorial, walk through the work in the order the reader needs to do it. Explain why a step matters when the reason isn't obvious.
- Use descriptive headings when they help navigation. Don't force every article into the same outline or add headings to every few sentences.
- Keep paragraphs focused. Mix short sentences with longer explanations; don't make the whole article a series of one-line paragraphs.
- End when the useful material is finished. A repository link, a next step, or a brief invitation for feedback can be enough. A formal recap or catchphrase isn't required.

## Technical substance

- Prefer concrete behavior, examples, code, and screenshots over broad claims about usefulness or simplicity.
- Explain the meaningful connections between components: what runs where, who calls whom, what data moves, and what triggers an update.
- Read the relevant source and README before describing a project. Verify claims against the implementation; don't turn a README into an article by merely rephrasing each section.
- Include implementation details that teach something or explain a decision. An article doesn't need an inventory of every file, endpoint, variable, or dependency.
- Describe limitations and tradeoffs plainly where they affect the reader. Distinguish observed behavior from documented guarantees.
- Never invent Joel's motivation, personal experiences, failed attempts, results, measurements, or opinions. Ask for missing personal context or write around it using verified facts.
- Don't claim code was run or a deployment succeeded unless that was verified. Check current external documentation when an article depends on current API or product behavior.
- Use runnable, focused code examples with language-tagged fences. Identify placeholders clearly and keep credentials and private account details out of published content.
- Link to the project and relevant primary documentation near the explanation they support.

## Editing preferences

- Favor active voice and specific verbs. Say what the code does rather than calling it “powerful,” “seamless,” or “robust.”
- Cut filler openings, repeated explanations, canned transitions, and generic conclusions.
- Rhetorical questions, asides, exclamation points, and emphasis are available tools, not requirements. Use them where they sound natural.
- Use lists for steps or genuinely parallel items. Keep explanations in prose when the relationship between ideas matters.
- Preserve personality when editing. Fix ambiguity, factual mistakes, and distracting grammar without polishing everything into a generic professional voice.

## Avoid AI-isms and Claudeisms

Joel explicitly wants to avoid recognizable AI writing habits, including patterns often called “Claudeisms.” Treat this as an editorial preference, not a claim that any particular word proves AI authorship. Apply it to article prose and suggested titles.

- Cut canned openings and scene-setting: “In today's digital landscape,” “In the ever-evolving world of,” “Let's dive in,” “Let's unpack that,” and “Let's explore.” Open with the actual subject.
- Don't use the formula of a dramatic hook, a rhetorical question, and then a dictionary-style definition. Start with the project's actual problem or behavior; explain unfamiliar terms when the reader needs them.
- Avoid inflated vocabulary and marketing filler: “delve,” “tapestry,” “a testament to,” “beacon of innovation,” “unlock the power of,” “game-changing,” “revolutionize,” “transform the landscape,” “supercharge,” and “elevate.” Prefer the literal action. Use “use” instead of “leverage” when that is all it means.
- Watch for ornamental uses of “landscape,” “dynamic,” “foster,” “vibrant,” “hurdle,” “nuance,” “poignant,” “labyrinth,” and “myriad.” Say “help people build a community” rather than “foster a vibrant community.” Keep precise technical uses, such as a dynamic IP address or a data transform.
- Remove empty signposting: “It's worth noting,” “It is important to remember,” “To be fair,” “Importantly,” “At its core,” “Here's the thing,” “The key insight,” “The real magic,” and “This is where things get interesting.” State the fact or explain what makes it interesting.
- Don't manufacture a revelation with “It's not X. It's Y,” “This isn't about X; it's about Y,” “not just X, but Y,” or a dramatic “X—not Y.” State what something does. Explain a real technical distinction directly when it matters.
- Avoid canned question-and-answer beats: “The result? ...”, “The best part? ...”, “Why? Because ...”, and “The catch? ...”. A natural question is fine; don't use these as a recurring paragraph template.
- Avoid performative candor and praise: “Let's be honest,” “I'll be blunt,” “To be clear,” “genuinely,” and “That's a great question.” Show the reasoning without announcing sincerity or flattering the reader.
- Don't decorate explanations with “quietly,” “beautifully,” “elegantly,” “surprisingly,” or “deceptively simple” unless the description adds a specific, defensible observation. Explain the behavior instead.
- Don't use em dashes in authored article prose or titles. Rewrite with periods, commas, colons, or parentheses. Don't substitute double hyphens or spaced en dashes to recreate the same habit. Preserve punctuation in exact quotations and literal code when necessary.
- Avoid repetitive sentence fragments, dramatic one-line paragraphs, forced groups of three, and repeated “No X. No Y. Just Z.” constructions. Let the material determine the rhythm.
- Don't use “Why this matters” as a heading or rhetorical transition, in any capitalization. Explain a concrete consequence alongside the relevant detail instead of adding a generic importance section.
- Don't give every section a bold lead-in, every heading a clever subtitle, or every ending a slogan. Skip “Key Takeaways,” “The Bottom Line,” “Final Thoughts,” “In conclusion,” “To wrap up,” “Ultimately,” and “Happy coding!” unless Joel specifically requests that format.
- Avoid symmetrical layouts imposed for appearance: the same number of bullets per section, matching bolded verbs in every bullet, and mechanically balanced headings. Prefer sentence case for new subheadings. Use bold, exclamation points, and emojis sparingly; don't add them to manufacture enthusiasm.
- Don't repeat the article in a closing paragraph, speculate vaguely about the future, or finish with an inspirational cliché. Stop once the explanation is complete.
- Write with a point of view when Joel has supplied one or the evidence supports a clear technical judgment. Don't dilute every statement with “while there are pros and cons” or other reflexive qualifications. Keep specific uncertainties and real tradeoffs; don't invent an opinion for Joel or claim certainty the evidence doesn't support.
- Avoid generic claims that a project “just works,” “handles the heavy lifting,” is “production-ready,” or is “a small change with a big impact.” Describe the work, reliability, or effect with evidence.
- Before delivering a draft, make a separate editing pass for these habits. Delete filler and rewrite the underlying sentence; don't just swap in synonyms. Preserve literal technical terms, quotations, and natural phrasing when they carry real meaning.

## Reference articles

Read these as examples of voice and approach, not as current technical authority or templates to copy:

- `content/tech/introducing-go-goldapi-a-go-package-for-querying-precious-metal-prices.md`: direct project introduction, authorship disclosure, and concrete usage.
- `content/tech/how-to-ssh-to-your-azure-linux-vms-with-username-and-password-from-windows-linux-or-mac.md`: conversational instructions tied to screenshots and commands.
- `content/tech/how-to-draw-a-dick-on-the-city-of-belleuve.md`: hands-on technical explanation with an irreverent premise and running commentary.

Posts in “the Martin files” reproduce another author's material; don't use their prose as evidence of Joel's personal voice. Joel confirmed that the original NameCamper introduction was written by an LLM before this guide. Don't use that original version as evidence of his voice or preferences. Revisions of that article should follow this guide.

## Repository conventions

- Articles for `/tech` live in `content/tech/` as Markdown with Hugo front matter. Follow nearby files for metadata and image paths.
- Start new articles with `draft: true` unless Joel asks to publish them. Creating a draft doesn't require publishing or deploying the site.
- Preserve existing article dates, slugs, and publication status unless the requested change calls for changing them.
- Edit source content rather than generated files in `public/`.
