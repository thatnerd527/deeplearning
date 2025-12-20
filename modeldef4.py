import tensorflow as tf
from tensorflow.keras import layers, Model
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.applications.resnet50 import preprocess_input

# This is a dynamic model architecture that makes it possible to have dynamic layers and unit sizes tuned.
# This architecture is a slight departure from normal deep learning architectures where the amount of layers and the amount of units are fixed in and unchanging during training.
# But doing it like this allows us to control every single facet of the model dynamically using a program, and also increases flexibillity.
@tf.keras.utils.register_keras_serializable()
class DynamicResNetClassifier(tf.keras.Model):
    def __init__(self, num_classes, layer_configs, dropout_rate):
        super(DynamicResNetClassifier, self).__init__()
        # 1. Backbone
        self.backbone = tf.keras.applications.ResNet50(
            include_top=False, weights='imagenet', pooling='avg'
        )
        self.backbone.trainable = False 

        # 2. Create Dynamic Layers
        self.dense_layers = []
        self.dropout_layers = []

        for units in layer_configs:
            self.dense_layers.append(layers.Dense(units, activation='relu'))
            self.dropout_layers.append(layers.Dropout(dropout_rate))

        # 3. Output
        self.output_layer = layers.Dense(num_classes)
    def call(self, inputs, training=False):
        x = tf.cast(inputs, tf.float32)
        x = preprocess_input(x)
        x = self.backbone(x)
        # Iterate through our dynamic list of layers
        for dense, drop in zip(self.dense_layers, self.dropout_layers):
            x = dense(x)
            x = drop(x, training=training)

        return self.output_layer(x)