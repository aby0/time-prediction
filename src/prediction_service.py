"""
This contains a function which takes raw sentence and predicts the reading time

"""
from feature_extraction import calculate_features
from create_model import predict


def predict_time(text):
    feature = calculate_features(text)
    output = predict('../result/reading.pkl', [feature])

    return float(output.reshape(-1, 1)[0][0])


if __name__ == '__main__':
    para = "This is the text that needs to be calculated for time"
    print predict_time(para)
