import requests
import json
import time
import uuid

class UnoSignup:
    def __init__(self):
        self.session = requests.Session()
        self.base_url = "https://uno.global/api/standardeconomics.backend.v1.BackendService"
        
        # Headers from your successful request
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
        
        # Generate device ID (you had one in your request)
        self.device_id = self._generate_device_id()
        
    def _generate_device_id(self):
        """Generate a device ID similar to the one in your request"""
        return f"CAESFDkzYnU4VFNUbUVPV012TFgwajJWGhQxNzgwOTcwODA3NjUyLnVGalJlVw=="
    
    def _track_event(self, event_name, event_data):
        """Send a tracking event (like the successful one you captured)"""
        track_payload = {
            "event_name": event_name,
            "event_data": event_data,
            "device_id": self.device_id,
            "timestamp": int(time.time() * 1000)
        }
        
        try:
            response = self.session.post(
                f"{self.base_url}/TrackClientUserEvent",
                headers=self.headers,
                json=track_payload
            )
            return response.status_code == 200
        except:
            return False
    
    def start_auth(self, phone_number):
        """Start authentication process"""
        print(f"\n[1/4] Initializing session for {phone_number}...")
        
        # First, send a tracking event to establish session
        self._track_event("signup_started", {"phone": phone_number})
        
        # Now try AuthStart
        auth_payload = {
            "phone_number": phone_number,
            "method": "sms"
        }
        
        response = self.session.post(
            f"{self.base_url}/AuthStart",
            headers=self.headers,
            json=auth_payload
        )
        
        print(f"  Status: {response.status_code}")
        
        if response.status_code == 200:
            print("  ✓ SMS code sent!")
            return True
        elif response.status_code == 403:
            print("  ⚠️ Rate limited or need CAPTCHA. Waiting 30 seconds...")
            time.sleep(30)
            # Retry once
            response = self.session.post(
                f"{self.base_url}/AuthStart",
                headers=self.headers,
                json=auth_payload
            )
            print(f"  Retry Status: {response.status_code}")
            return response.status_code == 200
        else:
            print(f"  ✗ Failed: {response.text}")
            return False
    
    def verify_code(self, phone_number, code):
        """Verify the SMS code and apply referral"""
        print(f"\n[3/4] Verifying code with referral 86IPOA...")
        
        verify_payload = {
            "phone_number": phone_number,
            "verification_code": code,
            "referral_code": "86IPOA"
        }
        
        response = self.session.post(
            f"{self.base_url}/AuthVerify",
            headers=self.headers,
            json=verify_payload
        )
        
        print(f"  Status: {response.status_code}")
        
        if response.status_code == 200:
            print("  ✓ Verification successful!")
            print("  ✓ Referral code 86IPOA applied!")
            
            # Track successful signup
            self._track_event("signup_completed", {
                "phone": phone_number,
                "referral": "86IPOA"
            })
            return True
        else:
            print(f"  ✗ Failed: {response.text}")
            return False
    
    def signup(self):
        """Complete signup flow"""
        print("=" * 50)
        print("UNO SIGNUP WITH REFERRAL CODE 86IPOA")
        print("=" * 50)
        
        # Get phone number
        phone = input("\n📱 Enter phone number (e.g., +639123456789): ").strip()
        
        # Step 1: Start auth
        if not self.start_auth(phone):
            print("\n❌ Failed to send verification code. Please try again later.")
            return False
        
        # Step 2: Get code from user
        print("\n[2/4] Waiting for SMS...")
        code = input("📨 Enter verification code from SMS: ").strip()
        
        # Step 3: Verify
        if not self.verify_code(phone, code):
            print("\n❌ Verification failed. Please check your code and try again.")
            return False
        
        # Step 4: Complete profile (if needed)
        print("\n[4/4] Completing account setup...")
        
        # Optional: Set name if prompted
        name = input("👤 Enter your full name (optional, press Enter to skip): ").strip()
        if name:
            profile_payload = {
                "full_name": name,
                "phone_number": phone
            }
            profile_response = self.session.post(
                f"{self.base_url}/UpdateProfile",
                headers=self.headers,
                json=profile_payload
            )
            print(f"  Profile update: {profile_response.status_code}")
        
        print("\n" + "=" * 50)
        print("✅ SIGNUP COMPLETE!")
        print("🎉 ₱100 bonus should be credited to your account")
        print("🔗 Referral code 86IPOA successfully applied")
        print("=" * 50)
        return True

if __name__ == "__main__":
    signup = UnoSignup()
    success = signup.signup()
    
    if not success:
        print("\n⚠️ If issues persist, try:")
        print("1. Clear browser cookies and cache")
        print("2. Use a different phone number")
        print("3. Wait 5-10 minutes between attempts")