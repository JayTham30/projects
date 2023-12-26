import requests
import hashlib
import sys




# Request data using the hash version of our password(query_char).
# Checks the status for the response to ensure it is [200] if not it will raise an error.
def request_api_data(query_char):
   url = "https://api.pwnedpasswords.com/range/" + query_char
   res = requests.get(url)
   if res.status_code != 200:
       raise RuntimeError(f"Error fetching: {res.status_code}, Check the API and try again")
   return res


# Check password if it exists in API response


def get_password_leaked_count(hashes, hash_to_check):
   hashes = (line.split(":") for line in hashes.text.splitlines())
   for h, count in hashes:
       if h == hash_to_check:
           return count
   return 0


# Hashes the password using the Hashlib and put it into uppercase


def pwned_api_checked(password):
   sha1password = (hashlib.sha1(password.encode("utf-8")).hexdigest().upper())
   first5_char, tail = sha1password[:5], sha1password[5:]
   response = request_api_data(first5_char)
   return get_password_leaked_count(response, tail)




def main(args):
   for password in args:
       count = pwned_api_checked(password)
       if count:
           print(f"{password} was found {count} times.....you should probably change your password")
       else:
           print(f"{password} was NOT found. Carry on")
   return "done"


if __name__ == "__main__":
   sys.exit(main(sys.argv[1:]))




