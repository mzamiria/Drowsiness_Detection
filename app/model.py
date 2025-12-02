

from tensorflow.keras.models import model_from_json
import numpy as np
import tensorflow as tf


# GPU settings
##config = tf.compat.v1.ConfigProto()
#config.gpu_options.per_process_gpu_memory_fraction = 0.15
#session=tf.compat.v1.Session(config=config)

class Awakeness(object):

    EYE_STATUS_LIST=['Close','Open']

    def __init__(self,model_json_file,model_weights_file):
        with open(model_json_file,'r' ) as json_file:
            loaded_model_json=json_file.read()
            self.loaded_model=model_from_json(loaded_model_json)

        self.loaded_model.load_weights(model_weights_file)
        self.loaded_model.make_predict_function()

    def predict_eye_status(self,img):
        self.preds=self.loaded_model.predict(img)
        return Awakeness.EYE_STATUS_LIST[np.argmax(self.preds)]
