def input_number(prompt=""):
    """
    A replacement for the built-in input() function that converts user input into a number.
    
    Parameters:
    - prompt (str): The prompt to display to the user.
    
    Returns:
    - int or float: The user's input converted to a number.
    
    Raises:
    - ValueError: If the input cannot be converted to a number.
    """
    while True:
        user_input = input(prompt)  # Use the built-in input() to get user input
        
        try:
            # Try converting to integer first
            return int(user_input)
        except ValueError:
            pass  # Not an integer, move to float conversion
        
        try:
            # Try converting to float if integer conversion fails
            return float(user_input)
        except ValueError:
            # Inform the user if the input is invalid
            print("Invalid input. Please enter a valid number.")
            
# October Reviews
oct_reviews = [
    [1001, 'October', 5, 'Great product! Highly recommend.'],
    [1002, 'October', 4, 'Good value for money. Could be better.'],
    [1003, 'October', 2, 'Stopped working after a month. Disappointed.'],
    [1004, 'October', 1, 'Terrible quality. Broke after a week.'],
    [1005, 'October', 3, 'Average. Nothing special.'],
    [1006, 'October', 2, 'Not worth the price. Broke within a few days.'],
    [1007, 'October', 5, 'Excellent quality! Very satisfied.'],
    [1008, 'October', 4, 'Works well, but could be more durable.']]

# November Reviews
nov_reviews = [
    [1010, 'November', 5, 'Love it! Definitely recommend.'], 
    [1011, 'November', None, 'Gets the job done. Worth the money.'],
    [1012, 'November', 2, 'Broke after two weeks. Definitely not satisfied.'],
    [1013, 'November', 2, 'Broke after two weeks. Definitely not satisfied.'],
    [1014, 'November', 1, 'Terrible quality. Completely useless after it broke.'],
    [1015, 'November', 5, 'Amazing product! Would buy again.'],
    [1016, 'November', 3, 'Decent performance but overpriced.'],
    [1017, 'November', 3, 'Decent performance but overpriced.'],
    [1018, 'November', 2, 'Stopped working. Very disappointing.'],
    [1019, 'November', None, 'Not great, but works for now.'],
    [1020, 'November', None, 'Broke within a few days. Would not recommend.'], 
    [1021, 'November', 1, 'Awful experience. It broke after just one use!']]

may_hires = {
    "emp_001": {
        "name": "Alice Green",
        "department": "Sales",
        "performance": [-99, 3, 5, 5, 4],
        "certifications": ["Excel", "Salesforce", "Excel"]
    }
}

june_hires = {
    "emp_002": {
        "name": "Ben Williams",
        "department": "Marketing",
        "performance": [3, 4, 4, 5, -99],
        "certifications": ["Google Ads", "SEO", "Google Ads"]
    }
}

july_hires = {
    "emp_003": {
        "name": "Chloe Johnson",
        "department": "HR",
        "performance": [5, 3, 5, 5],
        "certifications": ["Recruitment", "Excel"]
    }
}

sessions = [{'user_id': 'user014', 'intensity': 'high', 'duration': 38},
 {'user_id': 'user002', 'intensity': 'recovery', 'duration': 76},
 {'user_id': 'user012', 'intensity': 'low', 'duration': 81},
 {'user_id': 'user015', 'intensity': 'medium', 'duration': 98},
 {'user_id': 'user011', 'intensity': 'medium', 'duration': 104},
 {'user_id': 'user012', 'intensity': 'extreme', 'duration': 94},
 {'user_id': 'user012', 'intensity': 'medium', 'duration': 83},
 {'user_id': 'user001', 'intensity': 'high', 'duration': 90},
 {'user_id': 'user011', 'intensity': 'low', 'duration': 89},
 {'user_id': 'user011', 'intensity': 'low', 'duration': 97},
 {'user_id': 'user011', 'intensity': 'low', 'duration': 108},
 {'user_id': 'user015', 'intensity': 'medium', 'duration': 48},
 {'user_id': 'user009', 'intensity': 'low', 'duration': 17},
 {'user_id': 'user006', 'intensity': 'recovery', 'duration': 50},
 {'user_id': 'user012', 'intensity': 'extreme', 'duration': 39},
 {'user_id': 'user015', 'intensity': 'recovery', 'duration': 103},
 {'user_id': 'user012', 'intensity': 'recovery', 'duration': 91},
 {'user_id': 'user002', 'intensity': 'extreme', 'duration': 94},
 {'user_id': 'user012', 'intensity': 'medium', 'duration': 20},
 {'user_id': 'user007', 'intensity': 'high', 'duration': 45},
 {'user_id': 'user009', 'intensity': 'high', 'duration': 93},
 {'user_id': 'user007', 'intensity': 'recovery', 'duration': 106},
 {'user_id': 'user005', 'intensity': 'extreme', 'duration': 66},
 {'user_id': 'user002', 'intensity': 'extreme', 'duration': 104},
 {'user_id': 'user013', 'intensity': 'extreme', 'duration': 83},
 {'user_id': 'user008', 'intensity': 'low', 'duration': 72},
 {'user_id': 'user011', 'intensity': 'medium', 'duration': -99},
 {'user_id': 'user011', 'intensity': 'medium', 'duration': 45},
 {'user_id': 'user011', 'intensity': 'low', 'duration': 87},
 {'user_id': 'user012', 'intensity': 'recovery', 'duration': 89},
 {'user_id': 'user010', 'intensity': 'low', 'duration': 37},
 {'user_id': 'user014', 'intensity': 'high', 'duration': 104},
 {'user_id': 'user015', 'intensity': 'medium', 'duration': 75},
 {'user_id': 'user007', 'intensity': 'medium', 'duration': 29},
 {'user_id': 'user004', 'intensity': 'medium', 'duration': 26},
 {'user_id': 'user007', 'intensity': 'medium', 'duration': 85},
 {'user_id': 'user002', 'intensity': 'recovery', 'duration': 72},
 {'user_id': 'user007', 'intensity': 'low', 'duration': 97},
 {'user_id': 'user008', 'intensity': 'high', 'duration': 89},
 {'user_id': 'user005', 'intensity': 'high', 'duration': 105},
 {'user_id': 'user011', 'intensity': 'recovery', 'duration': 39},
 {'user_id': 'user014', 'intensity': 'extreme', 'duration': 66},
 {'user_id': 'user013', 'intensity': 'low', 'duration': 80},
 {'user_id': 'user008', 'intensity': 'low', 'duration': 22},
 {'user_id': 'user004', 'intensity': 'extreme', 'duration': 56},
 {'user_id': 'user014', 'intensity': 'medium', 'duration': 112},
 {'user_id': 'user015', 'intensity': 'recovery', 'duration': 104},
 {'user_id': 'user011', 'intensity': 'medium', 'duration': 62},
 {'user_id': 'user008', 'intensity': 'medium', 'duration': 110},
 {'user_id': 'user014', 'intensity': 'medium', 'duration': 77},
 {'user_id': 'user008', 'intensity': 'medium', 'duration': 39},
 {'user_id': 'user003', 'intensity': 'high', 'duration': 73},
 {'user_id': 'user009', 'intensity': 'high', 'duration': 100},
 {'user_id': 'user010', 'intensity': 'extreme', 'duration': 103},
 {'user_id': 'user015', 'intensity': 'extreme', 'duration': 111},
 {'user_id': 'user013', 'intensity': 'extreme', 'duration': 50},
 {'user_id': 'user015', 'intensity': 'extreme', 'duration': 59},
 {'user_id': 'user004', 'intensity': 'high', 'duration': 65},
 {'user_id': 'user003', 'intensity': 'recovery', 'duration': 110},
 {'user_id': 'user012', 'intensity': 'medium', 'duration': 85}]


def load_celebs():
    import os
    import pickle

    repo_url = "https://github.com/torederu/pivot-academy.git"
    repo_name = "pivot-academy"
    file_path = f"{repo_name}/celebs.pkl"

    # Check if the repository is already cloned
    if not os.path.exists(repo_name):
        # Install git-lfs
        print("Installing git-lfs...")
        os.system("git lfs install")
        
        # Clone the repository
        print(f"Cloning the repository from {repo_url}...")
        os.system(f"git clone {repo_url}")
    
    # Check if the pickle file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} not found. Check the repository or file structure.")

    # Load and return the pickle file
    print(f"Loading the pickle file from {file_path}...")
    with open(file_path, "rb") as f:
        return pickle.load(f)


def plot_image(image_array):
    """
    Plots a NumPy array as an image using Matplotlib.
    """
    import matplotlib.pyplot as plt

    plt.imshow(image_array)
    plt.axis("off")
    plt.show() 


def ppg_functions():
    os.system("wget https://raw.githubusercontent.com/torederu/pivot-academy/main/ppg_functions.py -O ppg_functions.py")
    
    # Dynamically import functions after downloading
    from ppg_functions import load_ppg_data, calculate_heart_rate_per_minute, plot_ppg_data, load_group_data
    
    # Return the imported functions directly
    return load_ppg_data, calculate_heart_rate_per_minute, plot_ppg_data, load_group_data
