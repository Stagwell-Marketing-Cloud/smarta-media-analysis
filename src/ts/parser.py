import re 
def extract_seconds_from_timestamps(timestamps):
    """
    Extracts only the seconds from timestamps in the format ('HH:MM:SS.mmm', 'HH:MM:SS.mmm').

    Args:
        timestamps (tuple): Tuple of start and end timestamps as strings.

    Returns:
        tuple: Tuple of seconds as integers or floats (e.g., (0, 4.333)).
    """
    def parse_to_seconds(timestamp):
        # Match HH:MM:SS.mmm format and convert to seconds
        match = re.match(r'(\d+):(\d+):([\d.]+)', timestamp)
        if match:
            hours, minutes, seconds = map(float, match.groups())
            return hours * 3600 + minutes * 60 + seconds
        return 0

    start_seconds = parse_to_seconds(timestamps[0])
    end_seconds = parse_to_seconds(timestamps[1])
    return (start_seconds, end_seconds)