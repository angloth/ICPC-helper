from fpdf import FPDF
from pathlib import Path

### Configuration

res_dir = "res"
res_path = Path.cwd() / res_dir

university_name = "Linköping University"
team_name = "Notorious Big O"

output_name = "NCPC-" + team_name  + ".pdf"
output_path = Path.cwd() / "out" / output_name

text_font = "times"
small_text_size = 14
big_text_size = 20
big_text_padding = 12
small_text_padding = 8

code_font = "courier"
code_size = 10
code_padding = 2


### Code
def add_text(pdf, text, font, font_size, padding, align='J'):
    pdf.set_font(font, size=font_size)
    pdf.multi_cell(w=0, h=(font_size+padding), txt=text, align=align)


def add_small_text(pdf, text, align='J'):
    add_text(pdf, text, text_font, small_text_size, small_text_padding, align)


def add_big_text(pdf, text, align='J'):
    add_text(pdf, text, text_font, big_text_size, big_text_padding, align)


def replace_tabs(code):
    return code.replace('\t', ' '*8)


def add_code_content(pdf, code_path):
    code_file = open(code_path)
    code_content = replace_tabs(code_file.read())
    add_text(pdf, code_content, code_font, code_size, code_padding, align='L')


def get_code_name(code_path):
    return str(code_path.stem).capitalize() + " implemented in " + str((code_path.suffix[1:])).capitalize()


def add_code_section(pdf, code_path):
    # Add name
    code_name = get_code_name(code_path)
    add_small_text(pdf, code_name + "\n\n")

    add_code_content(pdf, code_path)


def add_front_page(pdf, res_path):
    pdf.add_page()

    add_big_text(pdf, university_name, align='C')
    add_big_text(pdf, team_name, align='C')

    add_big_text(pdf, "")
    add_big_text(pdf, "")

    for file in res_path.iterdir():
        add_small_text(pdf, get_code_name(file))


def create_document(output_path, res_path):
    print("Begin creating ICPC document.\n")

    pdf = FPDF(orientation='P', unit='pt', format='A4')

    print("Add front page? [y/n]")

    if (input() == 'y'):
        add_front_page(pdf, res_path)
        print("\nAdded front page.\n")

    for f in res_path.iterdir():
        print("Adding: ", f)
        pdf.add_page()
        add_code_section(pdf, f)

    pdf.output(output_path)


    print("\nSuccesfully created ICPC document, saved to:", output_name)


if __name__ == "__main__":

    create_document(output_path, res_path)
