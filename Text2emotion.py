from paralleldots import set_api_key, get_api_key,emotion

api_key="GETYO'OWNKEY"

def emotion_scanning():
        print("Enter your input")
        x=input()
        error_checker(x)
        y=emotion(x)
        print(y['emotion']['emotion'])

def error_checker(text):
        api_key  = get_api_key()
        if not api_key == None:
                if type(text) != str:
                        return { "Error": "Input must be a string." }
                elif text == "":
                        return { "Error": "Input string cannot be empty." }
        else:
                return { "Error": "API key does not exist" }


if __name__ == "__main__":
        set_api_key(api_key)
        status ="xxx"
        while (not status == "exit()"):
                emotion_scanning()
                print("if you want to exit, enter 'exit()', else press enter")
                status=input()
                      
                

       
        

