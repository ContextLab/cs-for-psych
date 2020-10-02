# Adopting a 'programming mindset'

Writing computer code, or "programming" is fundamentally about using highly
structured and simplified languages to tell fancy calculators which numbers to
crunch.  Everything modern computers do may (with enough digging) be reduced to
repeated calls to a small number of instructions similar to what you've likely
already encountered if you've used a standard scientific calculator or graphing
calculator.  The challenge of programming is to arrange those seemingly simple
instructions in just the right way such that the computer you're feeding them to
does the stuff you want it to.  Two key principles are useful to keep in mind
as you're learning how to program.

## Computers are dumb and unthinking

The earliest general purpose programmable computers, including
[ENIAC](https://en.wikipedia.org/wiki/ENIAC), the [Bendix
G15](https://en.wikipedia.org/wiki/Bendix_G15),
[LGP-30of](https://en.wikipedia.org/wiki/LGP-30), and
[MIR](https://en.wikipedia.org/wiki/MIR_(computer)) were developed in the 1940s
and 1950s, around the time same time that modern psychology started to gain
momentum as a field.  Formal psychological theories developed in parallel drew
heavy inspiration from computers.  For example, classic memory theories still
discussed in introductory psychology courses today (e.g., the [Atkinson-Shiffrin
memory
model](https://en.wikipedia.org/wiki/Atkinson%E2%80%93Shiffrin_memory_model)) suggest that our memory systems have a short-term (working memory) storage buffer that is low-capacity but fast and easy to access, along with a long-term storage mechanism that is high-capacity but relatively slower and more difficult to access.  These concepts were inspired in part by computer [RAM](https://en.wikipedia.org/wiki/Random-access_memory) (which acts like a fast-access low-capacity buffer) and [hard disks](https://en.wikipedia.org/wiki/Hard_disk_drive) (which are slower but have a large capacity).  Theories like these have continued to propagate the misconception that silicon computers are brain-like in a deep sense.  Although many biological systems, including brains, fit some definitions of the word "computer" (e.g., see [this blog post](https://medium.com/the-spike/yes-the-brain-is-a-computer-11f630cad736)), the converse does not hold.  Biological brains bear very little resemblance to modern silicon computers.

This historical context is important to internalize because it can help to
de-mystify many aspects of how computers work.  Unlike biological brains,
computers can *only* do exactly what its programming instructions tell it to do:
no more, and no less.  When you are in the throes of a programming challenge you
can't seem to make sense of, it can be incredibly tempting in the moment to
resort to dangerous thoughts like "my computer hates me" or others that ascribe
any sort of intelligence or "will" to the computer.  Some programming challenges
are incredibly difficult to work through, and can stump even seasoned
professional programmers.  Many questions in computer science remain unsolved.
But there can be no *true* mysteries in computer programming: unlike the "real
world," computer systems are fully deterministic, and you (as the programmer)
will have the means of knowing and tracking every single tiny computation that
the computer performs.  With sufficient time and patience, this gives you the
power to track any "behavior" (calculations) that the computer carries out.

## Complexity can arise from simple building blocks

Every biological organism on earth is comprised of cells whose structures and
functions are encoded in [DNA](https://en.wikipedia.org/wiki/DNA) using an
"alphabet" with just 4 "letters"
([bases](https://en.wikipedia.org/wiki/Nucleobase)) and a small number of
"words" ([codons](https://en.wikipedia.org/wiki/DNA_codon_table)).  All past,
current, and future biodiversity may be expressed using this tiny "language."

In an analogous way, the full diversity of programs that run on computers may be
reduced to a small set of computer
[instructions](https://en.wikipedia.org/wiki/Instruction_set_architecture)
(e.g., addition, subtraction, multiplication, division, logical comparisons,
loading and storing data, etc.) that may be carried out by the
[CPU](https://en.wikipedia.org/wiki/Central_processing_unit).  The key to
harnessing the full power of computers is to iteratively build complexity.  In
other words, basic commands may be combined in sequences that form more
expressive and complex commands.  In turn, those hybrid commands may be combined
in sequences that form still more expressive and complex commands.  After just a
few iterations of this approach, it is possible to create all existing computer
programs-- [operating systems](https://en.wikipedia.org/wiki/Operating_system),
[video games](https://en.wikipedia.org/wiki/Video_game), [self-driving
cars](https://en.wikipedia.org/wiki/Self-driving_car),
[chatbots](https://en.wikipedia.org/wiki/Chatbot), etc.  The key challenge is to
build up intuitions for which combinations of instructions will be useful for
efficiently carrying out a particular desired task.

# Learning to think like a programmer

Thinking like a programmer means mentally tackling a difficult challenge by
continually breaking the problem down into successively smaller (and simpler)
pieces, until you find a small enough and simple enough piece that you're able
to solve that one thing.  Then you just "[do the next right
thing](https://www.youtube.com/watch?v=w6g1yQV0dIY)" and repeat the process
until your challenge is solved.

Realistically, although this approach will (in principle) allow you to solve any
programming problem, many novice programmers find it difficult to build up good
intuitions for how to systematically break a complex problem down.  You may find
some of the following exercises useful to work through:

1. Instruct someone to make an [ice cream
sundae](https://en.wikipedia.org/wiki/Sundae) or put on a jacket. Be as detailed
and specific as possible. Pretend that the person you're instructing is a "dumb"
robot who can understand only primitive instructions (e.g., raise your right arm
by this amount; rotate your hips 30 degrees clockwise; walk forward until you
encounter resistance; etc.).  Your instructions should take the form of a
numbered list or flow chart.  Following the flow chart should result in the
desired (complex) action being performed (e.g., a sundae is made).

2. Practice defining, with as much detail and as specifically as possible,
commonly encountered categories of things.  Foods work particularly well.  For
example, define what a "sandwich" is, or what a "soup" is.  Your definition
should take the form of a numbered list or flow chart that could be followed in
order to determine if something does or does not satisfy the definition.  After
designing your definition, "debug" it by verifying that some examples are
correctly classified.  Now try to come up with "adversarial" examples to "break"
your definition.  For example, is a [hot
dog](https://en.wikipedia.org/wiki/Hot_dog) a sandwich?  Are two pieces of bread
with nothing in between a sandwich?  Can a sandwich be made of non-bread (or
non-edible) materials? Does your definition accommodate multi-layered sandwiches?

3. From the moment you wake up until the moment you go to sleep, spend a day
trying to see the world through the eyes of a computer.  Break down every action
or observation or thought into its constituent parts and instructions.  Separate
data (what is physically happening) from interpretation (what you *think* is
happening).  Think about how each moment of your day could be broken down and
characterized (or explained) using combinations of very simple instructions.
