import random
import hashlib
from datetime import datetime, timedelta
import os
import tkinter as tk
from tkinter import scrolledtext

# Import categories from another Python file
from categories import (
    electronics, mechanics, physics, software_engineering,
    biomechanics, bioelectromechanical_systems, quantum_computing,
    nanotechnology, advanced_materials, aerospace_engineering,
    energy_systems, biotechnology, artificial_intelligence, robotics,
    computational_neuroscience, cyber_physical_systems, genomic_engineering,
    advanced_robotics_and_automation, materials_science_at_the_nanoscale,
    theoretical_physics, electromechanical_systems, quantum_electronics,
    computational_mechanics, control_systems_engineering, photonics_engineering,
    microsystems_engineering, high_performance_computing, complexity_theory,
    astrophysics, thermodynamics, nonlinear_dynamics, advanced_numerical_methods,
    nano_electromechanical_systems, nanobots, electrodynamics, cybernetics,
    quantum_information_theory, biomechanical_engineering, materials_science,
    space_time_geometry
)

from templates import idea_templates

from topic_relationships import topic_relationships

# Path to store the last run date, sent ideas, and saved ideas
last_run_file = "last_run.txt"
sent_ideas_file = "sent_ideas.txt"
saved_ideas_file = "saved_ideas.txt"

# Settings
test_mode = True  # TODO: set this false if you want to generate and show ideas
ideas_per_display = 10  # TODO: set the number of ideas to display
run_interval_days = 7  # TODO: set the day intervals between showing ideas
skip_sent_ideas = True  # TODO: set based on preference for new ideas

# Define topic relationships (example format)
# Higher weight means more likely to appear together


# Function to generate a hash for an idea
def hash_idea(idea):
    return hashlib.sha256(idea.encode()).hexdigest()

# Function to generate a single random idea considering relationships
def generate_idea():
    all_topics = [
        electronics, mechanics, physics, software_engineering,
        biomechanics, bioelectromechanical_systems, quantum_computing,
        nanotechnology, advanced_materials, aerospace_engineering,
        energy_systems, biotechnology, artificial_intelligence, robotics,
        computational_neuroscience, cyber_physical_systems, genomic_engineering,
        advanced_robotics_and_automation, materials_science_at_the_nanoscale,
        theoretical_physics, electromechanical_systems, quantum_electronics,
        computational_mechanics, control_systems_engineering, photonics_engineering,
        microsystems_engineering, high_performance_computing, complexity_theory,
        astrophysics, thermodynamics, nonlinear_dynamics, advanced_numerical_methods,
        nano_electromechanical_systems, nanobots, electrodynamics, cybernetics,
        quantum_information_theory, biomechanical_engineering, materials_science,
        space_time_geometry
    ]
    
    topic_list = [topic for sublist in all_topics for topic in sublist]

    selected_topics = []

    for _ in range(5):  # Generate 5 topics for the idea
        possible_topics = list(set(topic_list) - set(selected_topics))
        
        if selected_topics:
            last_topic = selected_topics[-1]
            if last_topic in topic_relationships:
                weighted_topics = [topic for topic in possible_topics if topic in topic_relationships[last_topic]]
                if weighted_topics:
                    selected_topic = random.choices(weighted_topics, [topic_relationships[last_topic][topic] for topic in weighted_topics])[0]
                else:
                    selected_topic = random.choice(possible_topics)
            else:
                selected_topic = random.choice(possible_topics)
        else:
            selected_topic = random.choice(possible_topics)
        
        selected_topics.append(selected_topic)
    
    template = random.choice(idea_templates)
    try:
        idea = template.format(*random.sample(selected_topics, 5))
        print(f"Generated Idea: {idea}")  # Debug output
        return idea
    except Exception as e:
        print(f"Error generating idea: {e}")
        raise

# Function to save ideas to a file
def save_ideas(ideas):
    with open(saved_ideas_file, 'w') as file:
        for idea in ideas:
            file.write(idea + '\n')

# Function to load saved ideas from a file
def load_saved_ideas():
    if os.path.exists(saved_ideas_file):
        with open(saved_ideas_file, 'r') as file:
            return [line.strip() for line in file]
    return []

# Function to read the hashes of sent ideas from the file
def read_sent_idea_hashes():
    if os.path.exists(sent_ideas_file):
        with open(sent_ideas_file, 'r') as file:
            return set(line.strip() for line in file)
    return set()

# Function to append a new hash to the file
def append_sent_idea_hash(idea_hash):
    with open(sent_ideas_file, 'a') as file:
        file.write(idea_hash + '\n')

# Function to check if the script has run in the specified interval
def has_run_recently():
    if os.path.exists(last_run_file):
        with open(last_run_file, 'r') as file:
            last_run_date_str = file.read().strip()
            last_run_date = datetime.strptime(last_run_date_str, '%Y-%m-%d')
            if datetime.now() - last_run_date < timedelta(days=run_interval_days):
                return True
    return False

# Function to update the last run date
def update_last_run_date():
    with open(last_run_file, 'w') as file:
        file.write(datetime.now().strftime('%Y-%m-%d'))

# Function to show ideas in a window
def show_ideas_window(ideas):
    root = tk.Tk()
    root.title("Research Ideas")

    text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=20)
    text_area.pack(expand=True, fill='both')

    idea_text = "\n\n".join([f"Idea {i+1}:\n{ideas[i]}" for i in range(len(ideas))])
    text_area.insert(tk.END, idea_text)
    
    root.mainloop()

# Main function
def main():
    if test_mode:
        unique_ideas = load_saved_ideas()
        if not unique_ideas:
            unique_ideas = [generate_idea() for _ in range(ideas_per_display)]
            save_ideas(unique_ideas)
        show_ideas_window(unique_ideas)
    else:
        if not has_run_recently():
            all_ideas = [generate_idea() for _ in range(ideas_per_display)]
            sent_idea_hashes = read_sent_idea_hashes()
            unique_ideas = []

            for idea in all_ideas:
                idea_hash = hash_idea(idea)
                if not skip_sent_ideas or idea_hash not in sent_idea_hashes:
                    unique_ideas.append(idea)
                    if skip_sent_ideas:
                        append_sent_idea_hash(idea_hash)

            if unique_ideas:
                save_ideas(unique_ideas)
                show_ideas_window(unique_ideas)
                update_last_run_date()
            else:
                print("No new unique ideas to display.")
        else:
            print(f"The script has already run in the last {run_interval_days} days.")

# Run the main function
if __name__ == "__main__":
    main()
