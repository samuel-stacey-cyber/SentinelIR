# SentinelIR — Research Question Brainstorming

## 1. What originally motivated me to build SentinelIR?

1. What problem did I want it to solve?
2. Who did I imagine using it?
3. Has that motivation changed as I’ve developed the tool?

**My answer:**

1. Originally, wanted to create a tool which SOC analysts could use, to make their detection of events easier, faster, and more reliable. Some good to put on my CV, relevant to cybersecurity, modern, can be expanded to either its current CLI, GUI, or web-UI. Would be a useful tool to set up, have alerts on, potential connection through an app to alert your phone, or connect to a specific device through bluetooth. Is an expandable, maintainable idea, that I can develop further post-dissertation, a real tool that people would use.

2. Imagine that SOC analyst would be able to use it / set it up and just leave it, connect it through CI pipeline, connected to their phone through an app, connected to their central servers just running, or a specific piece of technology they can use. As well as providing it to other companies who needs to set up alert monitoring, whether they want to check their history by running the tool against it, or just set it up as live monitoring, letting them know when something is detected.

3. No, still really enjoying learning different software engineering practices, process and steps to take to get an idea into something real. Was ultimately hoping for a web-UI / GUI but ultimately not within the timeframe set / could be done through using AI, but not necessary current, and will be overly complicated to manage with the dissertation.

## 2. What am I most curious to discover?

For example: which attacks the tool can detect, why it misses some, how to reduce false alerts, or how the available log information affects detection. What would I enjoy investigating beyond simply getting the software working?

**My answer:**

I would say, see how other tools work, what things they do great, things that need improving, and things that they've completely missed, then compare it against mine, see how improvements can be made. As well as through real feedback generated through the future CTF hosted on the vulnerable website, using SentinelIR to detect them as they go through! Ultimately trying to create a real tool that is reliable, you can just leave and hope and pray that nothing comes back, but if it does that it is real, and you are able to go ahead and look through a plan / create a plan of action, in order to resolve / tackle whatever SentinelIR threw at you!

## 3. Which security behaviours would I most like to investigate?

Possible areas include SSH authentication attacks, web authentication attacks, distributed login attempts, enumeration or suspicious web requests. Which one or two interest me most, and why?

**My answer:**

Definetly the more web side, as their are so many different vulnerabilities against websites, everyone has websites, and that is where most information is at! Enumeration probably second, due to having done penetration testing, it is the easiest and basically the only way of finding information, and being able to detect that someone is enumerating, would be useful to know on how to prevent please from doing it!

## 4. What could I compare to produce an informative result?

For example: simple counting rules versus rules that consider timing and event order; access logs alone versus access logs combined with application events; or different detection thresholds. These are possibilities, not commitments—what comparison appeals to me?

**My answer:**

Goal is to provide the user with as much information as humanly possible, to allow them to be able to make the most informed decision possible!

## 5. What have I already noticed that deserves investigation?

Have I encountered unexpected alerts, missed activity, unreliable parsing or assumptions that might not hold with real logs? Which parts of SentinelIR’s behaviour am I currently least confident about?

**My answer:**

I have worked on it really well, nothing seems to be `lacking`. Most thing I want improving its the expansion of analysing for different web vulnerabilities, in order to be able to detect things through the hosted vulnerable CTF. As well as potentially leading SentinelIR into a tangable product that could be sold as a web-defence tool just sitting in the background!

## 6. What experimental environment could I realistically build and manage?

1. What machines, virtual machines or containers can I use?
2. Which services could I run and collect logs from?
3. Roughly how much time can I give the project each week?
4. What would make the lab too complicated?

**My answer:**

1. Personally thinking of just hosting the website, I wouldn't mind either paying for a month or something, in order to be able to get as much primary research as possible! Not sure how I'll tackle this, but come to it when I do!
2. Not sure?
3. Round 4-6 hours, depending on how I am doing with other courseworks, but I can do most mornings tackle / juggling each coursework!
4. Just expanding into something niche and not relevant. Basically at any point I jump into a rabbit hole!

## 7. What would I want someone to learn from my dissertation?

Beyond seeing that SentinelIR works, what finding would be useful to a reader? If an improvement failed to increase detection performance, what could the experiment still teach us?

**My answer:**

Just how well and reliable a piece of software can be at providing a user, very much important, impacting data in order to be able to make an informed decision on something that either can ruin their reputation, cost them money, or completely mess up / break a business or leak / cause leakage of private and personal data!
Performance is not the goal, correctness is! As being able to rely on something is very important, plus then being able to make a decision on the back of it is even more important!!!
