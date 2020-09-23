# Euclid Gate Sequencer
## Description
This is a little web application to translate a sequence of gates into an
euclidean rhythm description, given by the amount of total steps, the active
steps and an offset. Additionaly, some sequences may not be a complete
euclidean rhythm but the beginning part of a bigger euclidean sequence.

## Rationale
The inspiration for this project arose from my lack of money. I have a modular
system where my only source of gates is a Pamela's New Workout by ALM.  It's a
fantastic clock and modulation module but it's kind of awkward to use as a gate
sequencer, unlike something like a Malekko Varigate 8, an Intellijel Metropolis
or a Hermod Squarp, for example, which are all really expensive. I also just
enjoy using more _modular-y_ solutions. So, to utilize the PNW as a gate source
I had to frequently think of how to mentally translate step sequences into
euclidean rhythms so I could punch them in and use them that way.

It's also useful for my livecoding in TidalCycles, which has euclidean rhythms
written directly into its syntax.

## Sources
Most of the needed theory was extracted from the original paper about euclidean rhythms by Godfried Toussaint which you can check [here](http://cgm.cs.mcgill.ca/~godfried/publications/banff.pdf).

Some further reading was necessary on Bjorklund's algorithm
[here](https://web.archive.org/web/20100528023736/https://ics-web.sns.ornl.gov/timing/Rep-Rate%20Tech%20Note.pdf).
