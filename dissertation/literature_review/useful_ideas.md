# Ideas to be used within Dissertation / Coursework

## Informative Table / Improved Abbreviation Table

When giving abbreviations, provide a table of not just the abbreviation but also the definition, order, and their reference:

| Information Type | Definition | Order | References |
| --- | --- | --- | --- |
| Additional Alerts (AA) | XYZ | 1 | [12], [14] |

## Tables

Have a table including some sort of `%`, providing the reader some sort of scale / data that they can view and understand, with comparable figures.

## Diagrams

Have some sort of diagram with plotted data -> then link back to within writing!

## Figures

Screenshots of the tool -> outputs + explaination of how it works

## Methodology

Include `study goals` -> referring back to the original research question!

## Appendicies

# Notes

## P01
Remembering that an alert is a common false positive
Always refere back to research questions -> when talking about the process you took (provides meaning to what you actually did, and why it was relevant to have done it / doing it)
Refere back to previous or future parts when speaking / comparing something -> and how it changes comapred to this specific thing! -> plus refere to limitations!
Ensure that studies / data collected are consistent and referrable!
Explain why something had to change / didn't happen the way it was intended or happened in a previous example!
Multiple studies -> try to use the same data -> providing comparable data + ensures that the original data was `true` -> allows for a comparison of data (another talking point)
When having two sources of `data` -> make them disjointed (unlinked) to provide different `sides of the street`
Ethical considerations -> use the same throughout + explain them + link them back when another one is used!
Evaluation strategy -> referring back to the original research questions!
Comparison of tables / studies -> how they differred / similar
Results section!
Just before a new paragraph, have ctrl+i, a super brief description of what this paragraph is about / its aim: `Experimental setup and ethical considerations.`
Always refer back to the research question when speaking about results `Evaluation Strategy.`
Include a discussion section -> if that applies to a solo writer? -> refer back to each research question and talk about how it was done/wasn't done -> limitations and whatnot

## P02
Brute-force attacks are known as `flat traffic` -> `repeated authentication attempts` - `application-layer actions`
Limiting false positives - look for specific attack behaviour rather than only unusual traffic - investigate whether authentication context helps distinguish attacks from normal login mistakes
Labelling different types of metrics - `True Positive (TP)` - `False Positive (FP)` - `True Negative (TN)` - `False Negative (FN)`
`Brute-force thresholds` -> define exactly what SentinelIR counts + which events belong together + the time window -> explain why the threshold was chosen -> test several values to see how precision and recall change -> link to RQ1!
Comparable data -> group detections and ground truth into the same unit before comparing them -> decide whether SentinelIR evaluates individual attempts, attack sequences or scenarios -> avoid counting several alerts for one attack as several successfully detected attacks!
Ground truth -> record what actually happened in the controlled scenarios separately from SentinelIR's detection rules -> avoid defining an attack only by the same threshold the detector uses!
Authentication context -> a POST request or redirect does not automatically prove failed or successful authentication -> investigate whether application authentication logs provide clearer evidence -> directly relevant to RQ1!
Threshold testing -> use separate scenarios to choose thresholds, then evaluate on held-out scenarios -> avoid choosing the best threshold using the final evaluation results!
