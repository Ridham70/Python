from fpdf import FPDF

class Shirtificate(FPDF):
    def create_shirtificate(self, name):
        self.add_page()
        self.set_font("Helvetica", "B", size=30)
        self.cell(0, 50, "CS50 Shirtificate", align="C")
        self.image("shirtificate.png", x=25, y=75, w=160)
        self.set_font("Helvetica", size=24)
        self.set_text_color(255, 255, 255)
        text_width = self.get_string_width(f"{name} took CS50")
        page_width = 210
        x_position = (page_width - text_width) / 2
        self.text(x_position, 135, f"{name} took CS50")


def main():
    name = input("Enter your name: ")
    pdf = Shirtificate()
    pdf.create_shirtificate(name)
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()



