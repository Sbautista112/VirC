- **Date:** 11/25/2026

## Context

What problem are we solving? Which constraints matter (cost, speed, hardware, what I want to learn)?
Trying to get more familiar with CNN models and how they work. For that I will make a virtual closet project and will compare different public models to measure their pros and cons.
## Options considered

   model             loading model   Average background removal    Longest removal
1. u2net                    0.58     0.09                           0.14
2. isnet-general-use       12.99     0.21                           0.36
3. birefnet-general        74.34     4.94                           6.75
4. u2net_cloth_seg          6.88     0.25                           0.30

1. One concern with u2net is that if an item is similar color to the background there is possibility that it might cut it out. But overall good speed.
2. Overall not bad and good at also being able to identify hangers but compared to u2net slower on average.
3. Really slow loading time and struggles at properley capturing clothings tags
4. fast loading time but horrible background removal.  


## Decision

Will go with u2net as overall the most the most fast in measurement categories. 

## Why

2. u2net                    0.58     0.09     0.14

## Consequences

These are values based on a locally downloaded model to results may differ depending on how and where we host this model other than locally so will have to be revisted at a later point.
