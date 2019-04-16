class differences:
    def __init__(self, dict):
        self.dict = dict

    def giveIntersection(self):
        s = list(self.dict.values())
        for i in range(len(s)):
            s[i] = set(s[i]).intersection(s[i-1])
        print(s[i])

def main():
    n = int(input("How many list you have? "))
    dict1 = {}
    for i in range(n):
        dict1[i] = list(input("Enter list: ").split())

    s = differences(dict1)
    s.giveIntersection()

if __name__ == "__main__":
    main()
