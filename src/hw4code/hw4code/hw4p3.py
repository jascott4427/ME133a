import numpy as np
import matplotlib.pyplot as plt

def find_coeffs_cubic(p0, p1, v0, v1, t0, t1):

    T = t1-t0
    equations = np.array([
        [1, t0, t0**2, t0**3],
        [1, T, T**2, T**3],
        [0, 1, 2*t0, 3*t0**2],
        [0, 1, 2*T, 3*T**2]
    ])
    params = np.array([p0, p1, v0, v1])
    
    return np.linalg.solve(equations, params)

def find_coeffs_quentic(p0, p1, v0, v1, a0, a1, t0, t1):

    T = t1-t0
    equations = np.array([
        [1, t0, t0**2, t0**3, t0**4, t0**5],
        [1, T, T**2, T**3, T**4, T**5],
        [0, 1, 2*t0, 3*t0**2, 4*t0**3, 5*t0**4],
        [0, 1, 2*T, 3*T**2, 4*T**3, 5*T**4],
        [0, 0, 2, 6*t0, 12*t0**2, 20*t0**3],
        [0, 0, 2, 6*T, 12*T**2, 20*T**3],
    ])
    params = np.array([p0, p1, v0, v1, a0, a1])
    
    return np.linalg.solve(equations, params)

def plot_and_max(title, coeffs, t0, t1):
    
    t_values = np.linspace(t0, t1, 100)

    def p(t, coeffs):
        a, b, c, d = coeffs
        return a + b * t + c * t**2 + d * t**3
    def v(t, coeffs):
        a, b, c, d = coeffs
        return b + 2 * c * t + 3 * d * t**2
    
    positions = [p(t, coeffs) for t in t_values]
    velocities = [v(t, coeffs) for t in t_values]
    
    max_position = max(positions)
    print(f"Maximum position reached: {max_position:.2f} radians")

    plt.figure(figsize=(12, 6))

    plt.subplot(2, 1, 1)
    plt.plot(t_values, positions, label='Position (rad)', color='blue')
    plt.title(f'Position vs Time - {title}')
    plt.xlabel('Time (s)')
    plt.ylabel('Position (rad)')
    plt.grid()
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.plot(t_values, velocities, label='Velocity (rad/s)', color='red')
    plt.title(f'Velocity vs Time - {title}')
    plt.xlabel('Time (s)')
    plt.ylabel('Velocity (rad/s)')
    plt.grid()
    plt.legend()

    plt.tight_layout()

p0, p1, v0, v1, t0, t1 = 0, 0, 1, 0, 0, 1
coeffs = find_coeffs_cubic(p0, p1, v0, v1, t0, t1)
plot_and_max('Cubic', coeffs, t0, t1)
plot_and_max('Quintic', coeffs, t0, t1)
plt.show()




