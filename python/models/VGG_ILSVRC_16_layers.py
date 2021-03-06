from kaffe.tensorflow import Network

class VGG_ILSVRC_16_layers(Network):
    def setup(self):
        (self.feed('data')
             .conv(3, 3, 64, 1, 1, name='conv1_1')
             .conv(3, 3, 64, 1, 1, name='conv1_2')
             #.max_pool(2, 2, 2, 2, name='pool1', with_argmax=True) # use argmax
             .max_pool(2, 2, 2, 2, name='pool1') # use argmax
             .conv(3, 3, 128, 1, 1, name='conv2_1')
             .conv(3, 3, 128, 1, 1, name='conv2_2')
             #.max_pool(2, 2, 2, 2, name='pool2', with_argmax=True) # use argmax
             .max_pool(2, 2, 2, 2, name='pool2') # use argmax
             .conv(3, 3, 256, 1, 1, name='conv3_1')
             .conv(3, 3, 256, 1, 1, name='conv3_2')
             .conv(3, 3, 256, 1, 1, name='conv3_3')
             #.max_pool(2, 2, 2, 2, name='pool3', with_argmax=True) # use argmax
             .max_pool(2, 2, 2, 2, name='pool3') # use argmax
             .conv(3, 3, 512, 1, 1, name='conv4_1')
             .conv(3, 3, 512, 1, 1, name='conv4_2')
             .conv(3, 3, 512, 1, 1, name='conv4_3')
	     #.max_pool(2, 2, 2, 2, name='pool4', with_argmax=True) # use argmax
             .max_pool(2, 2, 2, 2, name='pool4') # use argmax
             .conv(3, 3, 512, 1, 1, name='conv5_1')
             .conv(3, 3, 512, 1, 1, name='conv5_2')
             .conv(3, 3, 512, 1, 1, name='conv5_3')
             #.max_pool(2, 2, 2, 2, name='pool5')
             #.fc(4096, name='fc6')
             #.fc(4096, name='fc7')
             #.fc(1000, relu=False, name='fc8')
             #.softmax(name='prob')
             )
