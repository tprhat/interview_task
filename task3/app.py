from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['POST'])
def calculate_max_interviews():
    data = request.json

    start_times = data.get('start_times', [])
    end_times = data.get('end_times', [])

    if len(start_times) != len(end_times):
        return jsonify({'error': 'Start times and end times lists must have the same length'}), 400

    # Sort the intervals by end time
    intervals = sorted(zip(start_times, end_times), key=lambda x: x[1])

    max_interviews = 0
    current_end = float('-inf')

    for start, end in intervals:
        if start >= current_end:
            max_interviews += 1
            current_end = end

    return jsonify({'max_interviews': max_interviews})


if __name__ == '__main__':
    app.run()
