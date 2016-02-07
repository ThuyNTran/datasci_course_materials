import csv
import matplotlib.pyplot as plt


def read_input():
    wanted_fields = ["Category", "DayOfWeek", "Date", "Time", "PdDistrict"]

    def field_extractor(dic):
        return dict([(field, dic[field]) for field in wanted_fields])

    data = []
    with open("sanfrancisco_incidents_summer_2014.csv", "r") as f:
        reader = csv.DictReader(f)
        for line in reader:
            data.append(field_extractor(line))
    return data


def plot_crime_type(data):
    # extract data
    crime_types = {}
    for rec in data:
        c_type = rec["Category"]
        crime_types[c_type] = crime_types.get(c_type, 0) + 1

    # plot data
    plt.rcdefaults()
    categories = crime_types.keys()
    y_pos = range(len(categories))
    plt.barh(y_pos, [crime_types[cat] for cat in crime_types],height=2, align='center', alpha=0.4)
    plt.yticks(y_pos, categories)
    plt.xlabel('Number of occurrence')
    plt.title('Total number of occurrence of every crime')

    plt.show()


def plot_crime_district(data):
    # extract data
    crime_count = {}
    for rec in data:
        d = rec["PdDistrict"]
        crime_count[d] = crime_count.get(d, 0) + 1

    districts = crime_count.keys()

    # plot data
    plt.rcdefaults()
    y_pos = map(lambda a: a, range(len(districts)))
    plt.barh(y_pos, [crime_count[d] for d in districts], align='center', alpha=0.4)
    plt.yticks(y_pos, districts, fontsize=8)
    plt.xlabel('Number of occurrence', fontsize=10)
    plt.title('Total number of occurrence in every district', fontsize=12)

    plt.show()


def plot_crime_time(data):
    crime_count = {}
    for rec in data:
        month = int(rec["Date"].split("/")[0])
        crime_count[month] = crime_count.get(month) or [0]*24
        t = rec["Time"]
        crime_count[month][int(t.split(":")[0])] += 1

    # plot data
    months = {8: "Aug.", 7: "Jul", 6: "Jun"}
    plt.rcdefaults()
    for month in crime_count:
        plt.plot(range(24), crime_count[month], label=months[month])
    plt.xlabel('Hour (00-23)', fontsize=10)
    plt.ylabel('Number of crime', fontsize=10)
    plt.title('Total number of crime over hours of day in every month', fontsize=12)
    plt.legend()

    ax = plt.gca()
    ax.grid(True)

    plt.show()


if __name__ == "__main__":
    input_data = read_input()
    plot_crime_time(input_data)
    print 'hi'




