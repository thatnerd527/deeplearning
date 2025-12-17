import tensorflow as tf
from tensorflow.keras import layers, Model
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.applications.resnet50 import preprocess_input

class UnifiedResNetClassifier(Model):
    def __init__(self, num_classes):
        super(UnifiedResNetClassifier, self).__init__()
        self.backbone = ResNet50(
            include_top=False, 
            weights='imagenet', 
            pooling='avg'
        )
        self.backbone.trainable = False 
        self.layer1 = layers.Dense(64, activation='relu')
        self.layer2 = layers.Dense(48, activation='relu')
        self.layer3 = layers.Dense(128, activation='relu')
        self.output_layer = layers.Dense(num_classes)

    def call(self, inputs):
        x = tf.cast(inputs, tf.float32)
        x = preprocess_input(x)
        x = self.backbone(x)
        
        x = self.layer1(x)
        x = self.layer2(x)
        x = self.layer3(x)
        
        return self.output_layer(x)