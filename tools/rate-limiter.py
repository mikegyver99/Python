import time

class RateLimiter:
    def __init__(self, max_requests=10, time_window=60):
        self.max_requests = max_requests
        self.time_window = time_window
        self.requests = {}  # This was missing in the original code

    def is_allowed(self, ip):
        current_time = time.time()

        if ip not in self.requests:
            self.requests[ip] = []  # manually initialize if IP is new

        # Remove outdated requests
        self.requests[ip] = [t for t in self.requests[ip] if current_time - t < self.time_window]
        
        # Check if the number of requests in the current time window is less than the maximum allowed
        if len(self.requests[ip]) < self.max_requests: # This was missing in the original code
            self.requests[ip].append(current_time)  # This was missing in the original code
            print(self.requests[ip])  # Troubleshooting: print the list of request timestamps for the IP address
            return True
        else:
            return False

# Example usage
if __name__ == "__main__": #  added this to prevent code from running if imported as a module
    rate_limiter = RateLimiter()
    ip_address = "10.10.10.10"
    for i in range(12):
        if rate_limiter.is_allowed(ip_address):
            print(f"Request {i+1} from {ip_address} allowed.")
        else:
            print(f"Request {i+1} from {ip_address} denied. Rate limit exceeded.")
        time.sleep(1)
        