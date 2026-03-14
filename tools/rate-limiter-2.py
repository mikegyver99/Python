# Create simple rate limiter
# def Class
# needs 3 properties MaxRequests, IP, length of time,  
# need to track IPs and filter out/remove expired ones
import time

class RateLimiter():
    def __init__(self, maxrequests, timeout):
        self.maxrequests = maxrequests
        self.timeout = timeout
        self.tracker = {}  # Dictionary: { "ip": [timestamps] }


    def trackip(self, ip):
        self.ip = ip
        self.current_time = time.time()
        # 1. Handle new IPs: If the IP isn't in our tracker yet, add it
        if ip not in self.tracker:
            self.tracker[ip] = []
        # 2. Cleanup: Create a new list of non-expired timestamps
        valid_timestamp = []
        print(self.tracker[ip])
        for t in self.tracker[ip]:
            if self.current_time - float(t) < self.timeout:
                valid_timestamp.append(t)
                # print(valid_timestamp)
        # Update the dictionary with only valid ones
        self.tracker[ip] = valid_timestamp

        if len(self.tracker[ip]) < self.maxrequests:
            self.tracker[ip].append(self.current_time)
            return f"Request accepted. Total requests in window: {len(self.tracker[ip])}"
        else:
            return f"Rate limit exceeded! Max allowed: {self.maxrequests}"

limiter = RateLimiter(3, 5) # Max 3 requests every 5 seconds
# print(testing.trackip())
for i in range(15):
    time.sleep(1)
    print(limiter.trackip("10.0.0.1"))
    