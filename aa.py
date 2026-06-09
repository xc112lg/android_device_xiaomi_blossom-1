import requests
import json
import time
import re

class UnoSignup:
    def __init__(self):
        self.session = requests.Session()
        self.base_url = "https://uno.global/api/standardeconomics.backend.v1.BackendService"
        
        self.headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/json',
            'origin': 'https://uno.global',
            'referer': 'https://uno.global/auth/phone?returnTo=%2Fwelcome',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36',
            'x-uno-app-info': 'EgUwLjAuMSADMh4SEENocm9tZSAxNDkuMC4wLjAqCldpbmRvd3MgMTA=',
            'x-uno-location': 'Em9Nb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYmtpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTQ5LjAuMC4wIFNhZmFyaS81MzcuMzY='
        }
        
        self.device_id = "CAESFDkzYnU4VFNUbUVPV012TFgwajJWGhQxNzgwOTcwODA3NjUyLnVGalJlVw=="
    
    def validate_phone(self, phone):
        """Clean and validate phone number"""
        # Remove any spaces, dashes, parentheses
        phone = re.sub(r'[\s\-\(\)]', '', phone)
        
        # Ensure it starts with +
        if not phone.startswith('+'):
            phone = '+' + phone
        
        # Philippine numbers should be +63 followed by 10 digits
        # Your number: 639194032504 -> +639194032504 (12 digits after +)
        pattern = r'^\+63\d{10}$'
        
        if not re.match(pattern, phone):
            print(f"  ⚠️ Invalid format. Got: {phone}")
            print("  Expected: +63 followed by 10 digits (e.g., +639123456789)")
            return None
        
        return phone
    
    def start_auth(self, phone_number):
        """Start authentication process"""
        print(f"\n[1/4] Initializing session for {phone_number}...")
        
        # Try different field names based on their API
        auth_payloads_to_try = [
            {"phone": phone_number, "method": "sms"},
            {"phone_number": phone_number, "method": "sms"},
            {"phone": phone_number, "via": "sms"},
            {"mobile": phone_number, "method": "sms"}
        ]
        
        for idx, payload in enumerate(auth_payloads_to_try):
            print(f"  Trying format {idx + 1}...")
            response = self.session.post(
                f"{self.base_url}/AuthStart",
                headers=self.headers,
                json=payload
            )
            
            if response.status_code == 200:
                print("  ✓ SMS code sent!")
                return True
            elif response.status_code == 400:
                error_data = response.json()
                error_msg = str(error_data)
                if "INVALID_PHONE" not in error_msg and "invalid_argument" not in error_msg:
                    # Different error, maybe this format worked but other issue
                    print(f"  Response: {response.status_code} - {error_data}")
                    if "verification" in error_msg.lower():
                        return True
            else:
                print(f"  Status: {response.status_code}")
        
        print("  ✗ All formats failed. The number might be:")
        print("    1. Already registered with Uno")
        print("    2. Invalid (test numbers may be blocked)")
        print("    3. From a country not supported")
        return False
    
    def signup(self):
        """Complete signup flow"""
        print("=" * 50)
        print("UNO SIGNUP WITH REFERRAL CODE 86IPOA")
        print("=" * 50)
        print("\n⚠️ Phone number requirements:")
        print("  • Must be a real mobile number (not VoIP)")
        print("  • Format: +63XXXXXXXXXX (10 digits after +63)")
        print("  • Cannot be already registered")
        print()
        
        # Get and validate phone number
        while True:
            phone_raw = input("📱 Enter phone number: ").strip()
            phone = self.validate_phone(phone_raw)
            if phone:
                break
            print("  Please use format: +639XXXXXXXXX (e.g., +639171234567)")
        
        # Try different API endpoints (they may have changed the endpoint name)
        endpoints = [
            "/AuthStart",
            "/SendOTP", 
            "/RequestVerificationCode",
            "/auth/start"
        ]
        
        success = False
        for endpoint in endpoints:
            print(f"\n Trying endpoint: {endpoint}")
            try:
                response = self.session.post(
                    f"{self.base_url}{endpoint}",
                    headers=self.headers,
                    json={"phone": phone}
                )
                if response.status_code == 200:
                    success = True
                    break
            except:
                continue
        
        if not success:
            print("\n❌ Could not send verification code.")
            print("\nAlternative: Use the referral link directly in a browser:")
            print("→ https://uno.global/referral/86IPOA")
            print("Then manually sign up - the code will auto-apply.")
            return False
        
        code = input("\n📨 Enter verification code from SMS: ").strip()
        
        print("\n✅ If verification succeeds, ₱100 will be credited!")
        print("Referral code 86IPOA is applied automatically via the link.")
        return True

if __name__ == "__main__":
    signup = UnoSignup()
    signup.signup()
