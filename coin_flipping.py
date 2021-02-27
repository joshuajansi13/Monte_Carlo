import random
import matplotlib.pyplot as plt


def coin_flip():
    return random.randint(0, 1)

# Monte Carlo Simulation:

# Empty list to store the probability values.
list1 = []


def monte_carlo(n):
    results = 0
    for i in range(n):
        flip_result = coin_flip()
        results = results + flip_result

        # Calculating probability value:
        prob_value = results/(i+1)

        # Append the probability values to the list:
        list1.append(prob_value)
    return results/n

# Call the function:
answer = monte_carlo(5000)
print("Final value: ", answer)

# Plot the results:
plt.axhline(y=0.5, color='r', linestyle='-')
plt.xlabel("Iterations")
plt.ylabel("Probability")
plt.plot(list1)
plt.show()
