import csv
import random


# QuickSort function with comparison count tracker
def quicksort(arr, count_comparisons=0):
    if len(arr) <= 1:
        return arr, count_comparisons

    # Choose a pivot
    pivot = arr[-1]
    less, greater = [], []

    # Partitioning process
    for i in range(len(arr) - 1):
        count_comparisons += 1  # Count each comparison
        if arr[i] <= pivot:
            less.append(arr[i])
        else:
            greater.append(arr[i])

    # Recursively sort and combine results
    sorted_less, count_comparisons = quicksort(less, count_comparisons)
    sorted_greater, count_comparisons = quicksort(greater, count_comparisons)

    return sorted_less + [pivot] + sorted_greater, count_comparisons


# Function to read the CSV and extract latitudes and latitude-longitude pairs
def read_lat_lon_from_csv(file_path):
    latitudes = set()
    lat_lon_pairs = set()

    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Extract latitude and longitude as floats
            lat = float(row['lat'])
            lng = float(row['lng'])
            latitudes.add(lat)
            lat_lon_pairs.add((lat, lng))

    return list(latitudes), list(lat_lon_pairs)


# Part (a): Sorting unique latitudes
def sort_latitudes(latitudes):
    sorted_latitudes, comparison_count = quicksort(latitudes, 0)
    return sorted_latitudes, comparison_count


# Part (b): Sorting with shuffling
def sort_latitudes_with_shuffle(latitudes):
    random.shuffle(latitudes)
    sorted_latitudes, comparison_count = quicksort(latitudes, 0)
    return sorted_latitudes, comparison_count


# Part (c): Sorting (latitude, longitude) pairs
def sort_lat_lon_pairs(lat_lon_pairs):
    sorted_pairs, comparison_count = quicksort(lat_lon_pairs, 0)
    return sorted_pairs, comparison_count


# Function to save sorted latitudes to CSV
def save_latitudes_to_csv(sorted_latitudes, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["latitude"])
        for lat in sorted_latitudes:
            writer.writerow([lat])


# Function to save sorted (latitude, longitude) pairs to CSV
def save_lat_lon_pairs_to_csv(sorted_lat_lon_pairs, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["latitude", "longitude"])
        for lat, lon in sorted_lat_lon_pairs:
            writer.writerow([lat, lon])


# Main function to execute the tasks
def main(file_path):
    # Read data from CSV
    latitudes, lat_lon_pairs = read_lat_lon_from_csv(file_path)

    # Part (a): Sort unique latitudes
    sorted_latitudes, comp_count_latitudes = sort_latitudes(latitudes)
    #print("Sorted latitudes:", sorted_latitudes)
    print("Comparisons (no shuffle):", comp_count_latitudes)

    # Save sorted latitudes to CSV
    save_latitudes_to_csv(sorted_latitudes, "sorted_latitudes.csv")

    # Part (b): Sort with shuffling
    sorted_latitudes_shuffled, comp_count_latitudes_shuffled = sort_latitudes_with_shuffle(latitudes)
    #print("Sorted latitudes with shuffle:", sorted_latitudes_shuffled)
    print("Comparisons (with shuffle):", comp_count_latitudes_shuffled)

    # Part (c): Sort (latitude, longitude) pairs
    sorted_lat_lon, comp_count_lat_lon = sort_lat_lon_pairs(lat_lon_pairs)
    #print("Sorted (latitude, longitude) pairs:", sorted_lat_lon)
    print("Comparisons for (latitude, longitude) pairs:", comp_count_lat_lon)

    # Save sorted (latitude, longitude) pairs to CSV
    save_lat_lon_pairs_to_csv(sorted_lat_lon, "sorted_lat_lon_pairs.csv")


# Example usage
# Replace 'cities.csv' with your actual file path
file_path = 'worldcities.csv'
main(file_path)
