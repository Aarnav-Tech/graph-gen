# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 17:01:30 2024

@author: Aarnav
"""
import matplotlib.pyplot as plt
import time as t

print('Welcome to Linegraph creator!')
# Just for dramatics lol
t.sleep(1)
print('Loading.....')
t.sleep(1)
print('Loading.....')
t.sleep(1)
print('Loaded!')
t.sleep(1)

def display_marker_options():
    # Display available marker types
    print("Available marker types:")
    t.sleep(.3)
    print(" 'o' : Circle")
    t.sleep(.3)
    print(" 's' : Square")
    t.sleep(.3)
    print(" '^' : Triangle")
    t.sleep(.3)
    print(" 'D' : Diamond")
    t.sleep(.3)
    print(" 'x' : X marker")
    t.sleep(.3)
    print(" '+' : Plus marker")
    t.sleep(.3)
    print(" '|' : Vertical line marker")
    t.sleep(.3)
    print(" '_' : Horizontal line marker")

def get_user_input():
    # Get the number of data points
    num_points = int(input("How many data points do you want to plot?: "))
    
    # Initialize lists to hold x and y values
    x_values = []
    y_values = []
    
    # Collect x and y values from the user
    for i in range(num_points):
        x = float(input(f"Enter x value for point {i + 1}: "))
        y = float(input(f"Enter y value for point {i + 1}: "))
        x_values.append(x)
        y_values.append(y)
    
    return x_values, y_values

def plot_graph(x_values, y_values, marker_type):
    #plt.figure(figsize=(10, 5))
    plt.plot(x_values, y_values, marker=marker_type)
    plt.title('Them Graph')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.grid()
    plt.xticks(x_values)  # Set x-ticks to the x values
    plt.yticks(y_values)  # Set y-ticks to the y values
    
    # Set limits to always include the origin
    plt.xlim(left=min(0, min(x_values)), right=max(x_values) + 1)  # Adjust right limit as needed
    plt.ylim(bottom=min(0, min(y_values)), top=max(y_values) + 1)  # Adjust top limit as needed
    
    plt.show()

def main():
    display_marker_options()  # Display marker options to the user
    marker_type = input("Please enter a marker type from the above options: ")
    
    x_values, y_values = get_user_input()
    plot_graph(x_values, y_values, marker_type)

if __name__ == "__main__":
    main()
