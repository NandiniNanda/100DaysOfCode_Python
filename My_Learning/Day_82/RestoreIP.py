def restoreIpAddresses(s):
    def is_valid_segment(segment):
        # Check if the segment is valid (between 0 and 255)
        if len(segment) > 1 and segment[0] == '0':  # Avoid leading zeros
            return False
        num = int(segment)
        return 0 <= num <= 255

    def generate_ip_addresses(s, index, segments, current):
        # Base case: If we have formed 4 segments and used all characters in s
        if len(segments) == 4 and index == len(s):
            result.append(".".join(segments))
            return
        
        # Try adding a segment of length 1, 2, or 3 characters
        for length in range(1, 4):
            if index + length > len(s):
                break  # Out of bounds
            segment = s[index:index+length]
            if is_valid_segment(segment):
                segments.append(segment)
                generate_ip_addresses(s, index+length, segments, current)
                segments.pop()  # Backtrack

    result = []
    generate_ip_addresses(s, 0, [], "")
    return result

# Test cases
print(restoreIpAddresses("25525511135"))
print(restoreIpAddresses("0000"))
print(restoreIpAddresses("101023"))
