# Provided code
# This function checks to ensure that a list is of length
# 8 and that each element is type float
# Parameters:
# row - a list to check
# Returns True if the length of row is 8 and all elements are floats
def check_row_types(row):
    if len(row) != 8:
        print("Length incorrect! (should be 8): " + str(row))
        return False
    ind = 0
    while ind < len(row):
        if type(row[ind]) != float:
            print("Type of element incorrect: " + str(row[ind]) + " which is " + str(type(row[ind])))
            return False
        ind += 1
    return True
	
# define your functions here
#Converts a list of strings to a list of floats
def convert_row_type(data_lst):
    return [float(i) for i in data_lst]

# Calculates the score of the student for enrollment purposes
def calculate_score(data_lst):
    norm_gpa = data_lst[1]*2.0
    norm_sat = data_lst[0]/160.0
    score = 0.0
    score += norm_sat * 0.3
    score += norm_gpa * 0.4
    score += data_lst[2] * 0.1
    score += data_lst[3] * 0.2
    return score

# Checks if the given student is an outlier with no internet or abnormally high SAT
def is_outlier(data_lst):
    if data_lst[2] == 0 or data_lst[0]/160.0 < (data_lst[1]*2) - 2:
        return True
    return False

# Calculates the students score and takes into account if they are an outlier
def calculate_score_improved(score_lst):
    score = 0
    score += ((score_lst[0]/160)*0.3) + ((score_lst[1]*2)*0.4) + (score_lst[2]*0.1) + (score_lst[3]*0.2)
    if is_outlier(score_lst) or score >= 6:
        return True
    return False

# Checks if there is a single abnormally low grade.
def grade_outlier(grade_lst):
    sorted_grades = sorted(grade_lst)
    if (sorted_grades[1] - sorted_grades[0]) > 20:
        return True
    return False

# Sees if their grades steadily over 4 semesters
def grade_improvement(grades):
    sorted_grades = sorted(grades)
    if sorted_grades == grades:
        return True
    return False

def main():
    # Opening files. Don't worry, I close them all at the end. This is how the assignment had them set up to start.
    filename = "admission_algorithms_dataset.csv"
    out_name = "student_scores.csv"
    chosen_name = "chosen_students.csv"
    outlier_name = "outliers.csv"
    improved_outlier_name = "chosen_improved.csv"
    better_improved_name = "better_improved.csv"
    composite_chosen_name = "composite_chosen.csv"
    input_file = open(filename, "r")
    output_file = open(out_name, "w")
    chosen_file = open(chosen_name, "w")
    outlier_file = open(outlier_name, "w")
    improved_outlier_file = open(improved_outlier_name, "w")
    better_improved_file = open(better_improved_name, "w")
    composite_chosen_file = open(composite_chosen_name, "w")
    print("Processing " + filename + "...")
    # grab the line with the headers
    headers = input_file.readline()
    
    # TODO: loop through the rest of the file
    student_list = []
    student_names = []
    lines = input_file.readlines()
    converted_list = []
    
    for row in range(len(lines)):
        # Creates a list from the file, removing the commas and whitespace
        student_list.append(lines[row].strip().split(","))
        # Creates a list of just student names
        student_names.append(student_list[row].pop(0))
        # Creates a list of the numbers tied to students.
        converted_list.append(convert_row_type(student_list[row]))
        check_row_types(converted_list[row])
        output_file.write(f"{student_names[row]},{calculate_score(converted_list[row]):.2f}\n")
        if calculate_score(converted_list[row]) >= 6:
            chosen_file.write(f"{student_names[row]}\n")
        if is_outlier(converted_list[row]):
            outlier_file.write(f"{student_names[row]}\n")
        if calculate_score(converted_list[row]) >= 6 or calculate_score(converted_list[row]) >= 5 and is_outlier(converted_list[row]):
            improved_outlier_file.write(f"{student_names[row]}\n")
        if calculate_score_improved(converted_list[row]):
            better_improved_file.write(f"{student_names[row]},{str(converted_list[row][0])},{str(converted_list[row][1])},{str(converted_list[row][2])},{str(converted_list[row][3])}\n")
        if calculate_score(converted_list[row]) >= 6 or calculate_score(converted_list[row]) >= 5 and (is_outlier(converted_list[row]) or grade_outlier(converted_list[row][4:]) or grade_improvement(converted_list[row][4:])):
            composite_chosen_file.write(f"{student_names[row]}\n")

    # TODO: make sure to close all files you've opened!
    input_file.close(), output_file.close(), chosen_file.close(), outlier_file.close(), improved_outlier_file.close(), better_improved_file.close(), composite_chosen_file.close()

    print("done!")

# this bit allows us to both run the file as a program or load it as a
# module to just access the functions
if __name__ == "__main__":
    main()