# ME 405 Homework 0x00 by Evan Tran
from matplotlib import pyplot

# CODE FOR GENERATING PLOT VALUES
def load_labels(filename: str) -> list:
    with open(filename, 'r') as file:
        empty_list = []
        for line in file:
            empty_list.append(line)
        labels = empty_list[0]
        empty_list.pop(0)
        #print(labels)
        list1 = labels.split(',')
        list2 = []
        for item in list1:
            list2.append(item.strip())
        #print(list2)
        return list2

# CODE FOR GETTING VALUES FROM CSV FILE
def load_values(filename: str) -> tuple[list, list]:
    with open(filename, 'r') as file:
        empty_list = []
        for line in file:
            empty_list.append(line)
        empty_list.pop(0)
        list3 = []
        for item in empty_list:
            list3.append(item.strip())
        #print(list3)
        x_values = []
        y_values = []
        list4 = []
        for item in list3:
            try:
                stripped_item = item.strip()
                #print(stripped_item, type(stripped_item), stripped_item[0])
                if stripped_item[0] == '#':
                    list3.remove(item)
                elif stripped_item[0] == '':
                    list3.remove(item)
                else:
                    list4.append(item)
            except IndexError:
                continue
        list5 = []
        for item in list4:
            #print(item.split(','), type(item.split(',')))
            if len(item.split(',')) == 1:
                list4.remove(item)
            else:
                list5.append(item.split(','))
        #print(list5)
        for value in list5:
            try:
                x_values.append(float(value[0]))
                y_values.append(float(value[1]))
            except ValueError:
                continue
        # print(x_values)
        # print(y_values)
        # print(len(x_values), len(y_values))
        return x_values, y_values

# CODE FOR PLOTTING GRAPH
def plot_graph(labels: list, x_values: list, y_values: list) -> None:
    x_label = labels[0]
    y_label = labels[1]
    pyplot.xlabel(x_label)
    pyplot.ylabel(y_label)
    pyplot.plot(x_values, y_values)
    pyplot.show()

labels = load_labels('data.csv')
values = load_values('data.csv')
plot_graph(labels, values[0], values[1])