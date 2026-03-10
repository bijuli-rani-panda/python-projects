"""
Student Grade Manager
A Python application to manage student grades, track performance, and generate reports.
"""

import csv
import os
from datetime import datetime

# File paths
STUDENTS_FILE = 'students.csv'
GRADES_FILE = 'grades.csv'

class Student:
    """Represents a student with their information and grades."""
    
    def __init__(self, student_id, name, age, city):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.city = city
        self.grades = {}  # subject: grade
    
    def add_grade(self, subject, grade):
        """Add or update a grade for a subject."""
        self.grades[subject] = grade
    
    def get_average(self):
        """Calculate the average grade across all subjects."""
        if not self.grades:
            return 0
        return sum(self.grades.values()) / len(self.grades)
    
    def get_letter_grade(self):
        """Convert average to letter grade."""
        avg = self.get_average()
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        elif avg >= 60:
            return 'D'
        else:
            return 'F'
    
    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, City: {self.city}"


class GradeManager:
    """Manages all student grade operations."""
    
    def __init__(self):
        self.students = {}
        self.load_students()
        self.load_grades()
    
    def load_students(self):
        """Load students from CSV file."""
        if os.path.exists(STUDENTS_FILE):
            try:
                with open(STUDENTS_FILE, 'r', newline='', encoding='utf-8') as f:
                    reader = csv.DictReader(f)
                    student_id = 1
                    for row in reader:
                        student = Student(
                            student_id,
                            row['Name'],
                            int(row['Age']),
                            row['City']
                        )
                        self.students[student_id] = student
                        student_id += 1
                print(f"✓ Loaded {len(self.students)} students from {STUDENTS_FILE}")
            except Exception as e:
                print(f"Error loading students: {e}")
        else:
            print(f"{STUDENTS_FILE} not found. Starting with empty database.")
    
    def load_grades(self):
        """Load grades from CSV file."""
        if os.path.exists(GRADES_FILE):
            try:
                with open(GRADES_FILE, 'r', newline='', encoding='utf-8') as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        student_id = int(row['StudentID'])
                        if student_id in self.students:
                            subject = row['Subject']
                            grade = float(row['Grade'])
                            self.students[student_id].add_grade(subject, grade)
                print(f"✓ Loaded grades successfully")
            except Exception as e:
                print(f"Error loading grades: {e}")
        else:
            print(f"{GRADES_FILE} not found. No grades loaded.")
    
    def save_grades(self):
        """Save grades to CSV file."""
        try:
            with open(GRADES_FILE, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['StudentID', 'Subject', 'Grade'])
                for student in self.students.values():
                    for subject, grade in student.grades.items():
                        writer.writerow([student.student_id, subject, grade])
            print(f"✓ Grades saved to {GRADES_FILE}")
        except Exception as e:
            print(f"Error saving grades: {e}")
    
    def add_student(self, name, age, city):
        """Add a new student."""
        student_id = max(self.students.keys(), default=0) + 1
        student = Student(student_id, name, age, city)
        self.students[student_id] = student
        print(f"✓ Student '{name}' added with ID: {student_id}")
        return student_id
    
    def remove_student(self, student_id):
        """Remove a student by ID."""
        if student_id in self.students:
            name = self.students[student_id].name
            del self.students[student_id]
            print(f"✓ Student '{name}' (ID: {student_id}) removed")
            return True
        print(f"✗ Student with ID {student_id} not found")
        return False
    
    def add_grade(self, student_id, subject, grade):
        """Add or update a student's grade."""
        if student_id in self.students:
            self.students[student_id].add_grade(subject, grade)
            print(f"✓ Grade added: {self.students[student_id].name} - {subject}: {grade}")
            return True
        print(f"✗ Student with ID {student_id} not found")
        return False
    
    def remove_grade(self, student_id, subject):
        """Remove a grade for a specific subject."""
        if student_id in self.students:
            student = self.students[student_id]
            if subject in student.grades:
                del student.grades[subject]
                print(f"✓ Grade removed for {student.name} in {subject}")
                return True
            print(f"✗ No grade found for {subject}")
            return False
        print(f"✗ Student with ID {student_id} not found")
        return False
    
    def view_student(self, student_id):
        """View details of a specific student."""
        if student_id in self.students:
            student = self.students[student_id]
            print("\n" + "="*50)
            print(f"Student Details")
            print("="*50)
            print(f"ID: {student.student_id}")
            print(f"Name: {student.name}")
            print(f"Age: {student.age}")
            print(f"City: {student.city}")
            print("-"*50)
            print("Grades:")
            if student.grades:
                for subject, grade in student.grades.items():
                    print(f"  {subject}: {grade}")
                print(f"Average: {student.get_average():.2f}")
                print(f"Letter Grade: {student.get_letter_grade()}")
            else:
                print("  No grades recorded")
            print("="*50 + "\n")
            return True
        print(f"✗ Student with ID {student_id} not found")
        return False
    
    def view_all_students(self):
        """View all students with their grades."""
        if not self.students:
            print("No students in the system")
            return
        
        print("\n" + "="*80)
        print(f"{'ID':<5} {'Name':<15} {'Age':<5} {'City':<15} {'Average':<10} {'Grade':<6}")
        print("="*80)
        for student in self.students.values():
            avg = student.get_average()
            letter = student.get_letter_grade()
            print(f"{student.student_id:<5} {student.name:<15} {student.age:<5} {student.city:<15} {avg:<10.2f} {letter:<6}")
        print("="*80 + "\n")
    
    def view_all_grades(self):
        """View all grades for all students."""
        if not self.students:
            print("No students in the system")
            return
        
        print("\n" + "="*80)
        print("All Student Grades")
        print("="*80)
        for student in self.students.values():
            print(f"\n{student.name} (ID: {student.student_id}):")
            if student.grades:
                for subject, grade in student.grades.items():
                    print(f"  {subject}: {grade}")
                print(f"  Average: {student.get_average():.2f} ({student.get_letter_grade()})")
            else:
                print("  No grades recorded")
        print("="*80 + "\n")
    
    def find_top_performers(self):
        """Find students with highest averages."""
        if not self.students:
            print("No students in the system")
            return
        
        sorted_students = sorted(
            self.students.values(),
            key=lambda s: s.get_average(),
            reverse=True
        )
        
        print("\n" + "="*50)
        print("Top Performers (Ranked by Average)")
        print("="*50)
        for i, student in enumerate(sorted_students[:5], 1):
            print(f"{i}. {student.name}: {student.get_average():.2f} ({student.get_letter_grade()})")
        print("="*50 + "\n")
    
    def find_students_by_subject(self, subject):
        """Find all students who have a grade in a specific subject."""
        if not self.students:
            print("No students in the system")
            return
        
        students_with_subject = [
            s for s in self.students.values()
            if subject in s.grades
        ]
        
        if not students_with_subject:
            print(f"No students have grades in {subject}")
            return
        
        students_with_subject.sort(key=lambda s: s.grades[subject], reverse=True)
        
        print("\n" + "="*50)
        print(f"Students in {subject}")
        print("="*50)
        for student in students_with_subject:
            print(f"{student.name}: {student.grades[subject]}")
        print("="*50 + "\n")
    
    def class_average(self):
        """Calculate the overall class average."""
        if not self.students:
            print("No students in the system")
            return
        
        total_avg = 0
        count = 0
        for student in self.students.values():
            if student.grades:
                total_avg += student.get_average()
                count += 1
        
        if count > 0:
            print(f"\nClass Average: {total_avg/count:.2f}\n")
        else:
            print("\nNo grades recorded yet\n")


def display_menu():
    """Display the main menu."""
    print("\n" + "="*50)
    print("   STUDENT GRADE MANAGER")
    print("="*50)
    print("1.  Add New Student")
    print("2.  Remove Student")
    print("3.  Add/Update Grade")
    print("4.  Remove Grade")
    print("5.  View Student Details")
    print("6.  View All Students")
    print("7.  View All Grades")
    print("8.  Find Top Performers")
    print("9.  Find Students by Subject")
    print("10. Class Average")
    print("11. Save Grades to File")
    print("0.  Exit")
    print("="*50)


def get_choice(prompt, data_type=int):
    """Get validated user input."""
    while True:
        try:
            value = data_type(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please try again.")


def main():
    """Main function to run the grade manager."""
    print("\n" + "="*50)
    print("   WELCOME TO STUDENT GRADE MANAGER")
    print("="*50)
    
    manager = GradeManager()
    
    while True:
        display_menu()
        choice = get_choice("Enter your choice: ")
        
        if choice == 0:
            print("\nThank you for using Student Grade Manager!")
            print("Goodbye!")
            break
        
        elif choice == 1:
            print("\n--- Add New Student ---")
            name = input("Enter name: ").strip()
            age = get_choice("Enter age: ")
            city = input("Enter city: ").strip()
            if name and city:
                manager.add_student(name, age, city)
            else:
                print("Name and city cannot be empty")
        
        elif choice == 2:
            print("\n--- Remove Student ---")
            manager.view_all_students()
            student_id = get_choice("Enter student ID to remove: ")
            manager.remove_student(student_id)
        
        elif choice == 3:
            print("\n--- Add/Update Grade ---")
            manager.view_all_students()
            student_id = get_choice("Enter student ID: ")
            subject = input("Enter subject: ").strip()
            grade = get_choice("Enter grade (0-100): ", float)
            if 0 <= grade <= 100:
                manager.add_grade(student_id, subject, grade)
            else:
                print("Grade must be between 0 and 100")
        
        elif choice == 4:
            print("\n--- Remove Grade ---")
            manager.view_all_students()
            student_id = get_choice("Enter student ID: ")
            subject = input("Enter subject to remove grade: ").strip()
            manager.remove_grade(student_id, subject)
        
        elif choice == 5:
            print("\n--- View Student Details ---")
            manager.view_all_students()
            student_id = get_choice("Enter student ID: ")
            manager.view_student(student_id)
        
        elif choice == 6:
            print("\n--- View All Students ---")
            manager.view_all_students()
        
        elif choice == 7:
            print("\n--- View All Grades ---")
            manager.view_all_grades()
        
        elif choice == 8:
            print("\n--- Top Performers ---")
            manager.find_top_performers()
        
        elif choice == 9:
            print("\n--- Find Students by Subject ---")
            subject = input("Enter subject name: ").strip()
            manager.find_students_by_subject(subject)
        
        elif choice == 10:
            print("\n--- Class Average ---")
            manager.class_average()
        
        elif choice == 11:
            print("\n--- Save Grades ---")
            manager.save_grades()
        
        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()
