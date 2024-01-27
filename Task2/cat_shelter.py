import sys

def analyze_cat_shelter(log_file):
    try:
        # Open the specified log file for reading
        with open(log_file, 'r') as file:
            # Initialize variables to store cat shelter statistics
            cat_entries = 0
            intruder_doused = 0
            total_time_in_house = 0
            visit_durations = []

            # Iterate through each line in the log file
            for line in file:
                # Check for the end of the log
                if line.strip() == 'END':
                    break

                # Extract information from the log entry
                cat_name, entry_time, exit_time = line.strip().split(',')
                entry_time, exit_time = int(entry_time), int(exit_time)
                duration = exit_time - entry_time

                # Analyze the entry based on cat name
                if cat_name == 'OURS':
                    cat_entries += 1
                    total_time_in_house += duration
                    visit_durations.append(duration)
                else:
                    intruder_doused += 1

            # Display analysis results
            if cat_entries == 0:
                print("No visits from the correct cat.")
            else:
                avg_duration = sum(visit_durations) / len(visit_durations)
                max_duration = max(visit_durations)
                min_duration = min(visit_durations)

                print("Log File Analysis")
                print("==================")
                print(f"Cat Visits: {cat_entries}")
                print(f"Other Cats: {intruder_doused}")
                print(f"Total Time in House: {total_time_in_house // 60} Hours, {total_time_in_house % 60} Minutes")
                print(f"Average Visit Length: {int(avg_duration)} Minutes")
                print(f"Longest Visit: {max_duration} Minutes")
                print(f"Shortest Visit: {min_duration} Minutes")

    except FileNotFoundError:
        # Handle the case where the specified file does not exist
        print(f'Error: Cannot open "{log_file}". The file does not exist.')
    except Exception as e:
        # Handle unexpected errors during file processing
        print(f'An unexpected error occurred: {e}')

def run_analyzer():
    # Check if the correct number of command line arguments is provided
    if len(sys.argv) != 2:
        print("Error: Missing command line argument! Please provide the log file name.")
    else:
        # Run the cat shelter log analyzer with the provided log file
        log_file = sys.argv[1]
        analyze_cat_shelter(log_file)

if __name__ == "__main__":
    # Executing the cat shelter log analyzer when the script is running
    run_analyzer()
