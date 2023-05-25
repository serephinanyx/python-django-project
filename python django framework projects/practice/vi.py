class Idea:
    def idea_display(self):
        print("WELCOME TO IDEA")
class Vodafone:
    def voda_display(self):
        print("WELCOME TO VODAFONE")
class VI(Idea,Vodafone):
    def display(self):
        self.idea_display()
        self.voda_display()
        print("WELCOME TO VI-2022")
vi=VI()
vi.display()

    
        
