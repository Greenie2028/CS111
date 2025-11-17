def list_sort(lst):
    lst.sort()
    lst.reverse()
    return lst

def get_grade_percent(grades, total_points):
    if isinstance(grades, float):
        return grades/total_points
    return sum(grades)/total_points

def get_letter(total_avg):
    if total_avg >= 93.0:
        return "A"
    elif total_avg >= 90:
        return "A-"
    elif total_avg >= 87:
        return "B+"
    elif total_avg >= 83:
        return "B"
    elif total_avg >= 80:
        return "B-"
    elif total_avg >= 77:
        return "C+"
    elif total_avg >= 73:
        return "C"
    elif total_avg >= 70:
        return "C-"
    elif total_avg >= 67:
        return "D+"
    elif total_avg >= 63:
        return "D"
    elif total_avg >= 60:
        return "D-"
    else:
        return "E" 

def main():
    # Get input file
    input_name = input("Please enter the grade data filename: ")
    #input_name = "test_files\\grades2.test.dat"

    with open(input_name, 'r') as grade_file:
        lines = grade_file.readlines()

    row = 0
    while row < len(lines):
        if lines[row][0] == "#" or lines[row] == "\n":
            lines.pop(row)
        else:
            row +=1
    for i in range(len(lines)):
        lines[i] = lines[i].strip().split(", ")
    lab_grade = []
    hw_grade = []
    proj_grade = []
    pc_grade = []
    midterm1_grade = 0.0
    has_mt1 = False
    midterm2_grade = 0.0
    has_mt2 = False
    midterm3_grade = 0.0
    has_mt3 = False
    final_grade = 0.0
    has_final = False
    #Sorting out the file into different grade times
    for i in range(len(lines)):
        if lines[i][0][:-2] == "Lab":
            lab_grade.append(float(lines[i][1]))

        elif lines[i][0][:-1] == "Homework":
            hw_grade.append(float(lines[i][1]))

        elif lines[i][0][:-1] == "Project" or lines[i][0] == "FreeCoding":
            proj_grade.append(float(lines[i][1]))

        elif lines[i][0][:-1] == "ProgressCheck":
            pc_grade.append(float(lines[i][1]))

        elif lines[i][0] == "Midterm1":
            midterm1_grade = float(lines[i][1])
            has_mt1 = True
        elif lines[i][0] == "Midterm2":
            midterm2_grade = float(lines[i][1])
            has_mt2 = True
        elif lines[i][0] == "Midterm3":
            midterm3_grade = float(lines[i][1])
            has_mt3 = True
        else:
            final_grade = float(lines[i][1])
            has_final = True

    #Total Points Vars
    lab_total = 0.0
    hw_total = 0.0
    proj_total = 0.0
    pc_total = 0.0
    
    total_avg = 0.0
    
    #lab total points
    lab_grade = list_sort(lab_grade)
    lab_grade.pop()
    lab_grade.pop()
    lab_total = len(lab_grade) * 20

    #homework total points
    hw_grade = list_sort(hw_grade)
    hw_grade.pop()
    hw_total = len(hw_grade) * 50

    #project total
    proj_total = len(proj_grade) * 100

    #progress check total
    pc_total = len(pc_grade) * 100

    #Total average based on if midterms and finals have been completed
    total_avg = ((get_grade_percent(lab_grade, lab_total)*10) + (get_grade_percent(hw_grade, hw_total)*10)
        + (get_grade_percent(proj_grade,proj_total)*20) + (get_grade_percent(pc_grade, pc_total)*10))
    if has_final:
        total_avg += ((get_grade_percent(midterm1_grade, 20)*10) + (get_grade_percent(midterm2_grade, 20)*10) 
        + (get_grade_percent(midterm3_grade, 20)*10) + (get_grade_percent(final_grade, 70)*20))
    elif has_mt3:
        total_avg += (get_grade_percent(midterm1_grade, 20)*10) + (get_grade_percent(midterm2_grade, 20)*10) + (get_grade_percent(midterm3_grade, 20)*10)
        total_avg /= 0.8
    elif has_mt2:
        total_avg += (get_grade_percent(midterm1_grade, 20)*10) + (get_grade_percent(midterm2_grade, 20)*10)
        total_avg /= 0.7
    elif has_mt1:
        total_avg += (get_grade_percent(midterm1_grade, 20)*10)
        total_avg /= 0.6
    else:
        total_avg /= 0.5

    #Final Output
    print("Here are the students grades:")
    print("Category, Points, Percentage")
    print(f"Labs: {sum(lab_grade):.1f}/{lab_total} {(sum(lab_grade)/lab_total)*100:.1f}%")
    print(f"Homeworks: {sum(hw_grade):.1f}/{hw_total} {(sum(hw_grade)/hw_total)*100:.1f}%")
    print(f"Projects: {sum(proj_grade):.1f}/{proj_total} {(sum(proj_grade)/proj_total)*100:.1f}%")
    print(f"Progress Checks: {sum(pc_grade):.1f}/{pc_total} {(sum(pc_grade)/pc_total)*100:.1f}%")
    if has_mt1:
        print(f"Midterm 1: {midterm1_grade:.1f}/20 {(midterm1_grade/20)*100:.1f}%")
    if has_mt2:
        print(f"Midterm 2: {midterm2_grade:.1f}/20 {(midterm2_grade/20)*100:.1f}%")
    if has_mt3:
        print(f"Midterm 3: {midterm3_grade:.1f}/20 {(midterm3_grade/20)*100:.1f}%")
    if has_final:
        print(f"Final: {final_grade:.1f}/70 {(final_grade/70)*100:.1f}%")
    print()
    print(f"The overall grade in the class is: {get_letter(total_avg)} ({total_avg:.2f}%)")

if __name__ == "__main__":
    main()