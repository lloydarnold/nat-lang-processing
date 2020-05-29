# On the topic of Models
As this is my first project working with TensorFlow, I started off looking at 
models already in existence. As before, I used the work of Artem Oppenheimer
as a starting point, and tried to develop an understanding of what was going
on through a mix of reverse engineering his code & reading the tf documentation.
As with most other machine learning, we need to define a model that consists of a
certain structure, and we can then train them to be smart by adjusting parameters.

In the past, my experience with Neural Networks has been limited to multi-layer
perceptrons. Whilst these are very handy models, they have one major shortcoming -
they consider everything that they are processing in isolation. This is okay when
used to classify images, or play pong, but less okay when dealing with language, as 
the meaning of a word changes depending on those around it. To deal with this, we can
utilise a so-called long-term short memory (LSTM) model. I will discuss A how this works
and B how this can be implemented in TensorFlow. 

## Long Term Short Memory models
