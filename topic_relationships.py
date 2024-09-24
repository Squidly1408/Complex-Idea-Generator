# topic_relationships.py

# Topic relationships with both positive and negative weights
topic_relationships = {
    'Electronics': {'Software Engineering': {'positive': 5, 'negative': 0}, 
                    'Mechanical Engineering': {'positive': 3, 'negative': 0},
                    'Robotics': {'positive': 4, 'negative': 1}},
    'Software Engineering': {'Electronics': {'positive': 5, 'negative': 0}, 
                             'Robotics': {'positive': 4, 'negative': 0},
                             'Artificial Intelligence': {'positive': 5, 'negative': 1}},
    'Robotics': {'Electronics': {'positive': 4, 'negative': 0}, 
                 'Software Engineering': {'positive': 4, 'negative': 0}, 
                 'Artificial Intelligence': {'positive': 5, 'negative': 0},
                 'Mechanical Engineering': {'positive': 5, 'negative': 1}},
    'Bioelectromechanical Systems': {'Biomechanics': {'positive': 5, 'negative': 0}, 
                                     'Robotics': {'positive': 4, 'negative': 0}},
    'Biomechanics': {'Bioelectromechanical Systems': {'positive': 5, 'negative': 0}, 
                     'Computational Neuroscience': {'positive': 4, 'negative': 0}},
    'Quantum Computing': {'Advanced Materials': {'positive': 5, 'negative': 0},
                          'Nanotechnology': {'positive': 4, 'negative': 1},
                          'Physics': {'positive': 5, 'negative': 0}},
    'Advanced Materials': {'Quantum Computing': {'positive': 5, 'negative': 0}, 
                           'Artificial Intelligence': {'positive': 3, 'negative': 0},
                           'Energy Systems': {'positive': 4, 'negative': 1}},
    'Artificial Intelligence': {'Software Engineering': {'positive': 5, 'negative': 0},
                                'Robotics': {'positive': 5, 'negative': 0},
                                'Advanced Materials': {'positive': 3, 'negative': 0}},
    'Computational Neuroscience': {'Biomechanics': {'positive': 4, 'negative': 0},
                                   'Cyber-Physical Systems': {'positive': 3, 'negative': 1}},
    'Cyber-Physical Systems': {'Computational Neuroscience': {'positive': 3, 'negative': 1}},
    'Space-Time Geometry': {'Quantum Information Theory': {'positive': 4, 'negative': 0}},
    'Microsystems Engineering': {'Nanotechnology': {'positive': 4, 'negative': 0},
                                 'Photonics Engineering': {'positive': 3, 'negative': 1}},
    'Nanotechnology': {'Microsystems Engineering': {'positive': 4, 'negative': 0},
                       'Advanced Materials': {'positive': 3, 'negative': 1}},
    'Photonics Engineering': {'Microsystems Engineering': {'positive': 3, 'negative': 1}},
}

def display_relationships(relationships):
    """
    Displays the relationships between topics with positive and negative weights.
    """
    for topic, related_topics in relationships.items():
        print(f"{topic}:")
        for related_topic, weights in related_topics.items():
            print(f"  - {related_topic}: Positive Weight {weights['positive']}, Negative Weight {weights.get('negative', 0)}")

# Display relationships when run directly
if __name__ == "__main__":
    display_relationships(topic_relationships)
