from __future__ import print_function

#  How to process data in list 
student_data = [
    {"name": "Kortze", "id": 1, "scores": [68, 70, 56, 98]},
    {"name": "Kalo", "id": 2, "scores": [68, 100, 56, 100]},
    {"name": "Jamu", "id": 3, "scores": [68, 75, 56, 81]},
    {"name": "Kliki", "id": 4, "scores": [68, 98, 56, 100]},
    {"name": "Robert", "id": 5, "scores": [73, 99, 56, 81]},
    {"name": "Che", "id": 6, "scores": [92, 76, 56, 73]},
    {"name": "Uche", "id": 7, "scores": [68, 88, 56, 81]},
    {"name": "Mikee", "id": 8, "scores": [77, 75, 56, 82]},
    {"name": "Bob", "id": 9, "scores": [68, 56, 56, 60]},
]


def process_student_data(data, pass_threshold=60, merit_threshold=75):
    #  Perform some basic stats on student data
    for sdata in data:
        # Averages the total of the first student's scores and returns that average for comparsion
        # before it is
        av = sum(sdata["scores"]) / float(len(sdata["scores"]))
        sdata["average"] = av  # Assign av to each data

        # Compare if the average is higer than the merit_threshold
        if av > merit_threshold:
            # Assign av to each data
            sdata["assessment"] = "passed with merit"
        # Compare if the average is higer than the pass_threshold
        elif av > pass_threshold:
            # Assign av to each data
            sdata["assessment"] = "passed"
        # If non is true then assessment is failed
        else:
            # Assign av to each data
            sdata["assessment"] = "failed"
        # Print
        print(
            "%s's (id: %d) final assessment is: %s"
            % (sdata["name"], sdata["id"], sdata["assessment"].upper())
        )


if __name__ == "__main__":
    process_student_data(student_data)
