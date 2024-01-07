def find_s(dataset, y):
    hypothesis = dataset[0][:-1]

    for sample in dataset:
        if sample[-1] == y:
            for i in range(len(hypothesis)):
                if sample[i] != hypothesis[i]:
                    hypothesis[i] = '?'
    
    return hypothesis

def find_final_s(dataset):
    final_hypothesis_1 = find_s(dataset, '1')
    final_hypothesis_2 = find_s(dataset, '0')

    if final_hypothesis_1.count('?') < final_hypothesis_2.count('?'):
        print('Final Hypothesis: ', final_hypothesis_1)
    else:
        print('Final Hypothesis: ', final_hypothesis_2)

dataset_1 = [
    ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', '1'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', '1'],
    ['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change', '0'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change', '1']
]

dataset_2 = [
    ['Japan', 'Honda', 'Blue', '2020', 'Eco', '1'],
    ['Japan', 'Toyota', 'Green', '2022', 'Sport', '0'],
    ['Japan', 'Toyota', 'Blue', '2019', 'Eco', '1'],
    ['USA', 'Audi', 'Red', '2018', 'Eco', '0'],
    ['Japan', 'Honda', 'White', '2023', 'Eco', '1'],
    ['Japan', 'Toyota', 'Green', '2016', 'Eco', '1'],
    ['Japan', 'Honda', 'Red', '2017', 'Eco', '0']
]

dataset_3 = [
    ['Big', 'Red', 'Circle', '0'],
    ['Small', 'Red', 'Triangle', '0'],
    ['Small', 'Red', 'Circle', '1'],
    ['Big', 'Blue', 'Circle', '0'],
    ['Small', 'Blue', 'Circle', '1']
]

dataset_4 = [
    ['Overcast', 'Hot', 'High', 'False', '1'],
    ['Rainy', 'Mild', 'High', 'False', '1'],
    ['Rainy', 'Cool', 'Normal', 'False', '1'],
    ['Rainy', 'Cool', 'Normal', 'True', '0'],
    ['Overcast', 'Cool', 'Normal', 'True', '1'],
    ['Sunny', 'Mild', 'High', 'False', '0'],
    ['Sunny', 'Cool', 'Normal', 'False', '1'],
    ['Rainy', 'Mild', 'Normal', 'False', '1'],
    ['Sunny', 'Mild', 'Normal', 'True', '1'],
    ['Rainy', 'Mild', 'High', 'True', '0']
]

find_final_s(dataset_4)