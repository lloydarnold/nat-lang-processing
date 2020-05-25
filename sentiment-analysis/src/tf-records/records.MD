# TensorFlow Records

Reading up on tensorflow, I decided that I should convert the dataset 
being used to a TF record format. This is a special binary data type 
created by tensorflow that allows for much faster data access. They're 
also of use when dealing with datasets which are larger than can be stored
in memory. Whilst that isn't the case with this project, I felt that
it would be useful to work out how to do this now.

Reading the documentation on this, I realised that, as this datset is text
only, I could encode it with the type `tf.train.BytesList`. In order to do
this, the string data type needs to be first encoded as bytes, using `String.encode()`.

