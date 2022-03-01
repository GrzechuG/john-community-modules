from john_community_modules.troll_module import TrollHandler

if __name__ == "__main__":
    troll = TrollHandler()
    message = "Hello John!"

    print(troll(message))
