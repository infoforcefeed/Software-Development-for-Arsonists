---
title:Ad-Hoc Rules for Maintainable Software
author:Quinlan Pfiffer
date:2014-12-23
---

I recently read [The Lava Layer Anti-Pattern](http://mikehadlow.blogspot.com/2014/12/the-lava-layer-anti-pattern.html)
and it inspired me to try to write down some of the rules
discovered over my short software career. Most of the time I joke about having
no dependencies on a project, but a lot of the time it makes sense. There are a
few things that I've been seeing repeated over the past year or so that I think
are good ideas, so I'm going to attempt to write them down.

## 1. Avoid side-effectful code

> "You overloaded plus? What does plus do?"

This one comes straight from the functional programming world, but can easily be
applied to imperative languages as well. Side-effects are the bane of anyone
trying to reason about your program, and reasoning about a large program you're
trying to maintain is important. If you don't know what I mean by side-effects,
see #5.

## 2. Assume all code will outlive you, program for longevity and maintainability

It is not uncommon to hear of decade-year old codebases that are still chugging
in the background, critical yet unmaintainable. Rewrites would result in a huge
expense and downtime that would be unavoidable. It is important to write your
code in such a way that it can be easily maintained or replaced, if the need
arises.

Hacks should be avoided. Every `TODO` and `temporary fix` you leave in the codebase
is a stain on your permanent record. This is kind of an open-ended item, because
it can effect all parts of the stack, from database (relational? K/V?) choice to
programming language (Shorter dev cycles? Faster execution speed? Portability?)
so I leave the interpretation up to you.

## 3. Typed inputs and outputs on functions

Another one out of the FP world. This is purely for the people
reading your code (this could be you!). Functions that have no side-effects 
and clear signatures can be easily reasoned about. Pass stuff in, get stuff out.
It also makes testing and linting much, much easier.

## 4. Immute as much as possible

Put `const` on everything. Touch only as much memory as you have to. Return new
objects instead of modified ones. This is one of those things that can help in
tracking down or eliminating bugs. The fewer functions that can modify
state, the better. Which leads me to...

## 5. DON'T MUTATE STATE

I first read this in the [Out of the Tar Pit](http://shaffner.us/cs/papers/tarpit.pdf)
paper by Moseley and Marks is probably one of the most important papers you'll
ever read. The go over state, the false security of unit testing, why state is
the enemy of the programmer and all sorts of other little tidbits that will help
you write better software.

Mutating state is the number one cause of problems, because it effects how
everything else in the program that is involved with that state acts. The Tarpit
paper goes over this much better than I ever could.

## 6. Avoid dependencies as much as possible

This is sort of a political philosphy, and most people will fall on the other
side of the fence than I, but I've seen too many Django packages fail to work with the
software stack I have after a handful of years because they haven't been kept up
to date.

Dependencies, like every other piece of software, have to be kept up to date.
Most dependencies do not follow rule #2, however, and will eventually fall
apart. New language runtimes, new APIs, your language's weird package manager is
down again, all sorts of different things can change and render your dependencies
broken.

You're probably going to be maintaining those dependencies in the long run
anyway, so you might as well start early.

## 7. If dependencies cannot be avoided, pick stable ones vs. cutting edge ones

This one is simple, don't pick something unproven unless it doesn't really
matter. That hot-shit compiles-to-CSS dont-call-it-CSS-language-of-the-month may
not be there two years from now. This is, again, heavily tied into #2.

So these are my rules, for now. We'll see how I feel about them five or six
years down the line.
