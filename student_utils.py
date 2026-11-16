def calculate_average(scores):
    """Ballar siyahısından orta balı hesablayıb qaytarır."""
    if not scores:
        return 0.0
    return sum(scores) / len(scores)
def get_highest_score(scores):
    """Siyahıdakı ən yüksək balı qaytarır."""
    return max(scores)
def get_lowest_score(scores):
    """Siyahıdakı ən aşağı balı qaytarır."""
    return min(scores)
def process_students(student_list):
    """Hər bir tələbənin adını ayrı sətirdə və ümumi sayını ekrana çıxarır."""
    print("Students:")
    for student in student_list:
        print(student)
    print("Total Students:", len(student_list))
def register_students(*students):
    """İstənilən sayda tələbə adını qəbul edir və qeydiyyatdan keçənləri göstərir."""
    print("Registered Students:")
    for student in students:
        print(student)
    print("Total:", len(students))