import FreeSimpleGUI as fsg
from zip_creator16 import make_archive

label1 = fsg.Text("Select files to compress:")
input1 = fsg.Input()
choose1 = fsg.FilesBrowse("Choose", key="files")

label2 = fsg.Text("Select destination folder:")
input2 = fsg.Input()
choose2 = fsg.FolderBrowse("Choose", key="folder")
output_text = fsg.Text(text_color="darkgreen",font=("Arial",20))
compress_button = fsg.Button("Compress")
output_label = fsg.Text("Name the output file:      ")
output_input = fsg.Input(key="output")


window = fsg.Window("Sanaan's zipper",
                    [[label1, input1, choose1],
                     [label2, input2, choose2],
                     [output_label, output_input],
                     [compress_button, output_text]])

while True:
    event, values = window.read()
    print(event, values)
    filepaths = values["files"].split(";")
    folder = values["folder"]
    final_output = values["output"]
    make_archive(filepaths, folder, final_output)
    output_text.update(value="Compression has been completed")

window.close()
