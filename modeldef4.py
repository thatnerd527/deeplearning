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
    

    # ============================================================
# Dynamic ResNet50 Classifier
# ============================================================
# Fungsi utama model:
# - Menerima input gambar dalam bentuk tensor (batch, H, W, C)
# - Mengekstraksi fitur menggunakan ResNet50 pretrained ImageNet
# - Memproyeksikan fitur ke beberapa layer Dense + Dropout
# - Menghasilkan logits untuk tugas klasifikasi
#
# Model ini dirancang sebagai baseline fleksibel yang dapat
# dikonfigurasi ulang tanpa mengubah arsitektur utama.
# ============================================================


# -------------------------
# Backbone (Feature Extractor)
# -------------------------
# ResNet50 digunakan sebagai feature extractor dengan konfigurasi:
# - include_top=False  -> classifier bawaan ResNet50 dibuang
# - pooling='avg'      -> global average pooling untuk menghasilkan
#                         vektor fitur 1D
# - weights='imagenet' -> menggunakan bobot pretrained ImageNet
#
# backbone.trainable = False:
# - Backbone dibekukan agar tidak ikut dilatih
# - Training difokuskan pada classification head
# - Mengurangi risiko overfitting dan mempercepat training
# -------------------------


# -------------------------
# Dynamic Classification Head
# -------------------------
# Head dibangun secara dinamis berdasarkan layer_configs:
# - Contoh: layer_configs = [128, 64]
#   -> Dense(128) + Dropout
#   -> Dense(64)  + Dropout
#
# Setiap Dense:
# - Menggunakan aktivasi ReLU
# - Diikuti Dropout(dropout_rate) untuk regularisasi
#
# Desain ini memungkinkan:
# - Perubahan jumlah layer
# - Perubahan ukuran tiap layer
# - Mudah digunakan untuk hyperparameter tuning (misalnya Optuna)
# -------------------------


# -------------------------
# Output Layer
# -------------------------
# Dense(num_classes) tanpa aktivasi:
# - Menghasilkan logits (nilai mentah sebelum softmax)
# - Digunakan bersama loss:
#   SparseCategoricalCrossentropy(from_logits=True)
#
# Softmax akan dihitung secara implisit di dalam fungsi loss
# -------------------------


# -------------------------
# Forward Pass (call)
# -------------------------
# Alur eksekusi saat model dipanggil:
# 1. Input dicast ke float32
# 2. Normalisasi menggunakan preprocess_input ResNet50
#    (standar ImageNet)
# 3. Ekstraksi fitur oleh backbone ResNet50
# 4. Fitur dilewatkan ke Dense + Dropout sesuai konfigurasi
# 5. Output akhir berupa logits
# -------------------------


# -------------------------
# Output Model
# -------------------------
# Bentuk output:
# - Tensor berukuran (batch_size, num_classes)
#
# Output ini kompatibel dengan training dan evaluasi
# berbasis classification loss dari_logits=True
# -------------------------


# -------------------------
# Kenapa Disebut "Dynamic"?
# -------------------------
# Karena arsitektur head tidak hard-coded:
# - Jumlah layer bisa diubah (panjang layer_configs)
# - Ukuran tiap layer bisa disesuaikan
# - Dropout rate bisa dituning
#
# Cocok untuk:
# - Baseline manual
# - Eksperimen arsitektur
# - Hyperparameter optimization otomatis
# -------------------------
