def load_ppg_data(base_heart_rate=1.5):
    """
    Generates a realistic synthetic PPG signal split into 10 segments
    (one per minute), with linear drift, sharp peaks, and noise.

    Args:
        base_heart_rate (float): Base heart rate in Hz (default: 1.5 Hz = 90 BPM).

    Returns:
        ppg_data (numpy array): Shape (3, 600, 10), where NaNs are introduced as specified.
    """
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy.signal import sawtooth

    # **Master seed to make results consistent for all students**
    np.random.seed(42)

    # Define fixed seeds for different parts of the signal
    freq_seeds = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109]
    hrv_seeds = [200, 201, 202, 203, 204, 205, 206, 207, 208, 209]
    noise_seeds = [300, 301, 302, 303, 304, 305, 306, 307, 308, 309]
    nan_seed = 999  # Fixed seed for NaN positions

    # Sampling rate (Hz) and duration
    fs = 100  # 100 Hz sampling frequency
    duration = 60  # 60 seconds
    t = np.linspace(0, duration, fs * duration)  # Time vector (6000 samples)

    # Initialize PPG wave
    ppg_wave = np.zeros_like(t)

    # Generate PPG wave with variability per segment
    for i in range(10):
        start = i * 600
        end = start + 600

        # **Vary heart rate frequency slightly per segment based on fixed seeds**
        np.random.seed(freq_seeds[i])
        freq_variation = base_heart_rate + np.random.uniform(-0.1, 0.1)
        systolic_wave = np.exp(-0.5 * ((t[start:end] % (1/freq_variation)) / 0.07) ** 2)
        dicrotic_wave = 0.2 * np.exp(-0.5 * (((t[start:end] - 0.2) % (1/freq_variation)) / 0.02) ** 2)

        # Combine waves for the current segment
        segment_wave = systolic_wave - dicrotic_wave

        # **Add heart rate variability (HRV) per segment based on fixed seeds**
        np.random.seed(hrv_seeds[i])
        hrv_variation = np.random.uniform(-0.05, 0.05, size=segment_wave.shape)
        segment_wave += hrv_variation

        # **Add segment-specific noise based on fixed seeds**
        np.random.seed(noise_seeds[i])
        noise = np.random.randn(600) * 0.02  # Increased noise for realism
        segment_wave += noise

        # Place segment wave into the full PPG wave
        ppg_wave[start:end] = segment_wave

    # **Add a simple, consistent linear drift across the entire signal**
    linear_drift = np.linspace(1, 10, len(ppg_wave))
    ppg_wave += linear_drift  # Easy to remove later

    # Reshape into (3, 600, 10) format
    ppg_data = np.tile(ppg_wave, (3, 1)).reshape(3, 600, 10)

    # **Introduce NaNs in Channel 1, 2, and 3 with fixed seeds**
    np.random.seed(nan_seed)

    # Track used NaN indices to avoid overlap
    used_indices = set()

    # Channel 1: Introduce 22 NaNs without overlap
    while len(used_indices) < 22:
        idx = np.random.choice(600 * 10)
        if idx not in used_indices:
            used_indices.add(idx)
            ppg_data[0, idx // 10, idx % 10] = np.nan

    # Channel 2: Introduce 58 NaNs without overlap
    while len(used_indices) < 22 + 58:
        idx = np.random.choice(600 * 10)
        if idx not in used_indices:
            used_indices.add(idx)
            ppg_data[1, idx // 10, idx % 10] = np.nan

    # Channel 3: Introduce 3226 NaNs without overlap
    while len(used_indices) < 22 + 58 + 3226:
        idx = np.random.choice(600 * 10)
        if idx not in used_indices:
            used_indices.add(idx)
            ppg_data[2, idx // 10, idx % 10] = np.nan

    return ppg_data

def calculate_heart_rate_per_minute(ppg_signal):
    """
    Computes heart rate for each minute from a PPG signal of shape (6000,1).
    Internally reshapes to (10, 600) to preserve segment structure.

    Args:
        ppg_signal (numpy array): Must be of shape (6000,1).

    Returns:
        heart_rate_per_min (numpy array): Shape (10,), estimated HR per minute.

    Raises:
        ValueError: If the input shape is incorrect.
    """
    import numpy as np
    from scipy.signal import find_peaks

    if ppg_signal.shape != (6000, 1):
        raise ValueError(f"Expected shape (6000,1), but got {ppg_signal.shape}. Please reshape using `.reshape(6000,1)`.")

    # Replace NaNs with the mean of valid data to avoid NaN results
    ppg_signal = np.nan_to_num(ppg_signal, nan=np.nanmean(ppg_signal))

    # **Reshape to (10, 600) to preserve segment structure**
    ppg_signal = ppg_signal.reshape((10, 600))

    # Define sampling rate
    sample_rate = 100  # Hz

    heart_rates = []

    for i in range(10):
        segment = ppg_signal[i, :]

        # Check if the segment contains only NaNs
        if np.all(np.isnan(segment)):
            heart_rates.append(np.nan)
            continue

        # Use a more lenient threshold to capture more peaks
        threshold = np.mean(segment) + 0.5 * np.std(segment)
        peaks, _ = find_peaks(segment, height=threshold, distance=30)

        # Compute time differences between beats
        beat_intervals = np.diff(peaks)

        # If no beats detected, store NaN
        if len(beat_intervals) == 0:
            heart_rate = np.nan
        else:
            heart_rate = (sample_rate / np.mean(beat_intervals)) * 60  # Convert intervals to BPM

        heart_rates.append(heart_rate)

    return np.array(heart_rates)  # Shape (10,)

def plot_ppg_data(ppg_data):
    """
    Plots PPG data with support for (6000,) and (3, 6000) shaped arrays.
    Always plots the first 500 data points for clarity.

    Args:
        ppg_data (numpy array): Input PPG data, shape (6000,) or (3, 6000).
    """
    import matplotlib.pyplot as plt

    # Determine the shape of the input data
    if ppg_data.ndim == 1:
        # Single channel case: (6000,)
        plt.figure(figsize=(10, 4))
        plt.plot(ppg_data[:500], label="PPG Signal")
        plt.title("PPG Signal (First 500 Samples)")
        plt.xlabel("Sample Number")
        plt.ylabel("Amplitude")
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.legend()
        plt.tight_layout()
        plt.show()

    elif ppg_data.ndim == 2 and ppg_data.shape[0] == 3:
        # Multi-channel case: (3, 6000)
        fig, axs = plt.subplots(3, 1, figsize=(10, 8), sharex=True)
        for i in range(3):
            axs[i].plot(ppg_data[i, :500], label=f"Channel {i+1}")
            axs[i].set_title(f"PPG Signal - Channel {i+1} (First 500 Samples)")
            axs[i].set_ylabel("Amplitude")
            axs[i].grid(True, linestyle='--', alpha=0.7)
            axs[i].legend()

        axs[-1].set_xlabel("Sample Number")
        plt.tight_layout()
        plt.show()

    else:
        print("Error: Input data must have shape (6000,) or (3, 6000).")


def load_group_data():
    """
    Generates PPG data for 5 participants with different base heart rates.

    Returns:
        list of numpy arrays: Each element is PPG data for one participant.
    """
    # Define base heart rates in Hz (~75, 80, 85, 90, 95 BPM)
    base_hrs = [1.25, 1.33, 1.42, 1.5, 1.58]

    # Generate PPG data for each participant
    group_data = [load_ppg_data(base_hr) for base_hr in base_hrs]

    return group_data
