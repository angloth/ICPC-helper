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
small_text_size = 12
big_text_size = 14
big_text_padding = 8
small_text_padding = 8

code_font = "courier"
code_size = 8
code_padding = 2


### Code
def add_text(pdf, text, font, font_size, padding):
    pdf.set_font(font, size=font_size)
    pdf.multi_cell(w=0, h=(font_size+padding), txt=text, align='J')


def add_small_text(pdf, text):
    add_text(pdf, text, text_font, small_text_size, small_text_padding)


def add_big_text(pdf, text):
    add_text(pdf, text, text_font, big_text_size, big_text_padding)


def replace_tabs(code):
    return code.replace('\t', '    ')


def add_code_content(pdf, code_path):
    code_file = open(code_path)
    code_content = replace_tabs(code_file.read())
    add_text(pdf, code_content, code_font, code_size, code_padding)


def add_code_section(pdf, code_path):
    # Add name
    code_name = str(code_path.stem).capitalize() + " implemented in " + str((code_path.suffix[1:])).capitalize()
    add_big_text(pdf, code_name + "\n\n")

    add_code_content(pdf, code_path)


def create_document(output_path, res_path):
    print("Begin creating ICPC document.\n")

    pdf = FPDF(orientation='P', unit='pt', format='A4')

    for f in res_path.iterdir():
        print("Adding: ", f)
        pdf.add_page()
        add_code_section(pdf, f)

    pdf.output(output_path)


    print("\nSuccesfully created ICPC document, saved to:", output_name)


if __name__ == "__main__":

    create_document(output_path, res_path)
