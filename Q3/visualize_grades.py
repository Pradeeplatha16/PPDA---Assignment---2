# File: visualize_grades.py
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import glob

# Function to read and combine grades from multiple CSV files
def load_grades_from_csv(directory):
    # Use glob to find all CSV files in the directory
    all_files = glob.glob(f"{directory}/*.csv")
    grades = []

    for file in all_files:
        # Read each CSV file
        df = pd.read_csv(file)
        grades.extend(df['Grade'].tolist())  # Extend the grades list

    return grades

# Function to create a histogram for student grades
def plot_grade_distribution(grades):
    # Create the histogram
    plt.figure(figsize=(10, 6))
    n, bins, patches = plt.hist(grades, bins=10, edgecolor='black', color='lightblue')

    # Title and labels
    plt.title('Distribution of Student Grades', fontsize=16)
    plt.xlabel('Grades', fontsize=14)
    plt.ylabel('Number of Students', fontsize=14)

    # Highlight specific grade ranges using different colors
    for patch, grade in zip(patches, bins):
        if grade < 50:  # Fail grades
            patch.set_facecolor('red')
        elif 50 <= grade < 75:  # Pass grades
            patch.set_facecolor('yellow')
        else:  # Distinction grades
            patch.set_facecolor('green')

    # Create a legend with colored patches for grade ranges
    red_patch = mpatches.Patch(color='red', label='Failing (< 50)')
    yellow_patch = mpatches.Patch(color='yellow', label='Passing (50-74)')
    green_patch = mpatches.Patch(color='green', label='Distinction (75+)')

    plt.legend(handles=[red_patch, yellow_patch, green_patch], loc='upper right')

    # Show the plot
    plt.tight_layout()
    plt.show()

# Main function to execute the visualization
if __name__ == "__main__":
    grades = load_grades_from_csv('StudentGradesVisualization')
    plot_grade_distribution(grades)
