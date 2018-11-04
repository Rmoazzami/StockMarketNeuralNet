import sys
import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense, Activation
from sklearn.model_selection import train_test_split


"""
    To run: python ml.py <data-filename> <"load" to load trained net>

"""

if __name__ == "__main__":
    filename = sys.argv[1]
    data = pd.read_pickle(filename)
    data = data.values
    print(len(data))
    print(len(data[0]))
    labels = data[:, -3:]
    data = data[:, 2:-3]
    features = len(data[0])
    for i in range(len(data)):
        val = str(data[i, 2])
        data[i, 2] = int(val)
    print(labels)
    print(data)
    """
    data = np.random.random((1000, features))
    labels = np.random.randint(2, size=(1000, 3))
    """
    train_data, test_data, train_labels, test_labels = train_test_split(data, labels, test_size=.2)
    model = 0
    if sys.argv[2] == 'load':
        json_file = open('model.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        model = model_from_json(loaded_model_json)
        # load weights into new model
        model.load_weights("model.h5")
    else:
        model = Sequential()
        model.add(Dense(features * 2, input_shape=(len(train_data[0]), ), activation='linear'))
        model.add(Dense(features * 2, activation='linear'))
        model.add(Dense(3, init='uniform', activation='linear'))
        model.compile(optimizer='adam',
                  loss='mean_squared_error',
                  metrics=['accuracy'])
        model.fit(train_data, train_labels, epochs=10, batch_size=32)
        model_json = model.to_json()
        with open("model.json", "w") as json_file:
            json_file.write(model_json)
        model.save_weights("model.h5")
    score = model.evaluate(test_data, test_labels)
    print(score)
    print(model.predict(data[0:1000, :]))


    
