from coinone_api_class import CoinoneAPIManager

if __name__   == "__main__":

    API_Class = CoinoneAPIManager()

    print(API_Class.get_result("Balance"))
    print("\n")
    print(API_Class.get_result('Daily Balance'))
    print("\n")
    print(API_Class.get_result('Deposit Address'))
    print("\n")
    print(API_Class.get_result('User Information'))
    print("\n")
    print(API_Class.get_result('Virtual Account'))
    print("\n")