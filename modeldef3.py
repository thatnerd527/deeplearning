import tensorflow as tf
from tensorflow.keras import layers, Model
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.applications.resnet50 import preprocess_input

class TunableResNetClassifier(Model):
    def __init__(self, num_classes, units_1, units_2, units_3, dropout_rate):
        super(TunableResNetClassifier, self).__init__()
        
        self.backbone = ResNet50(include_top=False, weights='imagenet', pooling='avg')
        self.backbone.trainable = False 
        
        # Dynamic Layers based on Optuna trials
        self.layer1 = layers.Dense(units_1, activation='relu')
        self.drop1 = layers.Dropout(dropout_rate)
        
        self.layer2 = layers.Dense(units_2, activation='relu')
        self.drop2 = layers.Dropout(dropout_rate)
        
        self.layer3 = layers.Dense(units_3, activation='relu')
        
        self.output_layer = layers.Dense(num_classes)

    def call(self, inputs, training=False):
        x = tf.cast(inputs, tf.float32)
        x = preprocess_input(x)
        x = self.backbone(x)
        
        x = self.layer1(x)
        x = self.drop1(x, training=training) # Dropout only active during training
        
        x = self.layer2(x)
        x = self.drop2(x, training=training)
        
        x = self.layer3(x)
        return self.output_layer(x)