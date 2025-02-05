import requests

def fetch_random_user_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()
    
    if data["success"] and "data" in data:
        user_data = data["data"]
        user_name = user_data["login"]["username"]
        location = user_data["location"]
        cordinates = location["coordinates"]
        country = user_data["location"]["country"]
        latitude = cordinates["latitude"]
        longitude = cordinates["longitude"]

        return user_name, country, latitude,longitude
    else:
        raise Exception("failed to fetch the user data")
    

def main():
    try:
        username, country, latitude, longitude = fetch_random_user_freeapi()
        print(f"username: {username}\n country: {country}\n cordinates: {latitude} , {longitude} ")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()


