class travels:
    def name(self):
        print("KPN travels")
class travels1:
    def name1(self):
        print("VPN travels")
class main(travels,travels1):
    def luxary(self):
        print("Enjoy the journey of happiness")
m=main()
m.name()
m.name1()
m.luxary()