from fpdf import FPDF

class Shirtificate(FPDF):
    def heading(self):
        self.set_font(family="helvetica", style="B", size=30)
        self.set_text_color(r=0, g=0, b=0)
        self.cell(w=0, h=50, text="CS 50 Shirtificate", border=0, align="C", new_y="NEXT")

    def text(self, name):
        self.set_font(family="helvetica", size=25)
        self.set_text_color(r=255, g=255, b=255)
        self.cell(w=0, h=30, text=f"{name} took CS50", border=0, align="C")

def main():
    name = input("Name: ")
    new_shirt = Shirtificate()
    new_shirt.add_page()
    new_shirt.set_auto_page_break(auto=False, margin=0)
    new_shirt.heading()
    new_shirt.image("shirtificate.png", x="C", w=190)
    new_shirt.set_y(125)
    new_shirt.text(name)
    new_shirt.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
