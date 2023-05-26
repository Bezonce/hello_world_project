import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

# Enable Streamlit session state
if 'cursor_position' not in st.session_state:
    st.session_state.cursor_position = 0

# Display file uploader
video_file = st.file_uploader("Upload a video file", type=["mp4", "webm", "ogg"])

# Check if a file was uploaded
if video_file is not None:
    # Get the file name and content
    file_name = video_file.name
    file_content = video_file.read()

    # Display the video with timecode
    video_id = st.video(file_content, format='video/mp4', start_time=0)

    # Generate random signal
    np.random.seed(0)
    signal = np.random.randn(100)

    # Create a time axis for the signal
    time = np.arange(len(signal))

    # Calculate cursor time based on video timecode
    cursor_time = int((st.session_state.cursor_position / 100) * len(signal))

    # Plot the signal with the cursor
    fig, ax = plt.subplots()
    ax.plot(time, signal)
    ax.axvline(x=cursor_time, color='r', linestyle='--')
    ax.set_xlabel('Time')
    ax.set_ylabel('Signal')
    st.pyplot(fig, clear_figure=True)

    # Create JavaScript callback function
    js_code = """
    var video = document.querySelector('video');
    var cursor = document.querySelector('input[type="range"]');

    function syncVideoCursor(event) {
        const currentTime = (event.currentTarget.currentTime / event.currentTarget.duration) * 100;
        cursor.value = currentTime.toFixed(2);
        cursor.dispatchEvent(new Event('input'));
    }

    video.addEventListener('timeupdate', syncVideoCursor);
    """

    # Execute JavaScript code
    st.script(js_code)

    # Update video playback based on cursor position
    cursor_position = st.slider("Cursor position", min_value=0, max_value=100, value=st.session_state.cursor_position, key='slider')
    st.session_state.cursor_position = cursor_position

    # Calculate cursor time based on video timecode
    cursor_time = int((cursor_position / 100) * len(signal))

    # Synchronize video playback with cursor
    st.experimental_set_component_value(video_id, {'time': (cursor_time / len(signal)) * st.video.get_video_duration(video_id)})
