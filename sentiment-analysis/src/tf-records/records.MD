# TensorFlow Records

Reading up on tensorflow, I decided that I should convert the dataset 
being used to a TF record format. This is a special binary data type 
created by tensorflow that allows for much faster data access. They're 
also of use when dealing with datasets which are larger than can be stored
in memory. Whilst that isn't the case with this project, I felt that
it would be useful to work out how to do this now.

Reading the documentation on this, we are told that there are three data types
that we can use. These are `tf.train.BytesList`, `tf.train.FloatList` and 
`tf.train.Int64List`, and can each encode a number of different data types.
Initially, I intended to encode the entire dataset as strings, using `tf.train.BytesList`
but, after considering this a little more, I realised that this would not actually
be a brilliant optimisation, as it would still leave a substantive amount of processing
to be done each time the dataset was read. Therefore, to minimise this, I decided to 
replace words with their map index at this stage, and thus store Integers in the place
of each word. 